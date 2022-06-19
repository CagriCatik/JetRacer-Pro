<div align="center">

  <img src="https://www.waveshare.com/media/catalog/product/cache/1/image/800x800/9df78eab33525d08d6e5fb8d27136e95/j/e/jetracer-pro-ai-kit-7.jpg" alt="logo" width="200" height="auto" />
  <h1>JetRacer Pro</h1>
  
  <p>
    JetRacer is an autonomous AI racecar using NVIDIA Jetson Nano
  </p>

  
<!-- Badges -->
<p>
  <a href="https://github.com/CagriCatik/JetRacerPro/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/CagriCatik/JetRacerPro" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/CagriCatik/JetRacerPro" alt="last update" />
  </a>
  <a href="https://github.com/CagriCatik/JetRacerPro/network/members">
    <img src="https://img.shields.io/github/forks/CagriCatik/JetRacerPro" alt="forks" />
  </a>
  <a href="https://github.com/CagriCatik/JetRacerPro/stargazers">
    <img src="https://img.shields.io/github/stars/CagriCatik/JetRacerPro" alt="stars" />
  </a>
  <a href="https://github.com/CagriCatik/JetRacerPro/issues/">
    <img src="https://img.shields.io/github/issues/CagriCatik/JetRacerPro" alt="open issues" />
  </a>
  <a href="https://github.com/CagriCatik/JetRacerPro/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/CagriCatik/JetRacerPro.svg" alt="license" />
  </a>
</p>
   
<h4>
    <a href="https://github.com/CagriCatik/JetRacerPro/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/CagriCatik/JetRacerPro">Documentation</a>
  <span> · </span>
    <a href="https://github.com/CagriCatik/JetRacerPro/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/CagriCatik/JetRacerPro/issues/">Request Feature</a>
  </h4>
</div>

<br />

<!-- Table of Contents -->
# Table of Contents

- [Table of Contents](#table-of-contents)
  - [About the Project](#about-the-project)
  - [Examples](#examples)
  - [Robot Operating System](#robot-operating-system)
    - [ROS Quick Installation on Jetson](#ros-quick-installation-on-jetson)
    - [Running RViz Visualization Tool](#running-rviz-visualization-tool)
  - [Virtual Network Computing](#virtual-network-computing)
    - [Setup VNC server on the **JetRacerPro**](#setup-vnc-server-on-the-jetracerpro)
    - [Connecting to VNC service from **Laptop**](#connecting-to-vnc-service-from-laptop)
  - [Roadmap](#roadmap)
  - [Acknowledgements](#acknowledgements)
  

<!-- About the Project -->
## About the Project

- To get started with JetRacer, follow these steps
  - [My BOM for Jetracer Pro](docs/latrax/bill_of_materials.md)
  - [Hardware setup]([docs/latrax/hardware_setup.md](https://www.waveshare.com/w/upload/f/fa/Jetracer_pro_Assembly_EN.pdf))
  - [Software setup](docs/software_setup.md)


<div align="center"> 
  <img src="https://www.waveshare.com/img/devkit/JetRacer-Pro-AI-Kit/JetRacer-Pro-AI-Kit-details-11.jpg" alt="screenshot" width="400" height="auto"/>
</div>



<!-- examples -->
## Examples

- JetRacer comes with a couple examples to get you up and running.  
- The examples are in the format of Jupyter Notebooks, which are interactive documents which combine text, code, and visualization.  
- Once you've completed the notebooks, start tweaking them to create your own racing software!
- Learn more in the [examples](docs/examples.md).

<!-- ros -->
## Robot Operating System

This section covers all the steps needed for setting up JetRacer to run with ROS Melodic.

### ROS Quick Installation on Jetson

- Setup your sources.list
    
    ```sh
    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

    sudo apt update
    sudo apt install ros-melodic-desktop-full
    ```
- Set up your keys
    ```sh
    sudo apt install curl # if you haven't already installed curl
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
    ```

- Desktop-Full Install: ROS, rqt, rviz, robot-generic libraries, 2D/3D simulators and 2D/3D perception 

    ```sh    
    sudo apt update
    sudo apt install ros-melodic-desktop-full
    ```

- Environments setup
    ```sh
    echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
    source ~/.bashrc
    source /opt/ros/melodic/setup.bash
    ```
- Dependencies

    ```sh
    sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
    ```

- #TODO
    ```py
    pip install -r requirements.txt
    ```

- #TODO
    ```sh
   chmod +x install.sh 
  
     ```

- #TODO    

    ```sh

    ```

### Running RViz Visualization Tool

Simple robot model is developed in URDF being built with Xacro. This model is then being parsed and visualized in RViz. To launch the RViz example, open a new terminal and enter the following command:

```sh
roslaunch xxx rviz.launch
```

<!-- vnc -->
## Virtual Network Computing

- VNC enables you to control your Jetson developer kit from another computer on the same network, by viewing and interacting with the desktop of the developer kit from the other computer. Your Jetson developer kit and the other computer need to be on the same network. A fairly fast network connection is needed. Slower connections will degrade the desktop interaction experience.

### Setup VNC server on the **JetRacerPro**

- Enable the VNC server to start each time you log in

    ```
    cd /usr/lib/systemd/user/graphical-session.target.wants
    sudo ln -s ../vino-server.service ./. 
    ```

- Configure the VNC server
  
    ```
    gsettings set org.gnome.Vino prompt-enabled false
    gsettings set org.gnome.Vino require-encryption false
    ```

- Set a password to access the VNC server
  
  ```
  # Replace thepassword with your desired password 
  gsettings set org.gnome.Vino authentication-methods "['vnc']" 
  gsettings set org.gnome.Vino vnc-password (echo -n 'JetRacerPro'|base64)
  ```

- Reboot the system so that the settings take effect

    ```
    sudo reboot
    ```

### Connecting to VNC service from **Laptop**

- Install gvncviewer by executing following commands:

    ```
    sudo apt update
    sudo apt install gvncviewer
    ```

- Launch gvncviewer

    ```
    gvncviewer 
    ```

- If you have configured the VNC server for authentication, provide the VNC password


<!-- Roadmap -->
## Roadmap

- [ ] Configure VNC
- [ ] Build your own jetson-image
- [ ] Optimize and maintain main-README and another READMEs of repo 
- [ ] Test quick ros installation
- [ ] Add own pictures
- [ ] Write a bash script for installation of varios apps
- [ ] Buy a 3D-Printer
- [ ] [Install IntelRealSense]()
- [ ] [ROS Camera Calibration](http://wiki.ros.org/camera_calibration/Tutorials/MonocularCalibration)





<!-- Acknowledgments -->
## Acknowledgements

Useful resources and libraries that used in this project:

- [Jetpack](https://github.com/NVIDIA-AI-IOT/jetracer/blob/master/docs/software_setup.md#latest-release--but-not-yet-fully-verified--) JetCard Image
- [JetBot](http://github.com/NVIDIA-AI-IOT/jetbot) - Educational AI robot based on NVIDIA Jetson Nano
- [JetCam](http://github.com/NVIDIA-AI-IOT/jetcam) - Easy to use Python camera interface for NVIDIA Jetson
- [JetCard](http://github.com/NVIDIA-AI-IOT/jetcard) - SD card image for web programming AI projects with NVIDIA Jetson Nano
- [torch2trt](http://github.com/NVIDIA-AI-IOT/torch2trt) - Easy to use PyTorch to TensorRT converter
- [ROS Single Line Installation](https://robocademy.com/2020/05/23/getting-started-with-new-ros-noetic-ninjemys/) - Quick install 
- [ROS on JetRacer-Pro](https://tutorial.cytron.io/2021/04/16/getting-started-with-robotic-operating-system-ros-and-jetracer-ai-kit/) - Setup for JetRacerPro
- [ROS Wrapper for Intel® RealSense](https://github.com/IntelRealSense/realsense-ros)
- [VNC with Jetson Nano](https://tutorial.cytron.io/2022/01/20/vnc-with-nvidia-jetson-nano-2gb-b01/) - Virtual Network Computing for JetRacerPro
 - [Readme Template](https://github.com/othneildrew/Best-README-Template)