

# Progress Report - CS 6501-003 Computational Visual Recognition

## Summary: 



## Data Collected: 
Of the initial candidate datasets from the project proposal, I chose to proceed with the Digital Database for Screening Mammography (DDSM), a collaborative effort between Massachusetts General Hospital, Sandia National Laboratories, and the University of South Florida Computer Science and Engineering Department. This is the largest public dataset I could find. The data is a mixture of normal, benign, and cancer volumes selected and digitized specifically for DDSM.

#### Cancer Example {Volume: cancer_01, Case: B-3013-1}:
![](http://marathon.csee.usf.edu/Mammography/DDSM/thumbnails/cancers/cancer_01/case3013/B_3013_1.RIGHT_MLO.LJPEG.1_highpass.gif)

#### Example annotation:
FILE: B_3013_1.RIGHT_MLO.OVERLAY  
TOTAL_ABNORMALITIES 2  
ABNORMALITY 1  
**LESION_TYPE MASS SHAPE IRREGULAR-ARCHITECTURAL_DISTORTION MARGINS SPICULATED**
ASSESSMENT 5  
SUBTLETY 5  
**PATHOLOGY MALIGNANT**  
TOTAL_OUTLINES 1  
BOUNDARY  
ABNORMALITY 2  
**LESION_TYPE MASS SHAPE IRREGULAR-ARCHITECTURAL_DISTORTION MARGINS SPICULATED**  
ASSESSMENT 5  
SUBTLETY 5  
**PATHOLOGY MALIGNANT**  
TOTAL_OUTLINES 1  
BOUNDARY  




http://marathon.csee.usf.edu/Mammography/DDSM/thumbnails/normals/normal_01/case0152/A_0152_1.RIGHT_CC.LJPEG.1_highpass.gif





## Implemented Modules: 3-4 paragraphs for each module implemented

## Preliminary results 1-3 paragraphs + figure + output results

## Pending work (clear direction): 1 paragraph


## Remaining Challenges (unclear direction)

I haven't fully figured out is how to normalize the data because they aren't all collected with identical equipment. For example there are at least three types of imagers: DBA, HOWTEK, and LUMISYS scanners representing 16bit/42microns, 12bit/43.5microns, 12bit/50microns, respectively. I wouldn't want there to be an artifact in the data for the algorithm to learn on. 

There are many annotations that, time permitting, may require flagging images for removal or special handling. As an example, one image has warning: "The LEFT_CC image has a scanner artifact in it. The rollers slipped while the image was scanning. That is why the letters look distorted."



