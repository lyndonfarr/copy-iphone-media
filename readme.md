# Python script for copying iPhone media to desktop on Linux Ubuntu 22.04

### Requirements:
###### Software:
python3
###### Packages:
libimobiledevice6 1libimobiledevice-utils 2ifuse

### Installing Requirements:
sudo apt install libimobiledevice6 libimobiledevice-utils ifuse

### How to use:
idevicepair pair 1sudo usbmuxd -z -f -v 2ifuse ~/iphone 3python3 /path/to/copyIphoneMedia.py /path/to/destination ~/iphone/DCIM/*/* 4fusermount -u ~/iphone 5idevicepair unpair

### Helpful Link:
[Link](https://wuzhaojun.wordpress.com/2021/03/19/memo-of-backup-iphones-photos-in-ubuntu-20-04/)