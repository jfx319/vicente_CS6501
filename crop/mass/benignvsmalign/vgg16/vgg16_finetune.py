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
nb_validation_samples = 481

nb_worker = 4  #cpus for real-time image augmentation
batch_size = 32
nb_epoch = 1000
img_width, img_height = 224, 224  # target size of input (resizes pictures to this)
modelname = 'VGG16'

#################################################################
# build the VGG16 network
base_model = VGG16(include_top=False, weights='imagenet', input_shape=(img_width, img_height, 3))

# add a global spatial average pooling layer
x = base_model.output
x = GlobalAveragePooling2D()(x)
# let's add a fully-connected layer
x = Dense(128, activation='relu')(x)
# and a logistic layer -- n classes
predictions = Dense(1, activation='softmax')(x)

# add the model on top of the convolutional base
model = Model(input=base_model.input, output=predictions)

#Save model architechture
json_string = model.to_json()
open(basedir+'/output/models/'+modelname+'_adapted.json', 'w').write(json_string)


# first: train only the top layers (which were randomly initialized)
for layer in base_model.layers:
    layer.trainable = False

# compile the model (should be done *after* setting layers to non-trainable)
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])


############
begintime = datetime.now().strftime("%Y%m%d_%H%M%S")

#Call backs
csvlogger = CSVLogger(basedir+'/output/'+begintime+'-'+modelname+'_traintop.csv', separator=',', append=False)

# prepare data augmentation configuration
train_datagen = ImageDataGenerator(
        rescale=1.0/65535,
        rotation_range=360,
        horizontal_flip=True, vertical_flip=True, 
        fill_mode='constant', cval=0)

# this is the augmentation configuration we will use for testing: only rescaling by 16bit value range or original picture
test_datagen = ImageDataGenerator(
        rescale=1.0/65535)

train_generator = train_datagen.flow_from_directory(
        train_data_dir, target_size=(img_width, img_height), batch_size=batch_size,
        class_mode='binary', 
        color_mode='rgb')

validation_generator = test_datagen.flow_from_directory(
        validation_data_dir, target_size=(img_width, img_height), batch_size=batch_size,
        class_mode='binary',
        color_mode='rgb')


# train the model on the new data for a few epochs
print('Training top layers... ')
model.fit_generator(
        train_generator, samples_per_epoch=nb_train_samples, nb_epoch=5,
        validation_data=validation_generator, nb_val_samples=nb_validation_samples, 
        callbacks=[csvlogger],
        nb_worker=nb_worker, pickle_safe=True)

############


### Open up last convolution block for training
for layer in model.layers[:15]:
    layer.trainable = False
for layer in model.layers[15:]:
    layer.trainable = True

# compile the model with a SGD/momentum optimizer and a very slow learning rate.
model.compile(loss='binary_crossentropy',
              optimizer=optimizers.SGD(lr=1e-4, momentum=0.9),
              metrics=['accuracy'])


begintime = datetime.now().strftime("%Y%m%d_%H%M%S")

#Call backs
checkpointer = ModelCheckpoint(filepath=basedir+'/output/checkpoints/'+begintime+'-'+modelname+'_finetune-{epoch:03d}-{val_acc:.3f}.hdf5', monitor='val_acc', save_weights_only=True, verbose=1, save_best_only=True)
tensorboardlogger = TensorBoard(log_dir=basedir+'/output/tensorboard/', histogram_freq=0, write_graph=True, write_images=False)
csvlogger = CSVLogger(basedir+'/output/'+begintime+'-'+modelname+'_finetune.csv', separator=',', append=False)

# prepare data augmentation configuration
train_datagen = ImageDataGenerator(
        rescale=1.0/65535,
        rotation_range=360,
        horizontal_flip=True, vertical_flip=True, 
        fill_mode='constant', cval=0)

# this is the augmentation configuration we will use for testing: only rescaling by 16bit value range or original picture
test_datagen = ImageDataGenerator(
        rescale=1.0/65535)

train_generator = train_datagen.flow_from_directory(
        train_data_dir, target_size=(img_width, img_height), batch_size=batch_size,
        class_mode='binary', 
        color_mode='rgb')

validation_generator = test_datagen.flow_from_directory(
        validation_data_dir, target_size=(img_width, img_height), batch_size=batch_size,
        class_mode='binary',
        color_mode='rgb')

### Fine-tune model
print('Fine tuning last convolution block model... ')
model.fit_generator(
        train_generator, samples_per_epoch=nb_train_samples, nb_epoch=nb_epoch,
        validation_data=validation_generator, nb_val_samples=nb_validation_samples, 
        callbacks=[checkpointer, tensorboardlogger, csvlogger],
        nb_worker=nb_worker, pickle_safe=True)



### Open up last convolution block for training
for layer in model.layers:
    layer.trainable = True

#for i, layer in enumerate(base_model.layers):
#   print(i, layer.name)

