


# Project Proposal - CS 6501-003: Computational Visual Recognition

Deliver to: 
visionlab.uva+project@gmail.com



## Objective: 

#### A. Re-implementing a previously proposed technique and reproducing the results on an existing dataset.

##### References
http://www.cs.technion.ac.il/~nastyad/publications/DKGHK_DLMIA2015.pdf  
http://cs231n.stanford.edu/reports/vibhua_final_report.pdf  
http://cs.adelaide.edu.au/~carneiro/publications/mass_detection_BIA.pdf  
http://www.nature.com/articles/srep27327 (data not public)  


#### B. Applying/improving existing techniques to a new dataset.
As part of a current ongoing open competition, a dataset of 640,000 de-identified digital mammography images from over 86000 patients, with corresponding clinical variables is available for training. The benefits include large dataset size, free computational resources (model is trained remotely on their server). The downsides are that the data is not publicly viewable and one is unable to access the trained model for inspection/visualization.  
https://www.synapse.org/#!Synapse:syn4224222/wiki/401743  



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


##### B. Segmentation of 2D mammography images



## Proposed Model: 

#### Inputs: 

A screening mammography exam consisting of 2 or more images for each (L/R) breast.

#### Outputs: 

A probability (between 0 and 1) of cancer diagnosis within one year for each (L/R) breast.

#### Scoring:

Training data labels are positive if a gold standard tissue-biopsy confirms cancer diagnosis within 1 year of the mammography image set. 

The training process seeks to minimize the cross-entropy loss of the output prediction layer. 


#### Performance Evaluation

According to the federally-funded Breast Cancer Surveillance Consortium, the overall sensitivity of digital mammography in the U.S. screening population is 84%, and the overall specificity is 91% [[3](http://www.ncbi.nlm.nih.gov/pubmed/26501537)]. This represents the gold standard human (radiologist) performance.




##### *Primary metric*:  Area Under the Receiver Operating Characteristics (AUROC)

The AUROC can be thought of as the average value of sensitivity over all possible values of specificity, and is a measure of how well the algorithm’s continuous score separates actually positive from actually negative breast cancer status.

To obtain an empirical ROC curve, the threshold is varied to cover the entire range of possible ratings, and the TPF is plotted as a function of the FPF. The specific (TPF, FPF) pair at a given decision threshold is termed an operating point [[7](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4108682/)].

When both the reference standard and the diagnostic test results are binary, the sensitivity (or TP fraction, TPF) of the test is defined as the percent correct on the set of actually positive cases, and the specificity is defined as the percent correct on the set of actually negative cases. The FP fraction (FPF) is defined as 1-specificity. TPF and FPF are properties inherent to the diagnostic test, and are independent of disease prevalence, so that the results from a prevalence-enriched test data set are representative of the true TPF and FPF of the test [[7](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4108682/)].


##### *Secondary metric*:  Partial Area Under the Receiver Operating Characteristics (pAUROC) curve

The pAUROC emphasizes a specific region of the ROC. As objective is concerned with reducing the False Positive rate (i.e., increase specificity) without decreasing the True Positive rate (sensitivity) below the current radiology practice (estimated as a sensitivity of 0.82 according to the statistics of the Breast Cancer Surveillance Consortium (Ref 3)), we will use the pAUROC computed as the area under the ROC in the range of sensitivities between 0.8 and 1.
 
![pAUROC](https://www.synapse.org/Portal/filehandle?ownerId=syn4224222&ownerType=ENTITY&xsrfToken=null&fileName=pAUC_se_fig_correct_version2.jpg&preview=false&wikiId=402020)



## Proposed Datasets: 

#### 
#### 
#### 
#### 



## Project Outcome / Deliverable

#### 
#### 

