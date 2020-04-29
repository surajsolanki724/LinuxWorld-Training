#!/usr/bin/python36
#for direct execution



import cv2
cap=cv2.VideoCapture(0)
ret,photo=cap.read()
cv2.imwrite("/root/Desktop/suraj.png",photo)
cv2.imshow('j',photo)
cv2.waitKey()
cv2.destroyAllWindows()
cap.release()

