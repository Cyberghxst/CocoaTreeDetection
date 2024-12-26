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

### Camera
For this project, a generic camera module was used. It has a Sony IMX219 sensor (8 megapixels)
You can buy it through [the following link](https://es.aliexpress.com/item/1005006297356747.html?spm=a2g0o.productlist.main.1.79d8XMx5XMx52a&algo_pvid=c9424126-9b67-4071-9412-fb38f46aff86&algo_exp_id=c9424126-9b67-4071-9412-fb38f46aff86-0&pdp_npi=4%40dis%21MXN%21278.51%21250.56%21%21%2113.55%2112.19%21%402103247417352518968927685e4528%2112000036658758852%21sea%21MX%210%21ABX&curPageLogUid=v0r4aV3c4Lyi&utparam-url=scene%3Asearch%7Cquery_from%3A).
This camera must be used with the `libcamera` libraries, so, with that in mind, YOU MUST USE `picamera2` since this lib is based on libcamera. otherwise, it wont work (even trying everything using raw opencv)
```bash
(kokoa) raspi@raspi:~/Documents/CocoaTreeDetection $ libcamera-hello --list-cameras
Available cameras
-----------------
0 : imx219 [3280x2464 10-bit RGGB] (/base/soc/i2c0mux/i2c@1/imx219@10)
    Modes: 'SRGGB10_CSI2P' : 640x480 [206.65 fps - (1000, 752)/1280x960 crop]
                             1640x1232 [41.85 fps - (0, 0)/3280x2464 crop]
                             1920x1080 [47.57 fps - (680, 692)/1920x1080 crop]
                             3280x2464 [21.19 fps - (0, 0)/3280x2464 crop]
           'SRGGB8' : 640x480 [206.65 fps - (1000, 752)/1280x960 crop]
                      1640x1232 [83.70 fps - (0, 0)/3280x2464 crop]
                      1920x1080 [47.57 fps - (680, 692)/1920x1080 crop]
                      3280x2464 [21.19 fps - (0, 0)/3280x2464 crop]
```

## Disclaimer
Any uncommented situation/error: try to google it, you will almost find out everything by seeing the whole internet
(this is how I solved all the errors I got) :)