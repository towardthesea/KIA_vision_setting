#!/bin/bash

# Essentials
sudo apt-get install build-essential
sudo apt-get install git
sudo apt-get install cmake
sudo apt-get install cmake-curses-gui
sudo apt-get install libedit-dev

# YARP related dependencies
sudo sh -c 'echo "deb http://www.icub.org/ubuntu $(lsb_release -c | awk '"'"'{print $2}'"'"') contrib/science" > /etc/apt/sources.list.d/icub.list'
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 57A5ACB6110576A6
sudo apt-get update
sudo apt-get install icub-common

# Gazebo
#sudo apt-get install gazebo7 libgazebo7-dev

cd ~

mkdir icub-install
mkdir icub-workspace 
export ROBOT_CODE=~/icub-workspace
export ROBOT_INSTALL=~/icub-install

cd icub-workspace
git clone https://github.com/robotology/yarp.git
git clone https://github.com/robotology/icub-main.git
git clone https://github.com/robotology/icub-contrib-common.git
git clone https://github.com/robotology/icub-hri.git
git clone https://github.com/robotology/kinect-wrapper.git
git clone https://github.com/robotology/human-sensing.git
git clone https://github.com/robotology/skeleton3D.git
git clone https://github.com/robotology-playground/rc_yarp_wrapper.git

#Install Yarp
cd $ROBOT_CODE/yarp
git checkout devel
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$ROBOT_INSTALL -DCREATE_GUIS=ON -DCREATE_LIB_MATH=ON ../
make install -j5

#Install icub-main
cd $ROBOT_CODE/icub-main
git checkout devel
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$ROBOT_INSTALL -DENABLE_icubmod_cartesiancontrollerserver=ON -DENABLE_icubmod_cartesiancontrollerclient=ON -DENABLE_icubmod_gazecontrollerclient=ON ../
make install -j5

#Install icub-contrib-common
cd $ROBOT_CODE/icub-contrib-common
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=$ROBOT_INSTALL ../
make install -j5

#Install icub-contrib-common
cd $ROBOT_CODE/kinect-wrapper
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=$ROBOT_INSTALL ../
make install -j5



