# Installation for KIA vision system
1. [CUDA](https://developer.nvidia.com/cuda-downloads)
- Choose deb(local) version
- Then: 
```
    sudo dpkg -i cuda-repo-<version>.deb
    sudo apt-key add /var/cuda-repo-<version>/7fa2af80.pub
    sudo apt-get update
    sudo apt-get install cuda
```
2. [cudnn](https://developer.nvidia.com/rdp/cudnn-download)
- Choose the one corresponding to the CUDA version (10-0)
- Check the installation [guide](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html)

3. Restart the machine
4. Check installation by:
```
    nvidia-smi
```
there would be a table showing information of the GPU. Otherwise, you are fucked up :)) Go to have a beer then!

5. Install **OpenCV 3**. This is the suported version of **yarpOpenPose**
```
	cd other-libs
	git clone https://github.com/opencv/opencv.git
	cd opencv
	cd ..
	 
	git clone https://github.com/opencv/opencv_contrib.git
	cd opencv_contrib
	cd ..
```

5. Install yarp and icub-main: can use the [yarp-install.sh](https://github.com/towardthesea/KIA_vision_setting/blob/master/yarp-install.sh) script
- Following the manual [here](http://wiki.icub.org/wiki/Linux:Installation_from_sources)

6. Install dependencies:
```
	sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
	sudo apt-get install --no-install-recommends libboost-all-dev
	sudo apt-get install libatlas-base-dev liblapack-dev libblas-dev
	sudo apt-get install libboost-all-dev
```

7. Install [openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose.git) at this commit (safe now):
```
	git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose.git
	git checkout fbee9b65241ddbb7b80ab980bdd90838521a4dbb 
```

8. Install other yarp modules:
```
	git clone https://github.com/robotology/icub-hri.git
	git clone https://github.com/robotology/human-sensing.git --> only install **yarpOpenPose**
	git clone https://github.com/robotology/skeleton3D.git
```
Check out the Skeleton3D to KUKA branch: 
```
	git checkout devel-kuka
```
9. Import context of **yarpOpenPose** and edit the *model_folder* context file **yarpOpenPose.ini** into the path to installed *openpose/models*, e.g. `/home/vision/other-lib/openpose/models/`
```
	yarp-config context --import yarpOpenPose
	gedit ~/.local/share/yarp/contexts/yarpOpenPose/yarpOpenPose.ini
```

10. Install camera [driver](https://github.com/roboception/rc_genicam_api.git)
11. Install camera [discover application](https://github.com/roboception/rcdiscover)

12. Install [rc_yarp_wrapper](https://github.com/robotology-playground/rc_yarp_wrapper) for the camera

13. Calibration the camera wrt the robot with web-based application
    - Run `rcdiscover-gui`
    - Click on the available camera to launch the web-based application
    - In **depth image** tab, make sure that the quality is chosen as **Medium**. **High** option requires more computation hence lower frequency with different depth image size. You can try but don't blame me then :P. Play with Minimum and Maximum distance depending on your application.
    - Open **Hand-eye calibration** tab and follow the on screen manual
	- Measure the calibration grid
	- Choose *sensor mounting* as **Static**
	- Choose *Pose* as **XYZABC** format for the transformation
	- Next Next Next



14. Fill down the frame transformation obtained in (13) in to **cam_in_robot** line of the configuration file `rc_yarp_wrapper.ini` of **rc_yarp_wrapper**. The first line only needs once!
```
	yarp-config context --import rc_yarp_wrapper
	gedit ~/.local/share/yarp/contexts/rc_yarp_wrapper/rc_yarp_wrapper.ini
```
15. Running application (each following line in a terminal):
```
	yarpserver 
	yarpmanager
```
- In yarpmanager, choose the application file from where you install **rc_yarp_wrapper**, e.g. `~/icub-workspace/rc_yarp_wrapper/app/script/rcCam_skeleton3D.xml`
- Open a terminal and check the name of the camera by: `gc_config -l`
- Fill the obtained *name* (e.g. `enp2s0:02938142`) into the *--device* parameter of the **rc_yarp_wrapper** application
- Run all application, Connect ports and write your paper :))


