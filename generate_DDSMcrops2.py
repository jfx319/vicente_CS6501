# -*- coding: utf-8 -*-
"""
python3
@author: jcx9dy
"""
import sys
import os
import numpy as np
import cv2
#import matplotlib.pyplot as plt
#import cv2
#from PIL import Image 
#from scipy.ndimage import imread
#from scipy.misc import imsave
#from skimage import io, img_as_bool
#from skimage.transform import resize
#import glob

#http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/
#https://pythonprogramming.net/loading-images-python-opencv-tutorial/
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html#read-image
#http://pro.arcgis.com/en/pro-app/tool-reference/data-management/minimum-bounding-geometry.htm
#http://docs.opencv.org/3.1.0/dd/d49/tutorial_py_contour_features.html
#http://docs.opencv.org/
#http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html
#


def genCrops(png, mask):
    #for now, instead of getting subcrops, i'm just going to get one bounding circle
    croplist = []
    
    #get bounding circle
    _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #cv2 tends to write in place; so mask will now be only a border
    cnt = contours[0]
    (x,y), radius = cv2.minEnclosingCircle(cnt)
    x = int(x)
    y = int(y)
    radius = int(np.ceil(radius))
    
    #generate a margin (since some bounding circles will be outside image)
    pad_width = int(np.ceil(4*radius))
    png_pad = np.pad(png, pad_width, 'constant', constant_values=0)
    
    # new circle mask
    newmask = np.zeros(png_pad.shape, np.uint8)
    newmask = cv2.circle(newmask, (int(x+pad_width), int(y+pad_width)), int(1.5*radius), 255, -1).astype('bool')
    
    #black out region outside circle mask
    png_pad[~newmask] = 0
    
    #crop square patch of circle region
    x1 = int(x + pad_width - 1.5*radius)
    x2 = int(x + pad_width + 1.5*radius + 1)
    y1 = int(y + pad_width - 1.5*radius)
    y2 = int(y + pad_width + 1.5*radius + 1)
    crop = png_pad[y1:y2, x1:x2]
    
    croplist.append({'row': y, 'col': x, 'radius': radius, 'crop': crop})        
   
    return croplist


############################################################
##########  MAIN

#Given a .npy file path (these were generated by generate_DDSMmasks.py)
   # assumes this format:   '.../cancer_01/case3013/masks/B_3013_1.RIGHT_CC.groundtruth.npy'
   # assumes mammogram in:  '.../cancer_01/case3013/PNGFiles/B_3013_1.RIGHT_CC.png'
   # assumes mask in:       '.../cancer_01/case3013/masks/B_3013_1.RIGHT_CC_\{BENIGN,MALIGNANT\}\{0-9\}.mask.png'

#RUN AS FOLLOWS:   python3 generate_DDSMcrops.py ./cancer_01/case3013/masks/B_3013_1.RIGHT_CC.groundtruth.npy
  # or parallelize:   parallel --eta -a npyfiles.txt python3 generate_DDSMcrops.py {}
  # ~ for just crops on 8-core


npypath = sys.argv[1]  #'./cancer_01/case3013/masks/B_3013_1.RIGHT_CC.groundtruth.npy'
#print('Processing:  ' + npypath)
basepath, npyfile = os.path.split(npypath)
imagename = os.path.splitext(os.path.splitext(npyfile)[0])[0]
casename = npypath.split('/')[-3]
volumename = npypath.split('/')[-4]
view = imagename.split('.')[1]


cropdir_benign = os.path.split(basepath)[0] + '/crop/benign'
cropdir_malign = os.path.split(basepath)[0] + '/crop/malignant'
os.makedirs(cropdir_benign, exist_ok=True)
os.makedirs(cropdir_malign, exist_ok=True)


#load data 
groundtruth = np.load(npypath).item()
mamm = cv2.imread(os.path.split(basepath)[0] + '/PNGFiles/' + imagename + '.png', -1)

### generate crops
for i, e in enumerate(groundtruth['BENIGN']):
    prefix = '-'.join([volumename, imagename, 'benign', 'B'+str(e['ASSESSMENT']), 'D'+str(e['DENSITY']), 'A'+str(e['PATIENT_AGE']).zfill(2), 'S'+str(e['SUBTLETY'])])
    suffix = '-'.join(['L_'+e['LESION_TYPE'].replace('-','_'), 'T_'+e['SHAPE'].replace('-','_')+e['TYPE'].replace('-','_'), 'E_'+e['MARGINS'].replace('-','_')+e['DISTRIBUTION'].replace('-','_')])
    mask = cv2.imread(basepath + '/' + imagename + '_BENIGN' + str(i) + '.mask.png', 0)
    croplist = genCrops(mamm, mask)
    for p in croplist:
        cv2.imwrite(cropdir_benign + '/' + prefix + '-a' + str(i) + '-y'+str(p['row']).zfill(4) + '-x'+str(p['col']).zfill(4) + '-r'+str(p['radius']).zfill(4) + '-' + suffix + '.png', p['crop'])
    
for i, e in enumerate(groundtruth['MALIGNANT']):
    prefix = '-'.join([volumename, imagename, 'malign', 'B'+str(e['ASSESSMENT']), 'D'+str(e['DENSITY']), 'A'+str(e['PATIENT_AGE']).zfill(2), 'S'+str(e['SUBTLETY'])])
    suffix = '-'.join(['L_'+e['LESION_TYPE'].replace('-','_'), 'T_'+e['SHAPE'].replace('-','_')+e['TYPE'].replace('-','_'), 'E_'+e['MARGINS'].replace('-','_')+e['DISTRIBUTION'].replace('-','_')])
    mask = cv2.imread(basepath + '/' + imagename + '_MALIGNANT' + str(i) + '.mask.png', 0)
    croplist = genCrops(mamm, mask)
    for p in croplist:
        cv2.imwrite(cropdir_malign + '/' + prefix + '-a' + str(i) + '-y'+str(p['row']).zfill(4) + '-x'+str(p['col']).zfill(4) + '-r'+str(p['radius']).zfill(4) + '-' + suffix + '.png', p['crop'])

#Can later load crops as follows: 
#np.array(PIL.Image.open('crop.png'))
#scipy.ndimage.imread('crop.png')
    #these are 16bit uint values stored in int32 array
    #if converting to float, should maybe divide by 2**16


#os.chdir(outdir+'/input')
#np.save(filename, myimg.reshape((newpixdim*newpixdim)).astype('float32'))
