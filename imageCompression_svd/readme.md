Usage: 
```
python3 imageCompression.py -filename -n
```
e.g.
```
python3 imageCompression.py example.png 100
```
Requirement: python 3.7 or above numpy installed Pillow installed.  
To install type 
``` 
& pip3 numpy Pillow
```
in terminal  
n is the number of eigenvalues you take. The quality of image depends on the value of n.
n is between 0 to 256.  
Purpose:  
This program will take in an image and spit out a image which is compressed using svd. It will show the ratio of compression.

