Alternative:  use existing AMI

http://www.bitfusion.io/2016/10/21/bitfusion-deep-learning-amis-now-available-on-aws-p2-instances/  
http://www.bitfusion.io/2016/05/09/easy-tensorflow-model-training-aws/  
https://github.com/bitfusionio/amis/tree/master/awsmrkt-bfboost-ubuntu14-cuda75-tensorflow  




https://github.com/saiprashanths/dl-docker#specs

http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cluster_computing.html#install-nvidia-driver
http://www.nvidia.com/object/gpu-accelerated-applications-tensorflow-installation.html

https://aws.amazon.com/blogs/aws/new-p2-instance-type-for-amazon-ec2-up-to-16-gpus/




# Build my own AMI image with up-to-date (~24 minutes for me)

### Start with: Ubuntu Server 14.04 LTS AMI

http://ramhiser.com/2016/01/05/installing-tensorflow-on-an-aws-ec2-instance-with-gpu-support/

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y build-essential git python-pip libfreetype6-dev libxft-dev libncurses-dev libopenblas-dev gfortran python-matplotlib libblas-dev liblapack-dev libatlas-base-dev python-dev python-pydot linux-headers-generic linux-image-extra-virtual unzip python-numpy swig python-pandas python-sklearn unzip wget pkg-config zip g++ zlib1g-dev
sudo pip install -U pip
```

install CUDA Toolkit 7.0
```bash
wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1410/x86_64/cuda-repo-ubuntu1410_7.0-28_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1410_7.0-28_amd64.deb
rm cuda-repo-ubuntu1410_7.0-28_amd64.deb
sudo apt-get update
sudo apt-get install -y cuda

#install CUDNN
#https://developer.nvidia.com/rdp/assets/cudnn-65-linux-v2-asset
tar -zxf cudnn-6.5-linux-x64-v2.tgz && rm cudnn-6.5-linux-x64-v2.tgz
sudo cp -R cudnn-6.5-linux-x64-v2/lib* /usr/local/cuda/lib64/
sudo cp cudnn-6.5-linux-x64-v2/cudnn.h /usr/local/cuda/include/

sudo reboot
```

~/.bashrc
```bash
export CUDA_HOME=/usr/local/cuda
export CUDA_ROOT=/usr/local/cuda
export PATH=$PATH:$CUDA_ROOT/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CUDA_ROOT/lib64
```


install Bazel 0.1.4, JAVA
```bash
sudo add-apt-repository -y ppa:webupd8team/java
sudo apt-get update
# Hack to silently agree license agreement
echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections
echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-selections
sudo apt-get install -y oracle-java8-installer

#install bazel
sudo apt-get install pkg-config zip g++ zlib1g-dev
https://github.com/bazelbuild/bazel/releases/download/0.1.4/bazel-0.1.4-installer-linux-x86_64.sh
chmod +x bazel-0.1.4-installer-linux-x86_64.sh
./bazel-0.1.4-installer-linux-x86_64.sh --user
rm bazel-0.1.4-installer-linux-x86_64.sh
```

install tensorflow
```bash
git clone --recurse-submodules https://github.com/tensorflow/tensorflow
cd tensorflow
```

build TensorFlow with GPU support using CUDA version 3.0 (currently required on AWS) via the unofficial settings.
```bash
TF_UNOFFICIAL_SETTING=1 ./configure
#type 3.0 to use CUDA version 3.0
```

build
```bash
bazel build -c opt --config=cuda //tensorflow/cc:tutorials_example_trainer
bazel build -c opt --config=cuda //tensorflow/tools/pip_package:build_pip_package
bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg
sudo pip install --upgrade /tmp/tensorflow_pkg/tensorflow-0.6.0-cp27-none-linux_x86_64.whl
```

verify working
```bash
python ~/tensorflow/tensorflow/models/image/mnist/convolutional.py
```

```python
import tensorflow as tf
tf_session = tf.Session()
x = tf.constant(1)
y = tf.constant(1)
tf_session.run(x + y)
```



### install other packages: 
```bash
sudo pip install numpy scipy pandas sklearn matplotlib Pillow jupyter

sudo pip install keras 
#version 1.1.1 oct 31st, 2016

sudo pip install keras_diagram
#from keras_diagram import ascii
#print(ascii(model))

sudo pip install kerasvis
#https://github.com/neuralyzer/kerasvis
#from kerasvis import DBLogger
#logger = DBLogger(comment="An example run")
```




