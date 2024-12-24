# Cocoa Tree Detection
Implementation of a YOLOv8 model to detect cocoa trees using Python, CustomTkinter, OpenCV and PiCamera2 on a Raspberry Pi 4 Model B.

## Project Information
### Board
The board used for this project was the Raspberry Pi 4 Model B (4GB) with the next OS features.
```bash
raspi@raspi:~ $ neofetch

       _,met$$$$$gg.          raspi@raspi 
    ,g$$$$$$$$$$$$$$$P.       ----------- 
  ,g$$P"     """Y$$.".        OS: Debian GNU/Linux 12 (bookworm) aarch64 
 ,$$P'              `$$$.     Host: Raspberry Pi 4 Model B Rev 1.5 
',$$P       ,ggs.     `$$b:   Kernel: 6.6.62+rpt-rpi-v8 
`d$$'     ,$P"'   .    $$$    Uptime: 3 hours, 29 mins 
 $$P      d$'     ,    $$P    Packages: 1740 (dpkg) 
 $$:      $$.   -    ,d$$'    Shell: bash 5.2.15 
 $$;      Y$b._   _,d$P'      Resolution: 1920x1080 
 Y$$.    `.`"Y$$$$P"'         DE: labwc:wlroots 
 `$$b      "-.__              Theme: PiXflat [GTK3] 
  `Y$$                        Icons: PiXflat [GTK3] 
   `Y$$.                      Terminal: lxterminal 
     `$$b.                    Terminal Font: Monospace 10 
       `Y$$b.                 CPU: (4) @ 1.800GHz 
          `"Y$b._             Memory: 1439MiB / 3742MiB 
              `"""
```
The usage of a 64-bit OS has an important reason: it has less problems with the needed python libraries.
(discovering this was really a pain :/)

### Python Version
The python version used for this project was: 3.11.2 (Raspberry Pi OS built-in [no need for extra installations])
```bash
raspi@raspi:~ $ python --version
Python 3.11.2
```

### Python Libraries
In this part I am showing the used libs and its versions.
```bash
(kokoa) raspi@raspi:~ $ pip show opencv-python
Name: opencv-python
Version: 4.10.0.84
Summary: Wrapper package for OpenCV python bindings.
Home-page: https://github.com/opencv/opencv-python
Author: 
Author-email: 
License: Apache 2.0
Location: /home/raspi/kokoa/lib/python3.11/site-packages
Requires: numpy, numpy, numpy, numpy, numpy, numpy
Required-by: ultralytics


(kokoa) raspi@raspi:~ $ pip show ultralytics
Name: ultralytics
Version: 8.3.54
Summary: Ultralytics YOLO 🚀 for SOTA object detection, multi-object tracking, instance segmentation, pose estimation and image classification.
Home-page: 
Author: 
Author-email: Glenn Jocher <glenn.jocher@ultralytics.com>, Jing Qiu <jing.qiu@ultralytics.com>
License: AGPL-3.0
Location: /home/raspi/kokoa/lib/python3.11/site-packages
Requires: matplotlib, numpy, opencv-python, pandas, pillow, psutil, py-cpuinfo, pyyaml, requests, scipy, seaborn, torch, torchvision, tqdm, ultralytics-thop


(kokoa) raspi@raspi:~ $ pip show customtkinter
Name: customtkinter
Version: 5.2.2
Summary: Create modern looking GUIs with Python
Home-page: https://customtkinter.tomschimansky.com
Author: Tom Schimansky
Author-email: 
License: Creative Commons Zero v1.0 Universal
Location: /home/raspi/kokoa/lib/python3.11/site-packages
Requires: darkdetect, packaging


(kokoa) raspi@raspi:~ $ pip show picamera2
Name: picamera2
Version: 0.3.23
Summary: The libcamera-based Python interface to Raspberry Pi cameras, based on the original Picamera library
Home-page: https://github.com/RaspberryPi/picamera2
Author: Raspberry Pi & Raspberry Pi Foundation
Author-email: picamera2@raspberrypi.com
License: BSD 2-Clause License
Location: /usr/lib/python3/dist-packages
```

## Disclaimer
Any uncommented situation error / situation: try to google, you will almost find out everything by seeing the whole internet
(this is how I solved all the errors I got) :)