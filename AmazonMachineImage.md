Alternative:  use existing AMI

benchmarking:  
http://www.bitfusion.io/2016/11/03/quick-comparison-of-tensorflow-gpu-performance-on-aws-p2-and-g2-instances/


http://www.bitfusion.io/2016/10/21/bitfusion-deep-learning-amis-now-available-on-aws-p2-instances/  
http://www.bitfusion.io/2016/05/09/easy-tensorflow-model-training-aws/  
https://github.com/bitfusionio/amis/tree/master/awsmrkt-bfboost-ubuntu14-cuda75-tensorflow  



```
jcx9dy@donna:~$ ssh -i "donna.pem" ubuntu@54.235.54.22
The authenticity of host '54.235.54.22 (54.235.54.22)' can't be established.
ECDSA key fingerprint is SHA256:Duv7Jww2pjr7i4n3lpjBELQOq48hOk1+df9wh9TpBhA.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '54.235.54.22' (ECDSA) to the list of known hosts.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0664 for 'donna.pem' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "donna.pem": bad permissions
Permission denied (publickey).


jcx9dy@donna:~$ chmod 400 donna.pem 
jcx9dy@donna:~$ ssh -i "donna.pem" ubuntu@54.235.54.22


########################################################################################################################
########################################################################################################################

  ____  _ _    __           _               _
 | __ )(_) |_ / _|_   _ ___(_) ___  _ __   (_) ___
 |  _ \| | __| |_| | | / __| |/ _ \| '_ \  | |/ _ \
 | |_) | | |_|  _| |_| \__ \ | (_) | | | |_| | (_) |
 |____/|_|\__|_|  \__,_|___/_|\___/|_| |_(_)_|\___/


Welcome to Bitfusion Ubuntu 14 Tensorflow - Ubuntu 14.04 LTS (GNU/Linux 3.13.0-101-generic x86_64)

This AMI is brought to you by Bitfusion.io
http://www.bitfusion.io

Please email all feedback and support requests to:
support@bitfusion.io

We would love to hear from you! Contact us with any feedback or a feature request at the email above.

########################################################################################################################
########################################################################################################################



########################################################################################################################
########################################################################################################################

                                           BITFUSION EMAIL OPT IN                                                       

Register your email address to be entered into our monthly draw for Bitfusion t-shirts and  occasional hardware         
goodies.  Additionally you will receive product updates and information about new offerings from Bitfusion.

########################################################################################################################
########################################################################################################################

Would you like to register with Bitfusion.io? [y/n] n

Thank you for using the Bitfusion Ubuntu 14 Tensorflow

Please review the README located at /home/ubuntu/README for more details on how to use this AMI




ubuntu@ip-172-31-60-241:~$ nvidia-smi
Tue Nov 22 18:15:05 2016       
+------------------------------------------------------+                       
| NVIDIA-SMI 352.99     Driver Version: 352.99         |                       
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla K80           On   | 0000:00:1E.0     Off |                    0 |
| N/A   35C    P8    30W / 149W |     55MiB / 11519MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID  Type  Process name                               Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+



ubuntu@ip-172-31-60-241:~$ top

top - 18:16:48 up 6 min,  1 user,  load average: 0.13, 0.61, 0.36
Tasks: 141 total,   1 running, 140 sleeping,   0 stopped,   0 zombie
%Cpu0  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu1  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu2  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu3  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:  62881772 total,   918128 used, 61963644 free,    35080 buffers
KiB Swap:        0 total,        0 used,        0 free.   321184 cached Mem


ubuntu@ip-172-31-60-241:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
udev             30G   12K   30G   1% /dev
tmpfs           6.0G  796K  6.0G   1% /run
/dev/xvda1       99G   25G   70G  27% /
none            4.0K     0  4.0K   0% /sys/fs/cgroup
none            5.0M     0  5.0M   0% /run/lock
none             30G   12K   30G   1% /run/shm
none            100M  8.0K  100M   1% /run/user


ubuntu@ip-172-31-60-241:~$ ll
total 140
drwxr-xr-x 17 ubuntu ubuntu  4096 Nov 16 00:46 ./
drwxr-xr-x  4 root   root    4096 Nov 15 21:41 ../
-rw-r--r--  1 root   root       0 Nov 16 00:46 .bash_history
-rw-r--r--  1 ubuntu ubuntu   220 Apr  9  2014 .bash_logout
-rw-r--r--  1 ubuntu ubuntu  3688 Nov 15 21:50 .bashrc
drwxr-xr-x  4 ubuntu ubuntu  4096 Nov 15 21:50 .bazel/
drwxr-xr-x  2 ubuntu ubuntu  4096 Nov 15 21:50 bin/
drwx------  4 ubuntu ubuntu  4096 Nov 15 21:50 .cache/
drwxr-xr-x  3 ubuntu ubuntu  4096 Nov 15 21:41 .config/
-rw-rw-r--  1 ubuntu ubuntu 38324 Nov 18 23:30 EULA
-rw-------  1 root   root       0 Nov 16 00:46 .history
drwx------  4 ubuntu ubuntu  4096 Nov 22 18:12 .jupyter/
drwxr-xr-x  2 ubuntu ubuntu  4096 Nov 16 00:45 .keras/
drwxr-xr-x  2 ubuntu ubuntu  4096 Nov 16 00:45 keras-examples/
drwxr-xr-x  3 ubuntu ubuntu  4096 Nov 15 21:41 .local/
drwxr-xr-x  6 ubuntu ubuntu  4096 Nov 15 23:58 magenta/
drwx------  3 root   root    4096 Nov 16 00:00 .nv/
drwxr-xr-x  2 ubuntu ubuntu  4096 Nov 15 21:50 .oracle_jre_usage/
-rw-r--r--  1 ubuntu ubuntu   705 Nov 16 00:46 .profile
drwxr-xr-x  3 ubuntu ubuntu  4096 Nov 16 00:46 pynb/
-rw-rw-r--  1 ubuntu ubuntu 12837 Nov 18 23:30 README
-rw-------  1 root   root    1024 Nov 15 21:41 .rnd
drwx------  2 ubuntu ubuntu  4096 Nov 15 00:03 .ssh/
drwxr-xr-x  7 ubuntu ubuntu  4096 Nov 15 22:55 tensorflow/
drwxr-xr-x  7 ubuntu ubuntu  4096 Nov 16 00:07 tf-serving/



ubuntu@ip-172-31-60-241:~$ uname -a
Linux ip-172-31-60-241 3.13.0-101-generic #148-Ubuntu SMP Thu Oct 20 22:08:32 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux


ubuntu@ip-172-31-60-241:~$ which python
/usr/bin/python
ubuntu@ip-172-31-60-241:~$ which python3
/usr/bin/python3
ubuntu@ip-172-31-60-241:~$ python --version
Python 2.7.6
ubuntu@ip-172-31-60-241:~$ python3 --version
Python 3.4.3


ubuntu@ip-172-31-60-241:~$ python ~/tensorflow/tensorflow/models/image/cifar10/cifar10_multi_gpu_train.py
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcublas.so.7.5 locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcudnn.so.5 locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcufft.so.7.5 locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcuda.so.1 locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcurand.so.7.5 locally
>> Downloading cifar-10-binary.tar.gz 100.0%
Successfully downloaded cifar-10-binary.tar.gz 170052171 bytes.
Filling queue with 20000 CIFAR images before starting to train. This will take a few minutes.
I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:925] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
I tensorflow/core/common_runtime/gpu/gpu_device.cc:951] Found device 0 with properties: 
name: Tesla K80
major: 3 minor: 7 memoryClockRate (GHz) 0.8235
pciBusID 0000:00:1e.0
Total memory: 11.25GiB
Free memory: 11.13GiB
I tensorflow/core/common_runtime/gpu/gpu_device.cc:972] DMA: 0 
I tensorflow/core/common_runtime/gpu/gpu_device.cc:982] 0:   Y 
I tensorflow/core/common_runtime/gpu/gpu_device.cc:1041] Creating TensorFlow device (/gpu:0) -> (device: 0, name: Tesla K80, pci bus id: 0000:00:1e.0)
2016-11-22 18:29:20.997334: step 0, loss = 4.67 (2.1 examples/sec; 62.301 sec/batch)
2016-11-22 18:29:23.064279: step 10, loss = 4.64 (840.6 examples/sec; 0.152 sec/batch)
2016-11-22 18:29:24.643143: step 20, loss = 4.51 (826.9 examples/sec; 0.155 sec/batch)
2016-11-22 18:29:26.254807: step 30, loss = 4.39 (770.8 examples/sec; 0.166 sec/batch)
2016-11-22 18:29:27.873522: step 40, loss = 4.40 (770.2 examples/sec; 0.166 sec/batch)
2016-11-22 18:29:29.533449: step 50, loss = 4.23 (766.2 examples/sec; 0.167 sec/batch)
2016-11-22 18:29:31.175779: step 60, loss = 4.33 (825.3 examples/sec; 0.155 sec/batch)
2016-11-22 18:29:32.838024: step 70, loss = 4.41 (788.5 examples/sec; 0.162 sec/batch)
2016-11-22 18:29:34.486316: step 80, loss = 4.40 (790.2 examples/sec; 0.162 sec/batch)
2016-11-22 18:29:36.158620: step 90, loss = 4.09 (744.8 examples/sec; 0.172 sec/batch)
2016-11-22 18:29:37.821699: step 100, loss = 4.12 (766.1 examples/sec; 0.167 sec/batch)

2016-11-22 18:29:54.621281: step 200, loss = 3.82 (783.4 examples/sec; 0.163 sec/batch)
2016-11-22 18:30:11.167037: step 300, loss = 3.56 (774.1 examples/sec; 0.165 sec/batch)
2016-11-22 18:30:27.910897: step 400, loss = 3.37 (763.4 examples/sec; 0.168 sec/batch)

2016-11-22 18:30:44.432482: step 500, loss = 3.09 (766.8 examples/sec; 0.167 sec/batch)

2016-11-22 18:32:07.944061: step 1000, loss = 2.53 (787.3 examples/sec; 0.163 sec/batch)
2016-11-22 18:34:56.223261: step 2000, loss = 1.50 (769.3 examples/sec; 0.166 sec/batch)
2016-11-22 18:37:43.819220: step 3000, loss = 1.48 (766.6 examples/sec; 0.167 sec/batch)
2016-11-22 18:40:30.868867: step 4000, loss = 1.15 (759.0 examples/sec; 0.169 sec/batch)
2016-11-22 18:43:17.959348: step 5000, loss = 0.79 (801.6 examples/sec; 0.160 sec/batch)
2016-11-22 18:46:03.535481: step 6000, loss = 0.98 (775.0 examples/sec; 0.165 sec/batch)
2016-11-22 18:48:50.086918: step 7000, loss = 0.94 (786.9 examples/sec; 0.163 sec/batch)
2016-11-22 18:51:35.410308: step 8000, loss = 1.26 (800.2 examples/sec; 0.160 sec/batch)
2016-11-22 18:54:20.427048: step 9000, loss = 0.95 (780.1 examples/sec; 0.164 sec/batch)
2016-11-22 18:57:06.321096: step 10000, loss = 0.96 (755.7 examples/sec; 0.169 sec/batch)
2016-11-22 18:59:52.777928: step 11000, loss = 0.83 (793.5 examples/sec; 0.161 sec/batch)
2016-11-22 19:02:38.845511: step 12000, loss = 0.86 (785.2 examples/sec; 0.163 sec/batch)
2016-11-22 19:05:24.809961: step 13000, loss = 0.95 (791.0 examples/sec; 0.162 sec/batch)


ubuntu@ip-172-31-60-241:~$ python ~/tensorflow/tensorflow/models/image/cifar10/cifar10_eval.py
2016-11-22 19:53:21.111682: precision @ 1 = 0.827

```




```
https://www.tensorflow.org/versions/r0.11/tutorials/deep_cnn/index.html

It consists of 1,068,298 learnable parameters and requires about 19.5M multiply-add operations to compute inference on a single image.


https://github.com/tensorflow/tensorflow/blob/master/tensorflow/models/image/cifar10/cifar10_multi_gpu_train.py

Accuracy:
cifar10_multi_gpu_train.py achieves ~86% accuracy after 100K steps (256
epochs of data) as judged by cifar10_eval.py.
Speed: With batch_size 128.
System        | Step Time (sec/batch)  |     Accuracy
--------------------------------------------------------------------
1 Tesla K20m  | 0.35-0.60              | ~86% at 60K steps  (5 hours)
1 Tesla K40m  | 0.25-0.35              | ~86% at 100K steps (4 hours)
2 Tesla K20m  | 0.13-0.20              | ~84% at 30K steps  (2.5 hours)
3 Tesla K20m  | 0.13-0.18              | ~84% at 30K steps
4 Tesla K20m  | ~0.10                  | ~84% at 30K steps
```


New Group Security policy 
```
TCP protocols:
enable port 8787
enable port 8888 for ipython
enable port 6006 for tensorboard
enable port 22 for ssh
enable port 80 for http
enable port 443 for https
```




```bash
US East (N. Virginia)	ami-bbd1e7ac
```
cuda 8.0  ,  16 GiB root volume that was sufficient for the installation
http://expressionflow.com/2016/10/09/installing-tensorflow-on-an-aws-ec2-p2-gpu-instance/

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




