# preprocessing images from DDSM

In theory, software is provided with the dataset. However, these are c code compiled on either SunOS 4.1.4 (Solaris 1.1.2) or on SunOS 5.5 (Solaris 2.5). I would rather not install these (and I couldn't find a docker or virtualbox image with limited searching). 

The alternative, is looking around for someone else's implementation of DDSM conversion, since this is a very old dataset and there have been papers published. Google "ddsm github"

Options:
 - Actually used this one with cygwin + matlab:  https://github.com/trane293/DDSMUtility
   - but can also use linux equivalent functions (as noted below); would need to write ics parser from scratch, hence the lazy option of just going with 4 simultaneous instances of matlab (~2 days)
 - https://github.com/multinormal/ddsm
   - used the `get_ddsm_groundtruth.m` from this repo for generating masks
 - https://github.com/trane293/DDSM-Software-Chris-Rose/tree/master/DDSM-Software
 - https://github.com/wakahiu/ddsm-converter
 - http://stackoverflow.com/questions/13365587/getting-data-from-digital-database-for-screening-mammography-ddsm

### PGM 
Can probably ignore these. Haven't really figured out image details. ImageJ can open it, but there seems to be endian-related byte-size artifact (I recall this from peter's hw)?
 - 16bit signed or unsigned?
 - little-endian or big-endian?


### LJPEG
At exactly 4 of these (representing each breast, and each view) per case.  

In retrospect, the ftp sync missed 3 files which can be addressed as follows:  
```bash
ls -1 figment.csee.usf.edu/pub/DDSM/cases/done/*/case*/PNGFiles/*.LJPEG | wc-l
ls -1 figment.csee.usf.edu/pub/DDSM/cases/done/*/case*/PNGFiles/*.png | wc-l
# 10405 pictures, should be 10408 = 2602 cases (website claims "2620 cases available in 43 volumes" --> typo?)

cd figment.csee.usf.edu/pub/DDSM/cases/
for dir in `/usr/bin/find.exe ./done -mindepth 3 -type d`; do
  if [ `ls -1 ${dir} | wc -l` -ne "4" ]; then
    echo ${dir}
  fi
done | tee weird_pngfolders.txt


### some ljpeg /overlay were .gz'd
#benign_01\case3102
for gzfile in `ls -1 ./set1/*/case*/*.gz`; do
  gunzip $gzfile
done

#benign_10\case4164
#missing one ljpeg file, manually retrieve from:  
wget ftp://figment.csee.usf.edu/pub/DDSM/cases/benigns/benign_10/case4164/D_4164_1.LEFT_MLO.LJPEG

#cancer_09\case3407
#missing one ljpeg file, manually retrieve from:  
wget ftp://figment.csee.usf.edu/pub/DDSM/cases/cancers/cancer_09/case3407/B_3407_1.RIGHT_CC.LJPEG
```



Data descriptor is here:  http://marathon.csee.usf.edu/Mammography/DDSM/case_description.html#ALLFILES

Convert to PNG
```bash
#this executable only has ".exe" so that windows users recognize it as such (nonetheless, is a linux binary, so cygwin/bash needed)
./jpeg.exe -d -s C_0029_1.LEFT_CC.LJPEG
#creates a ".1" RAW format file "C_0029_1.LEFT_CC.LJPEG.1"

#convert .1 RAW format to PGM format, normalizing with scanner tech
./ddsmraw2pnm.exe C_0029_1.LEFT_CC.LJPEG.1 4648 2672 lumisys
  #output:  "C_0029_1.LEFT_CC.LJPEG.1-ddsmraw2pnm.pnm"
  
grep 'DIGITIZER' | awk '{print $2}'
#DBA scanner at MGH   ('A' and DBA)
#HOWTEK scanner at MGH   ('A' and HOWTEK)
#LUMISYS scanner at Wake Forest University   ('B' or 'C' and LUMISYS)
#HOWTEK scanner at ISMD   ('D' and HOWTEK)

#executable options:
 #'howtek-mgh'
 #'howtek-ismd'
 #'lumisys'
 #'dba'

#Example ICS line specifying image dimensions:
grep 'FILENAME LINES' | awk '{print $2 " " $5}'
 #LEFT_CC LINES 4648 PIXELS_PER_LINE 2672 



#from cygwin or linux: imagemagick 
/usr/bin/convert.exe C_0029_1.LEFT_CC.LJPEG.1-ddsmraw2pnm.pnm PNGFiles/C_0029_1.LEFT_CC.png

### DELETE INTERMEDIATES
rm C_0029_1.LEFT_CC.LJPEG.1
rm C_0029_1.LEFT_CC.LJPEG.1-ddsmraw2pnm.pnm


#http://stackoverflow.com/questions/27934784/shell-script-to-loop-and-start-processes-in-parallel
```


### ICS

Contains the clinical info and metadata


### PATCHES

method 1:  http://cs231n.stanford.edu/reports/vibhua_final_report.pdf  
method 2:  http://cs231n.stanford.edu/reports2016/306_Report.pdf  

How to generate patches? If we compute min/max pixel ranges of the border or mask (or is it also possible from chaincode?), then can draw a bounding box at those pixels. 

Given these:  
Chaincode

Border/outline

Mask (filled)


Random Rotate, or just the typical 90deg

random crop (after short side is resized to sufficient dimension) 

Resize to 64x64 or 224x224, or 256x256, etc

with 50,000 of 224x224 images, that's 10GB of raw byte size. 

Alternative: if training on sufficiently small patches, is there a need to rescale the mass/tumor? what if random cropping from the mass already gives enough variety?


### OVERLAY

Not all folders will have Overlay files

The [matlab code](https://github.com/trane293/DDSMUtility/blob/master/readBoundary.m) uses image size info from ICS, and the chain code to construct a binary boundary image of the same size, then 'imfill' holes to get the core. It is advisable to do this during runtime, rather than storing the entire binary image (which can be large, unless one forces the values to be raw 1bit values). 

I'd want to have a python implementation:  
https://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.ndimage.morphology.binary_fill_holes.html


Another [matlab repo](https://github.com/multinormal/ddsm/blob/master/ddsm-software/get_ddsm_groundtruth.m)
```matlab
overlays = get_ddsm_groundtruth('cancer_10\case1580\A_1580_1.LEFT_MLO.OVERLAY')
% overlays = 
%    [1x1 struct]    [1x1 struct]

length(overlays)
% ans =
%     2

overlays{1}
% ans = 
%    lesion_type: {'MASS SHAPE IRREGULAR MARGINS ILL_DEFINED'}
%     assessment: 4
%       subtlety: 3
%      pathology: 'MALIGNANT'
%    annotations: [1x1 struct]

overlays{2}
% ans = 
%    lesion_type: {'CALCIFICATION TYPE PLEOMORPHIC DISTRIBUTION CLUSTERED'}
%     assessment: 4
%       subtlety: 2
%      pathology: 'MALIGNANT'
%    annotations: [1x1 struct]

overlays{1}.annotations
% ans = 
%    boundary: @(image_dims)make_annotation_image(image_dims,bc_text{i})
%       cores: {[@(image_dims)make_annotation_image(image_dims,bc_text{i})]}

length(overlays{1}.annotations.cores)
% ans =
%     1

%%% It's kinda dumb that the author didn't put image dimensions already in the groundtruth matlab structure; have to manually get it
boundary_annotation = overlays{1}.annotations.boundary([4606 2221]);
imagesc(boundary_annotation)

%%% this seems to give an identical picture to the boundary?? 
imagesc(overlays{1}.annotations.cores{1}([4606 2221]))

```

Current remote access: 
```
ssh jcx9dy@128.143.129.160:/media/jcx9dy/SG4/figment.csee.usf.edu/pub/DDSM/cases/done

```

