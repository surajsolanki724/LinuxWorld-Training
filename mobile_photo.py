#!/usr/bin/python36
#for direct execution
import requests
import cv2
import numpy as np


url ="http://192.168.43.1:8080/shot.jpg"
geturl=requests.get(url)

#url photo python load
photoweb=geturl.content

#photo binary (bytes) into bytearray
photobyte=bytearray(photoweb)

# bytearray convert into id numpy
image=np.array(photobyte)

#id convert into 3D : cv2 support
frame=cv2.imdecode(image,-1)

cv2.imwrite("/root/Desktop/suraj.jpg",frame)

#image show
cv2.imshow("hi",frame)
cv2.waitKey()
cv2.destroyAllWindows()
