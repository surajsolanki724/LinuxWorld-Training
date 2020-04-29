#!/usr/bin/python36
print("hi")
  

import cv2
cap=cv2.VideoCapture(0)
ret,photo=cap.read()
cv2.imwrite("/root/Desktop/my.png",photo)

