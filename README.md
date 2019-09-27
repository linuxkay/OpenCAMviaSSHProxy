# OpenCAMviaSSHProxy
This opens network cam stream at separated network though ssh proxy.
## Description
Let's say you have 2 WiFi networks such as A and B. WiFi A is for your regular use browsing, facebooking and etc. WiFi B is for Local Network CAM. You don't want CAM to be connected outside of LAN. So in this case, WiFi B and CAM is completely isoated from WAN. However, You still can get access via ssh proxy if you have RaspberryPi3B+ connected Both WiFii A and WiFi B just using Ethernet and Wlan. Thanks to Pi3B+ has 2 NICs by default. SSH proxy magic does this for you.

# Demo in Animation
![DemoOpenCamviaProxy](https://raw.githubusercontent.com/wiki/linuxkay/OpenCAMviaSSHProxy/images/openCamviaProxy-demo.gif)

## Overview
Network topology looks like following
![Topology](https://raw.githubusercontent.com/wiki/linuxkay/OpenCAMviaSSHProxy/images/networkAplusB.gif)

So request ssh proxy first and then get http cam stream through ssh tunnel.

files

`run_cam_via_ssh_proxy.py`
- Establish ssh proxy connection to Raspberry1B+ 


## Requirements
gnome-terminal

Firefox

ssh key login authentication.

## Usage
Simpy run py file in terminal.

$ `python3 run_cam_via_ssh_proxy.py`

Best to put avobe command in keyboard shorcut. Then you can run in by tapping just 1 key.
![KeyboardShotcutCamProxy](https://raw.githubusercontent.com/wiki/linuxkay/OpenCAMviaSSHProxy/images/keyboard-shotcut-forCamproxy.jpeg)


## Install
Connect Raspberry Pi3B+ to WiFi A by ethernet cable and WiFi B using WiFi.

Now you have Raspberry Pi3B+ connected to 2 Networks.

Set up ssh passwordless authentication.

Edit `~/.ssh/config`
or create if it does not exist

Write

Host proxy-yogurt

        HostName IP address of pi3B+ given by WiFI A

        user pi

        port Specify Port number. 22 by default

        DynamicForward 9999

	RequestTTY no

	RemoteCommand cat

And save.
Credits to <a href="https://unix.stackexchange.com/questions/424183/what-is-the-ssh-config-corresponding-option-for-ssh-n">StackExchange: What is the .ssh/config corresponding option for ssh -N</a>
Create Firefox proxy profile by using following command

`firefox -ProfileManager`

name profile as you like, I named it proxy-to-yogurt. Keep it simple though.

Remeber the profile name. You need it later.

Go to preferences 

find Network settings

set as follows

![FireFoxsocksProxySettings](https://raw.githubusercontent.com/wiki/linuxkay/OpenCAMviaSSHProxy/images/socksproxy.jpeg)


Edit `run_can_via_ssh_proxy.py`

If you changed name of Host in `~/.ssh/config` then change line 4 to proxy-yogurt to whatever the name you name it on `~/.ssh/config` Host.

Edit line 5 `firefox -P "Profile you named in Firefox  profileManager"`


## Contribution

## Licence
[MIT]

## Author

[linuxkay](https://github.com/linuxkay)
