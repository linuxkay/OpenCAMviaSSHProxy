# OpenCAMviaSSHProxy
This opens network cam stream at separated network though ssh proxy.
## Description
Let's say you have 2 WiFi networks such as A and B. WiFi A is for your regular use browsing, facebooking and etc. WiFi B is for Local Network CAM. You don't want CAM to be connected outside of LAN. So in this case, WiFi B and CAM is completely isoated from WAN. However, You still can get access via ssh proxy if you have RaspberryPi3B+ connected Both WiFii A and WiFi B just using Ethernet and Wlan. Thanks to Pi3B+ has 2 NICs by default. SSH proxy magic does this for you.

# Demo in Animation
![DemoOpenCamviaProxy](https://raw.githubusercontent.com/wiki/linuxkay/OpenCAMviaSSHProxy/images/openCamviaProxy-demo.gif)

## Overview
![Topology](https://raw.githubusercontent.com/wiki/linuxkay/OpenCAMviaSSHProxy/images/networkAplusB.gif)

It opens HTTP CAM stream from another isolated network.

files

run_cam_via_ssh_proxy.py
- Establish ssh proxy connection to Raspberry1B+ 

## VS. 


## Requirements
gnome-terminal

Firefox

ssh key login authentication.

## Usage
Simpy run py file in terminal.

$ python3 run_cam_via_ssh_proxy.py

Best to put avobe command in keyboard shorcut. Then you can run in by tapping just 1 key.
![KeyboardShotcutCamProxy](https://raw.githubusercontent.com/wiki/linuxkay/OpenCAMviaSSHProxy/images/keyboard-shotcut-forCamproxy.jpeg)


## Install

## Contribution

## Licence
[MIT]

## Author

[linuxkay](https://github.com/linuxkay)
