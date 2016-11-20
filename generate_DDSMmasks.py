# -*- coding: utf-8 -*-
"""
python 3.5
@author: jcx9dy
"""
import sys
import os
import numpy as np
#import matplotlib.pyplot as plt
#import cv2
from PIL import Image 
from scipy.ndimage import binary_fill_holes, binary_erosion, imread
#from skimage import io, img_as_bool
#from skimage.transform import resize
#import glob

#%%
def parse_chaincode(row, col, key):
    
    #DDSM chaincode assumes: 
        #7 0 1
        #6 x 2
        #5 4 3

    #typically,  origin [0, 0] of image is the top-left corner
    chainstep = {'0': (row - 1 , col     ), 
                 '1': (row - 1 , col + 1 ),
                 '2': (row     , col + 1 ),
                 '3': (row + 1 , col + 1 ),
                 '4': (row + 1 , col     ),
                 '5': (row + 1 , col - 1 ),
                 '6': (row     , col - 1 ),
                 '7': (row - 1 , col - 1 )}

    return(chainstep[key])

def parse_boundary(height, width, chaincode, pad=25):
    #chaincode should be a list of strings
    
    if not (pad >= 0):
        raise ValueError('pad should be greater or equal to zero, not: ' + pad)

    #check ends with '#'
    if chaincode[-1] != '#':
        raise ValueError('Chaincode should end in "#"')
        
    #initialize blank mask with 25px padding all around
    boundary_pad = np.zeros( (height + 2*pad, width + 2*pad), dtype='bool')
    col = pad + int( chaincode[0] ) - 1  #-1 b/c python is 0-indexed
    row = pad + int( chaincode[1] ) - 1
    boundary_pad[row, col] = True

    for i in range(2, len(chaincode) - 1):   

        row, col = parse_chaincode(row, col, chaincode[i])
        boundary_pad[row, col] = True

        if ( col == pad + int( chaincode[0] ) - 1 ) and ( row == pad + int( chaincode[1] ) - 1 ):
            break #sometimes chaincode exceeds start (e.g. ./benign_01/case0241/C_0241_1.LEFT_MLO.OVERLAY)
    
    #check end pixel closes loop
    if ( (col - (pad + int( chaincode[0] ) - 1))^2 + (row - (pad + int( chaincode[1] ) - 1  ))^2 ) > 1.5:  #sqrt(2) being the diagonal (max) distance in 8-connectivity
        raise ValueError('Final pixel in chaincode not close enough to start pixel...')
    
    #fill boundary
    mask_pad = binary_fill_holes(boundary_pad)
    if not (np.sum(mask_pad) > np.sum(boundary_pad)): 
        ValueError('Unable to fill boundary')
    
    imgborder_pad = np.zeros( (height + 2*pad, width + 2*pad), dtype='bool')
    
    #left border numpy indexing is [a,b)
    imgborder_pad[ pad : pad + height   ,   pad ] = True
    #right border
    imgborder_pad[ pad : pad + height   ,   pad + width - 1 ] = True
    #top border
    imgborder_pad[ pad   ,   pad : pad + width ] = True
    #bottom border
    imgborder_pad[ pad + height - 1   ,   pad : pad + width ] = True
    
    #calculate border fix
    fixgap_pad = np.logical_and(imgborder_pad, mask_pad)
    #plt.imshow(boundary.astype(int), cmap='gray')
    #plt.imshow(binary_fill_holes(boundary), cmap='gray')
    
    #crop to original size
    boundary = np.zeros( (height, width), dtype='bool')
    boundary[boundary_pad[pad : pad + height,  pad : pad + width]] = True
    #add border fix to boundary
    boundary[fixgap_pad[pad : pad + height,  pad : pad + width]] = True
    mask = np.zeros( (height, width), dtype='bool')
    mask[mask_pad[pad : pad + height,  pad : pad + width]] = True
    
    return boundary, mask

def parse_icsfile(icspath):
    f = open(icspath, 'r')
    icslines = f.read().splitlines()
    f.close()
    
    age = 0
    density = 0
    dim_dict = {'LEFT_CC': (0, 0), 
                'LEFT_MLO': (0, 0), 
                'RIGHT_CC': (0, 0), 
                'RIGHT_MLO': (0, 0)}
    
    for i in range(len(icslines)):
            
        fields = icslines[i].split()
        
        if len(fields) > 0:  #handles empty lines
            if (fields[0] == 'PATIENT_AGE') and (len(fields) > 1):  #some patients don't have an age (e.g. ./benign_08/case1735/A-1735-1.ics)
                age = int( fields[1] )
                
            if fields[0] == 'DENSITY':   #BIRADS density 1 low (lower quartile, mostly fat), 4 high (upper quartile)
                density = int( fields[1] )
                
            if fields[0] in dim_dict:
                height = int( fields[2] )
                width = int( fields[4] )
                dim_dict[fields[0]] = (height, width)
    
    return age, density, dim_dict

def parse_overlayfile(overlaypath, height, width, age=None, density=None):

    f = open(overlaypath, 'r')
    overlaylines = f.read().splitlines()
    f.close()
    
    #   1963 BENIGN
    #    729 BENIGN_WITHOUT_CALLBACK
    #   1935 MALIGNANT
    #     37 UNPROVEN
    
    groundtruth = {'BENIGN': [],
                  'BENIGN_WITHOUT_CALLBACK': [],
                  'MALIGNANT': [],
                  'UNPROVEN': []}
    assessment = None
    subtlety = None
    pathology = ""
    flagDrawBoundary = False
    
    for i in range(len(overlaylines)):
        
        fields = overlaylines[i].split()
        
        if len(fields) > 0:    #handles empty lines
            if flagDrawBoundary == True: 
                #assumes other variables for current lesion has already been set
                
                boundary, mask = parse_boundary(height, width, fields)
                
                lesion = {'ASSESSMENT': assessment, 'SUBTLETY': subtlety, 'BOUNDARY': boundary, 'MASK': mask}
                if age != None: 
                    lesion['PATIENT_AGE'] = age
                if density != None:
                    lesion['DENSITY'] = density
                groundtruth[pathology].append(lesion) #apparently, append is in-place op
                
                #reset flag
                flagDrawBoundary = False
            
            if fields[0] == 'ASSESSMENT':     # ACR BI-RADS assessment code 
                assessment = int( fields[1] )
            
            if fields[0] == 'SUBTLETY':       # mammographer-assigned "subtlety rating" on a scale of 1 to 5, where 1 is "subtle" and 5 is "obvious."
                subtlety = int( fields[1] )

            if fields[0] == 'PATHOLOGY':
                pathology = fields[1]
                
            if fields[0] == 'BOUNDARY':
                flagDrawBoundary = True
                  #next line will be chain code

    return groundtruth
              

#%%
############################################################
##########  MAIN

#Given an overlay file path
   # assumes this format:   '.../cancer_01/case3013/B_3013_1.RIGHT_MLO.OVERLAY'
   # assumes ics in:        '.../cancer_01/case3013/B-3013-1.ics'
   # assumes png in:          '...//cancer_01/case3013/PNGFiles/B_3013_1.RIGHT_MLO.png'

#RUN AS FOLLOWS:   python3 generate_DDSMmasks.py ./cancer_01/case3013/B_3013_1.RIGHT_MLO.OVERLAY
  # or parallelize:   parallel --eta -a OVERLAYfiles.txt python3 generate_DDSMmasks.py {}
  # ~22min for just masks (no patches) on 8-core

overlaypath = sys.argv[1]
print('Processing:  ' + overlaypath)
basepath, overlayfile = os.path.split(overlaypath)
imagename = os.path.splitext(overlayfile)[0]
casename = overlaypath.split('/')[-2]
volumename = overlaypath.split('/')[-3]

#%%

icspath = basepath + '/' + os.path.splitext(imagename)[0].replace('_', '-') + '.ics'   #why did they switch to hyphens?!?
age, density, dimensions = parse_icsfile(icspath)

view = imagename.split('.')[1]
height, width = dimensions[view]

#groundtruth = parse_overlayfile(overlaypath, height, width)
groundtruth = parse_overlayfile(overlaypath, height, width, age, density) 

#make masks and save
os.makedirs(basepath + '/masks/', exist_ok=True)
mask_benign = np.zeros((height, width), dtype='bool')
mask_malignant = np.zeros((height, width), dtype='bool')

for p in groundtruth.keys():
    
    for i, shape in enumerate(groundtruth[p]):
        savename = imagename + '_' + p + str(i)
        boundary = shape['BOUNDARY']
        mask = shape['MASK']
        #save as lossless-compressed png ~13KB
        Image.fromarray(boundary.astype('uint8')*255).save(basepath + '/masks/' + savename + '.boundary.png')
        Image.fromarray(mask.astype('uint8')*255).save(basepath + '/masks/' + savename + '.mask.png')
        
        if p == 'BENIGN':
            mask_benign = np.logical_or(mask, mask_benign)
            if i == len(groundtruth[p]) - 1:
                Image.fromarray(mask_benign.astype('uint8')*255).save(basepath + '/masks/' + imagename + '_' + p  + '.merged.png')
        if p == 'MALIGNANT':
            mask_malignant = np.logical_or(mask, mask_malignant)
            if i == len(groundtruth[p]) - 1:
                Image.fromarray(mask_malignant.astype('uint8')*255).save(basepath + '/masks/' + imagename + '_' + p + '.merged.png')

        #delete boundary from groundtruth (so we can later save the metadata as small .npy)
        del(groundtruth[p][i]['BOUNDARY'])
        del(groundtruth[p][i]['MASK'])
        
#save metadata with np.save (alternative is pickle module, but np.save uses pickle too)
np.save(basepath + '/masks/' + imagename + '.groundtruth.npy', groundtruth)
#groundtruth = np.load(basepath + '/masks/' + savename + '.groundtruth.npy').item()

