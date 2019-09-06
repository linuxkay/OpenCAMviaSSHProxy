# OpenCAMviaSSHProxy
This opens network cam stream at separated network though ssh proxy.
## Description
Let's say you are in WiFi network A 192.168.0.0 but your cam at WiFi B 192.168.1.0 network. You still can get access via ssh proxy if you have RaspberryPi3B+ connected Both WiFiA and WiFiB using Ethernet and Wlan. Thanks to Pi3B+ has 2 NICs by default.

# Demo in Animation
![Topology](https://raw.githubusercontent.com/wiki/linuxkay/OpenCAMviaSSHProxy/images/networkAplusB.gif)

## Overview

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
python3 run_cam_via_ssh_proxy.py

Best to put avobe command in keyboard shorcut. Then you can run in by tapping just 1 key.
![KeyboardShotcutCamProxy](https://raw.githubusercontent.com/wiki/linuxkay/OpenCAMviaSSHProxy/images/keyboard-shotcut-forCamproxy.jpeg)


## Install

## Contribution

## Licence
[MIT]

## Author

[linuxkay](https://github.com/linuxkay)
