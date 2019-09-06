#!/usr/bin/env/python3.6
import os

os.system('gnome-terminal -- ssh proxy-yogurt')
os.system('firefox -P "proxy-to-yogurt" "http://192.168.0.100/cgi-bin/hi3510/snap.cgi?&-getstream"')
