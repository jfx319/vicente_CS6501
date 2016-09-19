


# Project Proposal - CS 6501-003: Computational Visual Recognition

Deliver to: 
visionlab.uva+project@gmail.com



### Objective: 

##### A. Re-implementing a previously proposed technique and reproducing the results on an existing dataset.

###### References
http://www.cs.technion.ac.il/~nastyad/publications/DKGHK_DLMIA2015.pdf  
http://cs231n.stanford.edu/reports/vibhua_final_report.pdf  
http://cs.adelaide.edu.au/~carneiro/publications/mass_detection_BIA.pdf  
http://www.nature.com/articles/srep27327 (data not public)  


##### B. Applying/improving existing techniques to a new dataset.
As part of a current ongoing open competition, a dataset of 640,000 de-identified digital mammography images from over 86000 patients, with corresponding clinical variables is available for training. The benefits include large dataset size, free computational resources (model is trained remotely on their server). The downsides are that the data is not publicly viewable and one is unable to access the trained model for inspection/visualization.  
https://www.synapse.org/#!Synapse:syn4224222/wiki/401743  



### Problem Statement: 

#### Impact / Motivation: 
Breast cancer is the most frequently diagnosed solid cancer and second leading cause of cancer death among U.S. women [1](http://www.cancer.org/cancer/breastcancer/detailedguide/breast-cancer-key-statistics). Despite the usefulness of screening mammography, routine mammography is associated with a high risk of false positive testing and may lead to overdiagnosis of clinically insignificant lesions [2](http://www.ncbi.nlm.nih.gov/pubmed/26501536). 

The recall rate (the number of women who require additional testing after a screening) associated with mammography remains high (approximately 100/1000); yet, the proportion of women recalled who are eventually found to have breast cancer is quite low (5/1000) [3](http://www.ncbi.nlm.nih.gov/pubmed/26501537). 

These false positives lead to increased anxiety and potential morbidity associated with unnecessary downstream diagnostic workup (healthcare expenditure, invasive biopsy, etc). False-positive recalls from mammography represent the tipping point for screening recommendations, with the U.S. Preventive Services Task Force recommending less frequent mammography screening due to these potential risks.

The proposed task is to use Deep Learning image recognition to improve radiologist's interpretive accuracy and reduce the overall recall rate without increasing the number of false negative exams.

In order to improve radiologists’ interpretive accuracy, multiple vendors have developed computer-assisted detection (CAD) software to help radiologists identify subtle suspicious masses and calcifications. The ultimate goal of computer-assisted detection is to increase the radiologist’s accuracy for detecting cancer and, thus, lead to improved patient outcomes. Unfortunately, Computer-assisted detection to date, developed on test case sets with little potential for dynamic improvement over time, has led to no significant improvement in any performance metric, including sensitivity, specificity, positive predictive value, recall rate and benign biopsy rate [5](http://www.ncbi.nlm.nih.gov/pubmed/17409321)[6](http://www.ncbi.nlm.nih.gov/pubmed/26414882).

According to the federally-funded Breast Cancer Surveillance Consortium, the overall sensitivity of digital mammography in the U.S. screening population is 84%, and the overall specificity is 91% [3](http://www.ncbi.nlm.nih.gov/pubmed/26501537). This represents the gold standard human (radiologist) performance.


Breast cancer is As part of routine screening, each patient may 

##### A. Classification of 2D mammography images


##### B. Segmentation of 2D mammography images



### Proposed Model: 

##### Inputs: 

##### Outputs: 

##### Evaluation Metric:



### Proposed Datasets: 

##### 
##### 
##### 
##### 



### Project Outcome / Deliverable

##### 
##### 

