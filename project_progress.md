

# Progress Report - CS 6501-003 Computational Visual Recognition

## Summary: 

This project's baseline aim is to replicate Vibhu Agarwal's and Clayton Carson's paper "Using Deep Convolutional Neural Networks to Predict Semantic Features of Lesions in Mammograms". Time permitting, additional tasks and/or datasets may also be explored and compared. The baseline task is classifying mammography X-ray images into malignant or benign by employing a neural network with 5 convolutional layers to learn deep image features. In total, the dataset consists of 2620 cases (695 normal, 870 benign, 914 cancer, 141 benign with callback), collectively totalling 8752 images with pixel masks overlay files. Although not huge when comparing with other machine learning image datasets, it is one of the largest available datasets in the medical imaging field; thus, it is hoped that these are sufficient to yield promising proof-of-concept results.

Current status:  Data has been acquired and mostly preprocessed (some advanced normalization steps and manual curation are still being thought out). Model is being coded up in keras+tensorflow and initial testing will begin shortly. In parallel, due to the anticipated size/complexity of training, additional compute resources are being explored such as the economic feasibility of cloud gpu instances. Working as a team of only one, there is more efficiency in decision making, but slower throughput in terms of implementation. 


## Data Collected: 
Of the initial candidate datasets from the project proposal, I chose to proceed with the Digital Database for Screening Mammography (DDSM), a collaborative effort between Massachusetts General Hospital, Sandia National Laboratories, and the University of South Florida Computer Science and Engineering Department. This is the largest public dataset I could find. The data is a mixture of normal, benign, and cancer volumes selected and digitized specifically for DDSM.

#### Data statistics

Each of the 2,620 cases contains at least four 25MB images in lossless jpeg (.LJPEG) format. 

The meta-information about the case is contained in a separate (.ICS) text file which contains image technical details (relevant for normalization) and additional useful diagnostic "features" such as ACR breast tissue density rating of 1 to 4 as assessed by an expert radiologist (note: tissue density is known to affect diagnostic interpretability).

#### Sample Images

Left: Normal {Volume: normal_01, Case: A-0002-1},   Right: Cancer {Volume: cancer_01, Case: B-3013-1}
![](http://marathon.csee.usf.edu/Mammography/DDSM/thumbnails/normals/normal_01/case0002/A_0002_1.RIGHT_MLO.LJPEG.1_highpass.gif) ![](http://marathon.csee.usf.edu/Mammography/DDSM/thumbnails/cancers/cancer_01/case3013/B_3013_1.RIGHT_MLO.LJPEG.1_highpass.gif)


#### Example overlay annotation:
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
```
BOUNDARY
1752 1536 4 4 4 4 4 4 4 4 5 4 5 4 5 4 5 4 5 4 5 4 5 4 5 4 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 5 6 5 6 5 6 5 6 5 6 5 6 5 6 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 4 4 4 4 4 4 4 4 6 6 6 6 6 6 6 6 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 5 6 6 5 6 6 5 6 6 5 6 6 5 6 6 5 6 6 5 6 6 5 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 5 6 5 6 5 6 5 6 5 6 5 6 5 6 5 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 5 6 5 6 5 6 5 6 5 6 5 6 5 6 5 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 4 4 4 4 4 4 4 4 6 6 6 6 6 6 6 6 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 4 4 4 4 4 4 4 4 5 4 5 4 5 4 5 4 5 4 5 4 5 4 5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 6 6 6 6 6 6 6 6 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 2 2 2 2 2 2 2 0 0 0 0 0 0 0 0 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 0 0 0 0 0 0 0 0 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 2 2 2 2 2 2 2 2 0 0 0 0 0 0 0 0 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 2 2 2 2 2 2 2 2 0 0 0 0 0 0 0 0 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 0 0 0 0 0 0 0 0 2 2 2 2 2 2 2 2 0 0 0 0 0 0 0 0 2 2 2 2 2 2 2 2 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6 6 6 6 6 6 6 6 0 0 0 0 0 0 0 0 6 6 6 6 6 6 6 6 0 0 0 0 0 0 0 0 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 7 7 6 7 7 6 7 7 6 7 7 6 7 7 6 7 7 6 7 7 6 7 7 6 #
```
The numbers represent initial starting pixel (x, y) and 8-connectivity direction of the next neighboring boundary pixel as follows: 
```
7 0 1
6 x 2
5 4 3
```


## Implemented Modules: 3-4 paragraphs for each module implemented

#### Pre-processing modules:

##### Image Decompression
Since the data is rather large, in a compressed and somewhat obscure/unwieldy format, there are many preprocessing steps required to convert the image into a format more suitable for input into the machine learning algorithm. Namely, the first module so far is for uncompressing the images, standardizing all images into 16-bit floating-point, single-channel pixel values and storing that on disk. This expansion requires a larger amount of space. I invested in a separate 4TB harddrive for storage of the raw-format data. Depending on computing needs (i.e. cloud), temporary online storage may be needed. I will be looking into setting up cloud storage very soon so that data ingress can proceed as model pipeline development continues.

##### Category parsing
The various classification tasks require image categories to be parsed from the metadata files: tumor vs malignant, mass vs calcification, BIRADS score (1-5), mass annotation (e.g. "spiculated"). Although the baseline task is simply binary classification: benign vs malignant; it is easy to code up extracting these other categories so that they may be later used for additional tasks. 

##### Ground-truth Mask Reconstruction
Because the overlay files specify tumor locations as a boundary file, these boundaries must be converted into a filled-in boolean mask so that internal pixels of the tumor can also be later referenced. This tumor pixel-wise segmentation task will be an extra task beyond the baseline classification task. 

##### Neural Network architecture
The model architecture is based on the original paper with 5 convolutional layers and is implemented in keras + tensorflow with ReLU activations, max pooling, batch normalization and dropout. An additional softmax layer is used for final categorical classification, which in the case of two classes will be equivalent to a logistic regression. 

##### Evaluation
For baseline classification, it is fairly straightforward to evaluate the confusion table and compute simple statistics like accuracy, etc. For the additional tasks such as for pixel-wise segmentation, other measures such as AuROC (area under the receiver-operating curve) will be implemented. 

The dataset comes with a target ROC performance result using previously published algorithm: 
![](http://marathon.csee.usf.edu/Mammography/DDSM/BCRP/FROC_AFUM.gif)

##### Visualization module: 
Time permitting, I wish to also implement a way of visualizing the learned layers to see what various layers are "seeing" and visualizing which subpatches or regions are contributing to the confidence of each classification. 


## Pending work (clear direction): 
The model code has been demo'd in keras + tensorflow following previous example documentation. Training is very slow without gpu access, so current priority is to obtain gpu testing on UVA's resources such as the CS gpu cluster or HPC. If these are difficult or too busy, I plan on investing in some cloud credits on Amazon. 

## Remaining Challenges (unclear direction):

I haven't fully figured out is how to normalize the data because they aren't all collected with identical equipment. For example there are at least three types of imagers: DBA, HOWTEK, and LUMISYS scanners representing 16bit/42microns, 12bit/43.5microns, 12bit/50microns, respectively. I wouldn't want there to be an artifact in the data for the algorithm to learn on (or "cheat"). 

There are many annotations that, time permitting, may require flagging images for removal or special handling. As an example, one image warns: "The LEFT_CC image has a scanner artifact in it. The rollers slipped while the image was scanning. That is why the letters look distorted." Such is the tradeoff when working with real-world data. 

