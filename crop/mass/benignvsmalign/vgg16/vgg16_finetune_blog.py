import sys, os
import h5py
import numpy as np
from datetime import datetime
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras import optimizers
from keras.models import Model
#from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D, SpatialDropout2D
from keras.layers import Activation, Dropout, Flatten, Dense, GlobalAveragePooling2D
from keras.callbacks import ModelCheckpoint, TensorBoard, CSVLogger
#from keras.layers import BatchNormalization

from keras.applications.vgg16 import VGG16

########################################

basedir = './'
train_data_dir = basedir+'/train'
validation_data_dir = basedir+'/validate'
os.makedirs(basedir+'/output/models', exist_ok=True)
os.makedirs(basedir+'/output/tensorboard', exist_ok=True)
os.makedirs(basedir+'/output/checkpoints', exist_ok=True)
os.makedirs(basedir+'/output/augmented', exist_ok=True)
nb_train_samples = 1881
nb_train_class0 = 903         #benign
nb_train_class1 = 978         #malignant
nb_validation_samples = 481
nb_validation_class0 = 238    #benign
nb_validation_class1 = 243    #malignant

nb_worker = 8  #cpus for real-time image augmentation
batch_size = 32
nb_epoch = 1000
img_width, img_height = 224, 224  # target size of input (resizes pictures to this)
modelname = 'VGG16notop'

#################################################################
# build the VGG16 network
base_model = VGG16(include_top=False, weights='imagenet', input_shape=(img_width, img_height, 3))

# build a classifier model to put on top of the convolutional model
top_model = Sequential()
top_model.add(Flatten(input_shape=base_model.output_shape[1:]))
top_model.add(Dense(256, activation='relu'))
top_model.add(Dropout(0.5))
top_model.add(Dense(1, activation='sigmoid'))

# note that it is necessary to start with a fully-trained
# classifier, including the top classifier, in order to successfully do fine-tuning
top_model.load_weights(basedir+'/output/checkpoints/'+modelname+'_top_weights.hdf5')

# add the model on top of the convolutional base
model = Model(input=base_model.input, output=top_model.output)
############################ not working yet


# freeze first 25 layers (up to the last conv block)
for layer in model.layers[:25]:  #model.layers has length 19 initially
    layer.trainable = False

# compile the model with a SGD/momentum optimizer and a very slow learning rate.
model.compile(loss='binary_crossentropy',
              optimizer=optimizers.SGD(lr=1e-4, momentum=0.9),
              metrics=['accuracy'])

begintime = datetime.now().strftime("%Y%m%d_%H%M%S")

#Save model architechture
json_string = model.to_json()
open(basedir+'/output/models/'+begintime+'-'+modelname+'.json', 'w').write(json_string)

#Call backs
checkpointer = ModelCheckpoint(filepath=basedir+'/output/checkpoints/'+begintime+'-'+modelname+'_finetune-{epoch:03d}-{val_acc:.3f}.hdf5', monitor='val_acc', save_weights_only=True, verbose=1, save_best_only=True)
tensorboardlogger = TensorBoard(log_dir=basedir+'/output/tensorboard/', histogram_freq=0, write_graph=True, write_images=False)
#earlystop = EarlyStopping(monitor='val_acc', min_delta=0.001, patience=10, verbose=1, mode='auto')
#reducelr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=10, verbose=1, mode='auto', epsilon=0.0001, cooldown=0, min_lr=0.001)
csvlogger = CSVLogger(basedir+'/output/'+begintime+'-'+modelname+'_finetune.csv', separator=',', append=False)

# prepare data augmentation configuration
train_datagen = ImageDataGenerator(
        rescale=1.0/65535,
        rotation_range=360,
        horizontal_flip=True,
        vertical_flip=True, 
        fill_mode='constant',
        cval=0)

# this is the augmentation configuration we will use for testing: only rescaling by 16bit value range or original picture
test_datagen = ImageDataGenerator(
        rescale=1.0/65535
        )

train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='binary', 
        color_mode='rgb'    #,
                                  #save_prefix='augmented',
                                  #save_to_dir=basedir+'/output/augmented',
                                  #save_format='png'
        )

validation_generator = test_datagen.flow_from_directory(
        validation_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='binary',
        color_mode='rgb')

### Train model
print('Training model... ')
model.fit_generator(
        train_generator,
        samples_per_epoch=nb_train_samples,
        nb_epoch=nb_epoch,
        validation_data=validation_generator,
        nb_val_samples=nb_validation_samples, 
        callbacks=[checkpointer, tensorboardlogger, csvlogger],
        nb_worker=nb_worker, 
        pickle_safe=True)
