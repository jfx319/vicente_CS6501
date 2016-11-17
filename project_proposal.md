# Project Proposal - CS 6501-003: Computational Visual Recognition

Deliver to: 
visionlab.uva+project@gmail.com

---
## Objective: 
Given that the class project has minimum requirements and encouraged "reach" goals, we list both here since it cannot be guaranteed without having attempted the tasks. The hope is to achieve both. 

At minimum, one of the papers from objective A will be re-implemented.

### A. Re-implementing a previously proposed technique and reproducing the results on an existing dataset

#### Existing Literature Papers

Data Available for reproducing method

 * Automated Mass Detection from Mammograms using Deep Learning and Random Forest  
http://cs.adelaide.edu.au/~carneiro/publications/mass_detection_BIA.pdf  
INbreast dataset comprises a set of 115 cases containing 410 images, where out of 410 images, 116 images contains the benign or malignant masses, whereas the rest does not contain any masses
All images on the DDSM-BCRP dataset contain malignant masses, with 39 cases for training and 40 cases for testing

* Using Deep Convolutional Neural Networks to Predict Semantic Features of Lesions in Mammograms  
http://cs231n.stanford.edu/reports/vibhua_final_report.pdf  
Digital Database for Screening Mammography (DDSM)
2,500 samples, pixel-level ground-truth annotation of suspicious areas
5 convolutional layers, 3 fully-connected layers

* DeepMammo: Breast Mass Classification using Deep Convolutional Neural Networks  
http://cs231n.stanford.edu/reports2016/306_Report.pdf

Data not available, but ideas/methods may be applied to other datasets:

 * Computational Mammography using Deep Neural Networks:  
http://www.cs.technion.ac.il/~nastyad/publications/DKGHK_DLMIA2015.pdf  
http://m.ibm.com/http/research.ibm.com/haifa/dept/imt/mia.shtml  

 * Discrimination of Breast Cancer with Microcalcifications on Mammography by Deep Learning  
http://www.nature.com/articles/srep27327  
Training: 1000 images, including 677 benign and 323 malignant lesions  
Testing: 204 images, including 97 benign and 107 malignant lesions

 * Unsupervised Deep Learning Applied to Breast Density Segmentation and Mammographic Risk Scoring  
http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7412749&tag=1  
Dutch Breast Cancer Screening Dataset  
394 cancers, and 1182 healthy controls  
images were segmented into the breast area, pectoral muscle and background using automated software (Volpara, Matakina Technology Limited, New Zealand)
texture dataset comprises 668 mediolateral mammograms from the Mayo mammography Health Study (MMHS) cohort at the Mayo Clinic in Rochester, Minnesota. The purpose of the MMHS study was to examine the association of breast density with breast cancer [58]. The chosen subset included 226 cases and 442 controls


### B. Applying/improving existing techniques to a new dataset
As part of a current ongoing open competition, a dataset of 640,000 de-identified digital mammography images from over 86000 patients, with corresponding clinical variables is available for training. The benefits include large dataset size, free computational resources (model is trained remotely on their server). The downsides are that the data is not publicly viewable and one is unable to access the trained model for inspection/visualization.  
https://www.synapse.org/#!Synapse:syn4224222/wiki/401743  

Core concepts, strategies, and algorithms from objective A will be applied to objective B.


---
## Problem Statement: 

#### Impact / Motivation: 
Breast cancer is the most frequently diagnosed solid cancer and second leading cause of cancer death among U.S. women [[1](http://www.cancer.org/cancer/breastcancer/detailedguide/breast-cancer-key-statistics)]. Despite the usefulness of screening mammography, routine mammography is associated with a high risk of false positive testing and may lead to overdiagnosis of clinically insignificant lesions [[2](http://www.ncbi.nlm.nih.gov/pubmed/26501536)]. 

The recall rate (the number of women who require additional testing after a screening) associated with mammography remains high (approximately 100/1000); yet, the proportion of women recalled who are eventually found to have breast cancer is quite low (5/1000) [[3](http://www.ncbi.nlm.nih.gov/pubmed/26501537)]. 

These false positives lead to increased anxiety and potential morbidity associated with unnecessary downstream diagnostic workup (healthcare expenditure, invasive biopsy, etc). False-positive recalls from mammography represent the tipping point for screening recommendations, with the U.S. Preventive Services Task Force recommending less frequent mammography screening due to these potential risks.

In order to improve radiologists’ interpretive accuracy, multiple vendors have developed computer-assisted detection (CAD) software to help radiologists identify subtle suspicious masses and calcifications. The ultimate goal of computer-assisted detection is to increase the radiologist’s accuracy for detecting cancer and, thus, lead to improved patient outcomes. Unfortunately, Computer-assisted detection to date, developed on test case sets with little potential for dynamic improvement over time, has led to no significant improvement in any performance metric, including sensitivity, specificity, positive predictive value, recall rate and benign biopsy rate [[5](http://www.ncbi.nlm.nih.gov/pubmed/17409321)][[6](http://www.ncbi.nlm.nih.gov/pubmed/26414882)].

#### The proposed task:  
Use deep Learning image recognition in the form of convolutional neural networks (CNN) to 
  * improve radiologist's interpretive accuracy 
  * reduce the overall recall rate without increasing the number of false negative exams

##### A. Classification of 2D mammography images
Given mammography images, classify each image into labeled categories (e.g. benign or tumor). 

##### B. (Optional) Segmentation of 2D mammography images
Given mammography images, classify each pixel into labeled categories (e.g. background, calcification, bone, lesion/tumor). 

Additional evaluation metrics will be imposed for segmentation: 
 * Dice coefficient [Dubrovina1 et al](http://www.cs.technion.ac.il/~nastyad/publications/DKGHK_DLMIA2015.pdf)
 * Intersection over Union (IU) [Long et al](https://people.eecs.berkeley.edu/~jonlong/long_shelhamer_fcn.pdf)


---
## Proposed Model: 

The model architecture is still being evaluated and may vary depending on the objective (replicating existing approach, or implementing a new one). It will likely consist of layered CNN for learning high-level image features as well as a SVM or FC layer(s) for final classification. For the separate task of image segmentation, an inverted architecture will be explored after the CNN (e.g. a deconvolutinal net or similar).

#### Inputs: 

A screening mammography exam consisting of 2 or more images for each (L/R) breast. These are single-channel black/white images.

#### Outputs: 

A probability (between 0 and 1) of cancer diagnosis within one year for each (L/R) breast.

#### Scoring:

Training data labels are positive if a gold standard tissue-biopsy confirms cancer diagnosis within 1 year of the mammography image set. 

The training process seeks to minimize the cross-entropy loss of the output prediction layer. 


#### Performance Evaluation

According to the federally-funded Breast Cancer Surveillance Consortium, the overall sensitivity of digital mammography in the U.S. screening population is 84%, and the overall specificity is 91% [[3](http://www.ncbi.nlm.nih.gov/pubmed/26501537)]. This represents the gold standard human (radiologist) performance.

A rough initial comparison can be made with accuracy and specificity on standardized held-out testing data (for each dataset). 

##### *Primary metric*:  Area Under the Receiver Operating Characteristics (AUROC)

The AUROC can be thought of as the average value of sensitivity over all possible values of specificity, and is a measure of how well the algorithm’s continuous score separates actually positive from actually negative breast cancer status.

To obtain an empirical ROC curve, the threshold is varied to cover the entire range of possible ratings, and the TPF is plotted as a function of the FPF. The specific (TPF, FPF) pair at a given decision threshold is termed an operating point [[7](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4108682/)].

When both the reference standard and the diagnostic test results are binary, the sensitivity (or TP fraction, TPF) of the test is defined as the percent correct on the set of actually positive cases, and the specificity is defined as the percent correct on the set of actually negative cases. The FP fraction (FPF) is defined as 1-specificity. TPF and FPF are properties inherent to the diagnostic test, and are independent of disease prevalence, so that the results from a prevalence-enriched test data set are representative of the true TPF and FPF of the test [[7](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4108682/)].


##### *Secondary metric*:  Partial Area Under the Receiver Operating Characteristics (pAUROC) curve

The pAUROC emphasizes a specific region of the ROC. As objective is concerned with reducing the False Positive rate (i.e., increase specificity) without decreasing the True Positive rate (sensitivity) below the current radiology practice (estimated as a sensitivity of 0.82 according to the statistics of the Breast Cancer Surveillance Consortium (Ref 3)), we will use the pAUROC computed as the area under the ROC in the range of sensitivities between 0.8 and 1.
 
![pAUROC](https://www.synapse.org/Portal/filehandle?ownerId=syn4224222&ownerType=ENTITY&xsrfToken=null&fileName=pAUC_se_fig_correct_version2.jpg&preview=false&wikiId=402020)


---
## Proposed Datasets: 

#### mini-MIAS
The Mammographic Image Analysis Society (MIAS) is an organisation of UK research groups interested in the understanding of mammograms and has generated a database of digital mammograms. Films taken from the UK National Breast Screening Programme have been digitised to 50 micron pixel edge with a Joyce-Loebl scanning microdensitometer, a device linear in the optical density range 0-3.2 and representing each pixel with an 8-bit word. The database contains 322 digitised films and is available on 2.3GB 8mm (ExaByte) tape. It also includes radiologist's "truth"-markings on the locations of any abnormalities that may be present. The database has been reduced to a 200 micron pixel edge and padded/clipped so that all the images are 1024x1024. Mammographic images are available via the Pilot European Image Processing Archive (PEIPA) at the University of Essex.  http://peipa.essex.ac.uk/info/mias.html

The database contains left and right breast images for 161 patients, and is available on a DAT-DDS tape. Its quantity consists of 322 images, which belong to three types: 208 normal, 63 benign and 51 malignant (abnormal) images. It also includes radiologist's `truth'-markings on the locations of any abnormalities that may be present. For each film, experienced radiologists give the type, location, scale, and other useful information of them. According to these experts’ descriptions, the database is conclude of four kinds of abnormities (architectural distortions, stellate lesions, circumscribed mass and calcifications). The database possesses an introduction file, which included following information:  
* type: which kinds mentioned above the abnormities belong to. 
* sort: whether the abnormities are cancer or benign ones.
* location and size: the original coordinates and diameters of the abnormities.  

##### Agreement between Radiologists on MIAS
http://eia.udg.es/~aoliver/publications/tesi/node64.html  

data from a random sample of 20,000 digital and 20,000 film-screen mammograms received by women age 60-89 years within the BCSC between January 2005 and December 2008.




#### BCSC
http://www.bcsc-research.org/data/mammography_dataset/



#### DDSM
The Digital Database for Screening Mammography (DDSM) is another resource for possible use by the mammographic image analysis research community. It is a collaborative effort between Massachusetts General Hospital, Sandia National Laboratories and the University of South Florida Computer Science and Engineering Department. The database contains approximately 2,500 studies. Each study includes two images of each breast, along with some associated patient information (age at time of study, ACR breast density rating, subtlety rating for abnormalities, ACR keyword description of abnormalities) and image information (scanner, spatial resolution, ...). Images containing suspicious areas have associated pixel-level "ground truth" information about the locations and types of suspicious regions. Also provided are software both for accessing the mammogram and truth images and for calculating performance figures for automated image analysis algorithms.  
In total, 2620 cases (695 normal,  870 benign, 914 cancer, 141 benign with callback), collectively totalling 8752 images with pixel masks overlay files. Heterogeneous files, 16bit or 12bit compressed lossless jpeg, 42 or 43.5 or 50 microns)  
http://see.xidian.edu.cn/vipsl/database_Mammo.html  
Data page:  
http://marathon.csee.usf.edu/Mammography/Database.html
* really look at notes, e.g. "The rollers slipped while the image was scanning. That is why the letters look distorted. "

#### DDSM BCRP (pixel level ground truth)
http://marathon.csee.usf.edu/Mammography/DDSM/BCRP/bcrp.html


#### INBREAST
FFDM, completely digital to begin with. 115 cases (410 images). 90 cases are from bilateral involvement, 25 cases are from mastectomy patients. Contours by specialists provided in XML format. Several types of lesions (masses, calcifications, asymmetries, and distortions) were included.  
calcifications are present in 301 of the 410 images. The tag “cluster” was only used in 27 sets of calcifications, in 21 images (≈1.3 clusters per image). Of these 21 images, only 2 had no single calcifications annotation. A total of 6880 calcifications were thus individually identified in 299 images (≈23.0 calcifications per image).




---
## Project Outcome / Deliverable

Regardless of whether this project achieves both objectives (replicating past study, or implementing/applying to new dataset), the following will be the presented: 

 * Compare evaluation metrics & performance to that of the study. 
 * Visualization of learned features/filters at various layers
 * If segmentation task is attempted:  visualizing predicted segmentation regions. 
