# Install OpenCV 3.1.0 on Ubuntu 16.04 with Python3 bindings

Follows: http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/

```bash
#http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/


cd /home/jcx9dy/git/

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libgtk-3-dev
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install python2.7-dev python3.5-dev


wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip
unzip opencv.zip

wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip
unzip opencv_contrib.zip

cd opencv-3.1.0/
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_EXTRA_MODULES_PATH=/home/jcx9dy/git/opencv_contrib-3.1.0/modules \
    -D PYTHON_EXECUTABLE=/usr/bin/python \
    -D BUILD_EXAMPLES=ON \
    -D WITH_CUDA=OFF \
    -D INSTALL_C_EXAMPLES=OFF ..

make -j8
sudo make install
sudo ldconfig


######
python3
import cv2
print cv2.__version__

### Tutorials

#http://www.pyimagesearch.com/2016/06/20/detecting-cats-in-images-with-opencv/
#https://www.pyimagesearch.com/practical-python-opencv/
```

### Tutorials

#http://www.pyimagesearch.com/2016/06/20/detecting-cats-in-images-with-opencv/
#https://www.pyimagesearch.com/practical-python-opencv/
