import sys, os
import h5py
import numpy as np
from datetime import datetime
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.optimizers import SGD
from keras.models import Model
#from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D, SpatialDropout2D
from keras.layers import Activation, Dropout, Flatten, Dense, GlobalAveragePooling2D
from keras.callbacks import ModelCheckpoint, TensorBoard, CSVLogger
#from keras.layers import BatchNormalization

from keras.applications.resnet50 import ResNet50

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
nb_epoch = 500
img_width, img_height = 224, 224  # target size of input (resizes pictures to this)
modelname = 'ResNet50'

#################################################################
# build the ResNet50 network
base_model = ResNet50(include_top=False, weights='imagenet', input_shape=(img_width, img_height, 3))
  #175 layers in notop
  #last layer is avg_pool
  #177 layers in full
  #last layer is flatten, then fc1000

for i, layer in enumerate(base_model.layers):
    print(i, layer.name)

#add our own classfication layer
x = base_model.output
x = Flatten()(x)
predictions = Dense(2, activation='softmax')(x)

#convert to model object
model = Model(input=base_model.input, output=predictions)

for i, layer in enumerate(model.layers):
    print(i, layer.name)

#add regularizers:
for layer in model.layers():
    if hasattr(layer, 'W_regularizer'):
        layer.W_regularizer = l2(l=0.001)

#Save model architechture
json_string = model.to_json()
open(basedir+'/output/models/'+modelname+'_adapted.json', 'w').write(json_string)

# first: train only the top layers (which were randomly initialized)
for layer in base_model.layers:
    layer.trainable = False

# compile the model (should be done *after* setting layers to non-trainable)
model.compile(optimizer=SGD(lr=.01, decay=0.0005, momentum=0.9), loss='categorical_crossentropy', metrics=['accuracy'])


############ STEP ONE
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
        class_mode='categorical', 
        color_mode='rgb')

validation_generator = test_datagen.flow_from_directory(
        validation_data_dir, target_size=(img_width, img_height), batch_size=batch_size,
        class_mode='categorical',
        color_mode='rgb')


# train the model on the new data for a few epochs
print('Training top classifier... ')
model.fit_generator(
        train_generator, samples_per_epoch=nb_train_samples, nb_epoch=10,
        validation_data=validation_generator, nb_val_samples=nb_validation_samples, 
        callbacks=[csvlogger],
        nb_worker=nb_worker, pickle_safe=True)

############ STEP TWO

### Open up last convolution block 5 for training
for layer in model.layers[:142]:
    layer.trainable = False
for layer in model.layers[142:]:
    layer.trainable = True

# compile the model with a SGD/momentum optimizer and a very slow learning rate.
model.compile(loss='categorical_crossentropy',
              optimizer=SGD(lr=.01, decay=0.0005, momentum=0.9),
              metrics=['accuracy'])

begintime = datetime.now().strftime("%Y%m%d_%H%M%S")

#Call backs
checkpointer = ModelCheckpoint(filepath=basedir+'/output/checkpoints/'+begintime+'-'+modelname+'_block5-{epoch:03d}-{val_acc:.3f}.hdf5', monitor='val_acc', save_weights_only=True, verbose=1, save_best_only=True)
tensorboardlogger = TensorBoard(log_dir=basedir+'/output/tensorboard/', histogram_freq=0, write_graph=True, write_images=False)
csvlogger = CSVLogger(basedir+'/output/'+begintime+'-'+modelname+'_block5.csv', separator=',', append=False)

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

### train block5
print('Fine tuning last convolution block model... ')
model.fit_generator(
        train_generator, samples_per_epoch=nb_train_samples, nb_epoch=100,
        validation_data=validation_generator, nb_val_samples=nb_validation_samples, 
        callbacks=[checkpointer, tensorboardlogger, csvlogger],
        nb_worker=nb_worker, pickle_safe=True)
        
model.save(modelname+'block5_fullmodel.hdf5')



############# STEP THREE

### Open up all layers for training
for layer in model.layers:
    layer.trainable = True

# compile the model with a SGD/momentum optimizer and a very slow learning rate.
model.compile(loss='categorical_crossentropy',
              optimizer=SGD(lr=.01, decay=0.0005, momentum=0.9),
              metrics=['accuracy'])

begintime = datetime.now().strftime("%Y%m%d_%H%M%S")

#Call backs
checkpointer = ModelCheckpoint(filepath=basedir+'/output/checkpoints/'+begintime+'-'+modelname+'_full-{epoch:03d}-{val_acc:.3f}.hdf5', monitor='val_acc', save_weights_only=True, verbose=1, save_best_only=True)
tensorboardlogger = TensorBoard(log_dir=basedir+'/output/tensorboard/', histogram_freq=0, write_graph=True, write_images=False)
csvlogger = CSVLogger(basedir+'/output/'+begintime+'-'+modelname+'_full.csv', separator=',', append=False)

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

### train full model
print('Fine tuning full model... ')
model.fit_generator(
        train_generator, samples_per_epoch=nb_train_samples, nb_epoch=nb_epoch,
        validation_data=validation_generator, nb_val_samples=nb_validation_samples, 
        callbacks=[checkpointer, tensorboardlogger, csvlogger],
        nb_worker=nb_worker, pickle_safe=True)

model.save(modelname+'_full.hdf5')

