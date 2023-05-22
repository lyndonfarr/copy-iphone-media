# Python script for copying iPhone media to desktop on Linux Ubuntu 22.04

[Helpful Link](https://wuzhaojun.wordpress.com/2021/03/19/memo-of-backup-iphones-photos-in-ubuntu-20-04/)

### Requirements:
#### Software:
 - python3
#### Packages:
 - libimobiledevice6
 - libimobiledevice-utils
 - ifuse

### Installing Requirements:
```bash
sudo apt install libimobiledevice6 libimobiledevice-utils ifuse
```

### How to use:
```bash
idevicepair pair
sudo usbmuxd -z -f -v
ifuse ~/iphone
python3 /path/to/copyIphoneMedia.py /path/to/destination ~/iphone/DCIM/*/*
fusermount -u ~/iphone
idevicepair unpair
```

### Licences:
This is NOT licensed. Use at your own risk.

## BONUS: Copy and convert any .HEIC files to .jpg

### Requirements:
#### Packages:
 - libheif-examples

### Installing Requirements:
```bash
sudo apt-get install libheif-examples
```

### Converting .HEIC files:
```bash
cd /path/to/directory
for file in *.HEIC; do heif-convert "$file" "${file/%.HEIC/.jpg}"; done
```