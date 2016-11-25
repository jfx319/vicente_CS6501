
# coding: utf-8

# In[ ]:

import sys, os
import numpy as np
from datetime import datetime
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint, EarlyStopping, TensorBoard, ReduceLROnPlateau, CSVLogger

# target size of input (resizes 101x101 pictures to this)
  #keras doesn't have a random crop preprocessing function yet
img_width, img_height = 96, 96

basedir = 'data'
train_data_dir = basedir+'/train'
validation_data_dir = basedir+'/validate'
os.makedirs(basedir+'/output/models', exist_ok=True)
os.makedirs(basedir+'/output/tensorboard', exist_ok=True)
os.makedirs(basedir+'/output/checkpoints', exist_ok=True)
os.makedirs(basedir+'/output/augmented', exist_ok=True)
nb_train_samples = 28357
nb_validation_samples = 6960
batch_size = 125
nb_epoch = 300

print('Building model...')
model = Sequential()
model.add(Convolution2D(32, 3, 3, input_shape=(img_height, img_width, 1)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Convolution2D(64, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Convolution2D(128, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('sigmoid'))

#sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])


begintime = datetime.now().strftime("%Y%m%d_%H%M%S")

#Save model architechture
json_string = model.to_json()
open(basedir+'/output/models/'+begintime+'-model_architecture.json', 'w').write(json_string)

#Call backs
checkpointer = ModelCheckpoint(filepath=basedir+'/output/checkpoints/'+begintime+'-checkpoint_weights_-{epoch:03d}-{val_acc:.3f}.hdf5', monitor='val_acc', save_weights_only=True, verbose=1, save_best_only=True)
tensorboardlogger = TensorBoard(log_dir=basedir+'/output/tensorboard/', histogram_freq=0, write_graph=True, write_images=False)
#EarlyStopping(monitor='val_loss', min_delta=0, patience=0, verbose=0, mode='auto')
#ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=10, verbose=0, mode='auto', epsilon=0.0001, cooldown=0, min_lr=0)
csvlogger = CSVLogger(basedir+'/output/training.csv', separator=',', append=False)


    
# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
        rescale=1.0/(65535),
        horizontal_flip=True,
        vertical_flip=True)

# this is the augmentation configuration we will use for testing: only rescaling by 16bit value range or original picture
test_datagen = ImageDataGenerator(rescale=1.0/(65535))

train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='binary', 
        color_mode='grayscale')#,
        #save_prefix='augmented',
        #save_to_dir=basedir+'/augmented',
        #save_format='png')

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
        nb_worker=4, 
        pickle_safe=True)

#model.save_weights('first_try.h5')  # always save your weights after training or during training

#model.load_weights(basedir+'/output/checkpoints/20161125_071924-checkpoint_weights_-102-0.572.hdf5')


