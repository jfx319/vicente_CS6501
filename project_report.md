
## Project Report - CS6501-003 - CNN for Mammography: distinguishing benign vs. malignant masses
Jeffrey Xing

### Abstract

This project's inspiration comes from Vibhu Agarwal's and Clayton Carson's paper "Using Deep Convolutional Neural Networks to Predict Semantic Features of Lesions in Mammograms" [1] as well as Arzav Jain's and Daniel Levy's paper "DeepMammo: Breast Mass Classification using Deep Convolutional Neural Networks" [2]. 
We attempt to reproduce and build on their prior work classifying 2D-mammography X-ray images of lesions into malignant or benign by employing a convolutional neural network (CNN) architecture. 
We implement and test two architectures at varying depths, ultimately achieving the best performance with a fine-tuned InceptionV3 model (83% accuracy, 64% sensitivity, 13% false positive rate), which is on par with the lower quartile of human FPR. 


### Introduction

Breast cancer is the number one leading cancer among females, and the second most fatal type in the same group [3].
2D Xray screening mammograms are currently considered to be the best method for early detection of breast cancer, although 3D tomosynthesis is becoming more popular (this is equivalent to a mammogram taken at multiple angles and synthetically reconstructed into a 3D stack). 
The interpretation and diagnosis by radiologists is still a manual and laborous process with high variance depending on the interpreter [4]. 
Methods for standardizing and improving diagnosis are still being explored. 
This paper examines previous approaches using convolutional neural network architecture to reduce feature-engineering and automatically learn a model from labeled data. 

#### Dataset

The dataset used is one of the largest publicly available radiographic imaging databases: Digital Database for Screening Mammography (DDSM) [5]. 
The full database contains roughly 2620 cases (patients), curated to contain well-balanced class distribution: (695 normal, 870 benign, 914 cancer, 141 benign with callback). 
The advantage of this dataset is that for regions of interest in each high-resolution (16bit, ~4000 x ~2000) image, there are a) expert radiologist annotated boundary shapes, b) clinically relevant physician's interpretation of the shape, and most importantly c) biopsy/pathology validated ground-truth status of the lesion. 
For this project, we only consider single contiguous masses (not calcifications, which tend to be star-like clusters of punctate dots) to stratify the problem into a more defined sub-challenge. 
To generalize better, we split our data by patient (instead of by image) into 80% train and 20% validation. 
The final distribution after selecting masses is shown in Table 1.
Although not huge when comparing with other machine learning image datasets, it is one of the largest available datasets in the medical imaging field; thus, it is hoped that these are sufficient to yield promising proof-of-concept results.

##### Table 1a. Number of patient cases in masses subset.
| |Benign | Malignant | Both | **Total**
|---|---|---|---|---|---
| Patients | 515 | 581 | 21 | 1117

##### Table 1b. Number of individual masses in training/validation split.
| | Benign | Malignant | **Total**
|---|---|---|---|
| Train | 903 | 978 | 1881
| Validation | 238 | 243 | 481

##### Sample Images
Left: Cancer {Volume: cancer_01, Case: B-3013-1},   Right: Normal {Volume: normal_01, Case: A-0002-1}:  
![](http://marathon.csee.usf.edu/Mammography/DDSM/thumbnails/cancers/cancer_01/case3013/B_3013_1.RIGHT_MLO.LJPEG.1_highpass.gif) __________ ![](http://marathon.csee.usf.edu/Mammography/DDSM/thumbnails/normals/normal_01/case0002/A_0002_1.RIGHT_MLO.LJPEG.1_highpass.gif) 




#### Preprocessing
As the raw images are in an obscure, old format (data is from 1990s), a preprocessing utility [6] was used to convert them to PNM intermediate format, whereupon an imagemagick wrapper [7] is used to convert to standard PNG. This utility [6] also claims to normalize batch effects due to different scanners/institutions used during data collection. 



#### Model architecture


Both models were implemented in keras [] with tensorflow backend and trained on gpu.




## Implemented Modules: 

##### Pre-processing: Image Decompression
Since the data is rather large, in a compressed and somewhat obscure/unwieldy format, there are many preprocessing steps required to convert the image into a format more suitable for input into the machine learning algorithm. Namely, the first module so far is for uncompressing the images, standardizing all images into 16-bit floating-point, single-channel pixel values and storing that on disk. This expansion requires a larger amount of space. I invested in a separate 4TB harddrive for storage of the raw-format data. Depending on computing needs (i.e. cloud), temporary online storage may be needed. I will be looking into setting up cloud storage very soon so that data ingress can proceed as model pipeline development continues. Following the baseline algorithm used by the paper, 64x64 pixel patch-wise training will be used (I am considering using a resized version of the large images as another way of computationally making this more feasible).

##### Pre-processing: Category parsing
The various classification tasks require image categories to be parsed from the metadata files: tumor vs malignant, mass vs calcification, BIRADS score (1-5), mass annotation (e.g. "spiculated"). Although the baseline task is simply binary classification: benign vs malignant; it is easy to code up extracting these other categories so that they may be later used for additional tasks. 

##### Pre-processing: Ground-truth Mask Reconstruction
Because the overlay files specify tumor locations as a boundary file, these boundaries must be converted into a filled-in boolean mask so that internal pixels of the tumor can also be later referenced. This tumor pixel-wise segmentation task will be an extra task beyond the baseline classification task. 

##### Neural Network architecture
The model architecture is based on the original paper with 5 convolutional layers and is implemented in keras + tensorflow with ReLU activations, max pooling, batch normalization and dropout. An additional softmax layer is used for final categorical classification, which in the case of two classes will be equivalent to a logistic regression. 

##### Evaluation
For baseline classification, it is fairly straightforward to evaluate the confusion table and compute simple statistics like accuracy, etc. For the additional tasks such as for pixel-wise segmentation, other measures such as AuROC (area under the receiver-operating curve) will be implemented. 

The dataset comes with a target ROC performance result using previously published algorithm: 
![](http://marathon.csee.usf.edu/Mammography/DDSM/BCRP/FROC_AFUM.gif)


### Future work

visualization of saliency


I haven't fully figured out is how to normalize the data because they aren't all collected with identical equipment. For example there are at least three types of imagers: DBA, HOWTEK, and LUMISYS scanners representing 16bit/42microns, 12bit/43.5microns, 12bit/50microns, respectively. I wouldn't want there to be an artifact in the data for the algorithm to learn on (or "cheat"). 

There are many annotations that, time permitting, may require flagging images for removal or special handling. As an example, one image warns: "The LEFT_CC image has a scanner artifact in it. The rollers slipped while the image was scanning. That is why the letters look distorted." Such is the tradeoff when working with real-world data. 



### References

[1] http://cs231n.stanford.edu/reports/vibhua_final_report.pdf

[2] http://cs231n.stanford.edu/reports2016/306_Report.pdf

[3] https://www.ncbi.nlm.nih.gov/pubmed/18003123

[4] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2786197/

[5] http://marathon.csee.usf.edu/Mammography/Database.html

[6] https://github.com/multinormal

[7] https://github.com/trane293/DDSMUtility




https://github.com/fchollet/keras
https://github.com/tensorflow/tensorflow
https://github.com/tensorflow/models/tree/master/inception




