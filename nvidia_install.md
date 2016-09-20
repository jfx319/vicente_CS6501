

### Run iTorch using Docker

I encountered some amount of difficulty Initially when I try to install iTorch/Jupyter locally on my Mac machine (mainly due to a security update of El Capitan and one of the dependencies just won't install). If you guys also hard time installing iTorch, it may be beneficial to try using Docker container. Docker can be thought as a very light-weight virtual machine (Read more here https://www.docker.com/what-docker). Here are the steps:
 
1. Installing Docker depending on your OS  
Ubuntu: https://docs.docker.com/installation/ubuntulinux/  
Mac: https://docs.docker.com/docker-for-mac/  
Windows: https://docs.docker.com/docker-for-windows/  
More OS options available: https://docs.docker.com/engine/installation/  
 
This step should be straightforward, but you may encounter problem like insufficient machine memory so docker for Mac cannot be installed. In that case you can try installing Docker Machine. After Docker is installed, your life will be much easier.
 
2. Pull down the iTorch Docker image  
In your terminal  
```
docker pull kaixhin/torch
```

3. Start up the iTorch instance  
```
docker run -it --rm -p 8888:8888 dhunter/itorch-notebook
```

Need to look into setting a password for this container.

And that's it!
 
4. Try iTorch in your browser!  
Go to localhost:8888 if you are using Linux Docker or Docker for Mac/Window. If you end up using Docker Machine, go to <docker VM's IP Address(on the top under the whale when you bring up the Docker QuickStart Terminal)>:8888
 




### To use cuda using nvidia docker
To use cuda using docker, you may take a look at this docker image.  
https://hub.docker.com/r/kaixhin/cuda-torch/

And to run this docker, you need to install nvidia docker first.  
https://github.com/NVIDIA/nvidia-docker
```
wget -P /tmp https://github.com/NVIDIA/nvidia-docker/releases/download/v1.0.0-rc.3/nvidia-docker_1.0.0.rc.3-1_amd64.deb
sudo dpkg -i /tmp/nvidia-docker*.deb && rm /tmp/nvidia-docker*.deb
```

And checkout this page for cuda version to use which depends on your nvidia driver version.  
https://github.com/NVIDIA/nvidia-docker/wiki/CUDA#requirements
```bash
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update
sudo apt-get install nvidia-361

#Reboot system to load drivers. 
#Note to self: skipped mesa and freeglut3 for now. Did not bother disabling Nouveau

sudo apt-get install mesa-common-dev
sudo apt-get install freeglut3-dev
```

Once you've finished installing nvidia driver and nvidia-docker, run:
```
nvidia-docker run -it --rm -p 8888:8888 kaixhin/cuda-torch

Then run jupyter notebook --ip="0.0.0.0" --no-browser to open a notebook on localhost:8888.

python kernel not found
need to install itorch kernel (not included in kaixhin's container)

```




### A useful guide for CUDA installation

I followed this guide to install latest cuda and nvidia driver for my GTX1070. My Linux version is 16.04.  This method works for all pascal graphic cards(PASCAL TITAN XGTX1080, GTX1070, GTX1060).  
https://yangcha.github.io/GTX-1080/

Based on some online survey and correspondence with Rivanna GPU HPC support, I might try a slightly older version: 

```
For tensorflow: 
https://www.tensorflow.org/versions/r0.10/get_started/os_setup.html#optional-install-cuda-gpus-on-linux

For torch: 
https://github.com/soumith/cudnn.torch

For install, there are three things to link up: 

1.  Nvidia GPU driver version
2.  Cuda Toolkit 7.5
3.  CUDNN v5 (nvidia's neural network library)

I believe I can locally install #2 and #3, but the Nvidia driver is the difficult one as it probably requires sudo privileges. I'm not sure what driver version is currently on there, I'd have to do some reading to see if it is compatible.

++

If this is too difficult or impossible on Rivanna's gpu, then I'll have to look into other options. But if it helps, I intended to loosely follow this Amazon install: 
http://www.pyimagesearch.com/2016/07/04/how-to-install-cuda-toolkit-and-cudnn-for-deep-learning/

Some people had compatibility issues with gpu driver version: 

Replacing the version 352.39 of the nvidia driver that was coming with CUDA 7.5 with version 361.45 (downloaded) solved the problem: 
# first download the installer from http://www.nvidia.com/download/driverResults.aspx/103306/en-us
# then unload the old driver, and install/build/load the new one:
$ sudo modprobe -r nvidia
$ sudo ./NVIDIA-Linux-x86_64-361.45.11.run
```






