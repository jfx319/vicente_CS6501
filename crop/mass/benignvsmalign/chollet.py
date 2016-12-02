#!/usr/bin/python3
# coding: utf-8

import sys, os
import numpy as np
from datetime import datetime
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D, SpatialDropout2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint, EarlyStopping, TensorBoard, ReduceLROnPlateau, CSVLogger
from keras.layers import BatchNormalization

basedir = './'
train_data_dir = basedir+'/train'
validation_data_dir = basedir+'/validate'
os.makedirs(basedir+'/output/models', exist_ok=True)
os.makedirs(basedir+'/output/tensorboard', exist_ok=True)
os.makedirs(basedir+'/output/checkpoints', exist_ok=True)
os.makedirs(basedir+'/output/augmented', exist_ok=True)
nb_train_samples = 7
nb_validation_samples = 7
batch_size = 32
nb_epoch = 1
nb_worker = 8  #cpus for real-time image augmentation
img_width, img_height = 224, 224  # target size of input (resizes pictures to this)
modelname = 'chollet_actual'

print('Building model...')
model = Sequential()
model.add(Convolution2D(32, 3, 3, input_shape=(img_height, img_width, 1)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Convolution2D(64, 3, 3))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Convolution2D(128, 3, 3))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

begintime = datetime.now().strftime("%Y%m%d_%H%M%S")

#Save model architechture
json_string = model.to_json()
open(basedir+'/output/models/'+begintime+'-'+modelname+'.json', 'w').write(json_string)

#Call backs
checkpointer = ModelCheckpoint(filepath=basedir+'/output/checkpoints/'+begintime+'-'+modelname+'-{epoch:03d}-{val_acc:.3f}.hdf5', monitor='val_acc', save_weights_only=True, verbose=1, save_best_only=True)
tensorboardlogger = TensorBoard(log_dir=basedir+'/output/tensorboard/', histogram_freq=0, write_graph=True, write_images=False)
#earlystop = EarlyStopping(monitor='val_acc', min_delta=0.001, patience=10, verbose=1, mode='auto')
#reducelr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=10, verbose=1, mode='auto', epsilon=0.0001, cooldown=0, min_lr=0.001)
csvlogger = CSVLogger(basedir+'/output/'+begintime+'-'+modelname+'.csv', separator=',', append=False)



# this is the augmentation configuration we will use for training
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
        color_mode='grayscale'    #,
                                  #save_prefix='augmented',
                                  #save_to_dir=basedir+'/output/augmented',
                                  #save_format='png'
        )

validation_generator = test_datagen.flow_from_directory(
        validation_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='binary',
        color_mode='grayscale')

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

#model.save_weights('first_try.h5')  # always save your weights after training or during training

#model.load_weights(basedir+'/output/checkpoints/20161125_071924-checkpoint_weights_-102-0.572.hdf5')



