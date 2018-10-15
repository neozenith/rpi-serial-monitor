#! /usr/bin/bash

export MY_IP=`/usr/bin/sudo /sbin/ifconfig | grep "inet " | grep -v 127.0.0.1 | cut -d " " -f10`
/usr/bin/env python3 /home/pi/projects/rpi-serial-monitor/visualise.py "$MY_IP"
