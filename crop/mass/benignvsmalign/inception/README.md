

Inception model, trained on amazon p2 instance


Final accuracies:
```
nb_train_samples = 1881
nb_train_class0 = 903         #benign
nb_train_class1 = 978         #malignant

nb_validation_samples = 481
nb_validation_class0 = 238    #benign
nb_validation_class1 = 243    #malignant

Found 1881 images belonging to 2 classes.
Found 481 images belonging to 2 classes.

### Chollet (3CN layers) Shallow:
Evaluating training data... 
['loss', 'acc']
[0.57276701523085771, 0.72669491525423724]
Evaluating validation data... 
['loss', 'acc']
[0.58316284418106079, 0.734375]

Inception V3: 
Evaluating training data... 
['loss', 'acc']
[0.24688780913918706, 0.89247881355932202]
Evaluating validation data... 
['loss', 'acc']
[0.43673722445964813, 0.828125]
```


### Stratify by other variables

Subtlety
```bash
ls -1 validate/benign/*-S5-*.png | wc -l
ls -1 validate/malignant/*-S5-*.png | wc -l

ls -1 validate/benign/*-S4-*.png | wc -l
ls -1 validate/malignant/*-S4-*.png | wc -l

ls -1 validate/benign/*-S3-*.png | wc -l
ls -1 validate/malignant/*-S3-*.png | wc -l

ls -1 validate/benign/*-S2-*.png | wc -l
ls -1 validate/malignant/*-S2-*.png | wc -l

ls -1 validate/benign/*-S1-*.png | wc -l
ls -1 validate/malignant/*-S1-*.png | wc -l



ls -1 train/benign/*-S5-*.png | wc -l
ls -1 train/malignant/*-S5-*.png | wc -l

ls -1 train/benign/*-S4-*.png | wc -l
ls -1 train/malignant/*-S4-*.png | wc -l

ls -1 train/benign/*-S3-*.png | wc -l
ls -1 train/malignant/*-S3-*.png | wc -l

ls -1 train/benign/*-S2-*.png | wc -l
ls -1 train/malignant/*-S2-*.png | wc -l

ls -1 train/benign/*-S1-*.png | wc -l
ls -1 train/malignant/*-S1-*.png | wc -l
```
