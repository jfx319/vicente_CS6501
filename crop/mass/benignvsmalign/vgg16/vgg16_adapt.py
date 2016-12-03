
import sys, os
import h5py
import numpy as np
from datetime import datetime
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
#from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D, SpatialDropout2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint, EarlyStopping, TensorBoard, ReduceLROnPlateau, CSVLogger
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
nb_epoch = 100
img_width, img_height = 224, 224  # target size of input (resizes pictures to this)
modelname = 'VGG16notop'


def save_bottlebeck_features():

    # load the VGG16 network with ImageNet weights
    model = VGG16(weights='imagenet', include_top=False)
    print('Model loaded.')
    
    datagen = ImageDataGenerator(rescale=1./65535)
    generator = datagen.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode=None, # predict method doesn't accept labels
        shuffle=False)   # our data will be in order 903 benign, 978 malignant
    bottleneck_features_train = model.predict_generator(generator, nb_train_samples)
    np.save(basedir+'/output/checkpoints/'+modelname+'_bottleneck_features_train.npy', bottleneck_features_train)
    print('train bottleneck features saved, shape:', bottleneck_features_train.shape)
    
    generator = datagen.flow_from_directory(
        validation_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode=None,  # predict method doesn't accept labels
        shuffle=False)    # our data will be in order 238 benign, 243 malignant
    bottleneck_features_validation = model.predict_generator(generator, nb_validation_samples)
    np.save(basedir+'/output/checkpoints/'+modelname+'_bottleneck_features_validation.npy', bottleneck_features_validation)
    print('validation bottleneck features saved, shape:', bottleneck_features_train.shape)

def train_top_model():
    train_data = np.load(basedir+'/output/checkpoints/'+modelname+'_bottleneck_features_train.npy')
    train_labels = np.array( [0]*nb_train_class0 + [1]*nb_train_class1 )

    validation_data = np.load(basedir+'/output/checkpoints/'+modelname+'_bottleneck_features_validation.npy')
    validation_labels = np.array( [0]*nb_validation_class0  + [1]*nb_validation_class1 )

    model = Sequential()
    model.add(Flatten(input_shape=train_data.shape[1:]))
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

    #Call backs
    csvlogger = CSVLogger(basedir+'/output/'+modelname+'_top_weights.csv', separator=',', append=True)

    model.fit(train_data, train_labels,
        nb_epoch=nb_epoch, 
        batch_size=batch_size,
        validation_data=(validation_data, validation_labels),
        callbacks=[csvlogger])
    
    model.save_weights(basedir+'/output/checkpoints/'+modelname+'_top_weights.hdf5')
    
### MAIN
save_bottlebeck_features()
train_top_model()
