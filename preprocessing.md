# preprocessing images from DDSM

In theory, software is provided with the dataset. However, these are c code compiled on either SunOS 4.1.4 (Solaris 1.1.2) or on SunOS 5.5 (Solaris 2.5). I would rather not install these (and I couldn't find a docker or virtualbox image with limited searching). 

The alternative, is looking around for someone else's implementation of DDSM conversion, since this is a very old dataset and there have been papers published. Google "ddsm github"

Options:
 - https://github.com/trane293/DDSMUtility
 - https://github.com/multinormal/ddsm
 - https://github.com/trane293/DDSM-Software-Chris-Rose/tree/master/DDSM-Software
 - https://github.com/wakahiu/ddsm-converter
 - http://stackoverflow.com/questions/13365587/getting-data-from-digital-database-for-screening-mammography-ddsm
 
 

### PGM 
Can probably ignore these. Haven't really figured out image details. ImageJ can open it, but there seems to be endian-related byte-size artifact (I recall this from peter's hw)?
 - 16bit signed or unsigned?
 - little-endian or big-endian?


### LJPEG
At least 4 of these (representing each breast, and each view) per case. Some cases have more?

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

```


### ICS

Contains the clinical info and metadata


### OVERLAY

Not all folders will have Overlay files

The [matlab code](https://github.com/trane293/DDSMUtility/blob/master/readBoundary.m) uses image size info from ICS, and the chain code to construct a binary boundary image of the same size, then 'imfill' holes to get the core. It is advisable to do this during runtime, rather than storing the entire binary image (which can be large, unless one forces the values to be raw 1bit values). 

I'd want to have a python implementation:  
https://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.ndimage.morphology.binary_fill_holes.html








