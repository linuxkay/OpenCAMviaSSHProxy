# OpenCAMviaSSHProxy
This opens network cam stream at separated network though ssh proxy.
## Description
Let's say you are in WiFi network A 192.168.0.0 but your cam at WiFi B 192.168.1.0 network. You still can get access via ssh proxy if you have RaspberryPi3B+ connected Both WiFiA and WiFiB using Ethernet and Wlan. Thanks to Pi3B+ has 2 NICs by default.

# Demo
![Topology](https://raw.githubusercontent.com/wiki/linuxkay/OpenCAMviaSSHProxy/images/networkAplusB.gif)

## Overview

It opens HTTP CAM stream from another isolated network.

files

run_cam_via_yogurt_proxy.py
- Establish ssh proxy connection to Raspberry1B+ 

## VS. 


## Requirements
Linux
gnome-terminal
Firefox
ssh key login setup needs to be done.

## Usage

## Install

## Contribution

## Licence
[MIT]

## Author

[linuxkay](https://github.com/linuxkay)
