import requests
import cv2
import numpy as np


while True:

	# url address
	url1 = "http://192.168.43.60:8080/shot.jpg"
	url2 = "http://192.168.43.60:8080/shot.jpg"
	url3 = "http://192.168.43.60:8080/shot.jpg"
	url4 = "http://192.168.43.60:8080/shot.jpg"

	# url connect
	geturl1 = requests.get(url1)
	geturl2 = requests.get(url2)
	geturl3 = requests.get(url3)
	geturl4 = requests.get(url4)

	# get photo access
	photoweb1 = geturl1.content
	photoweb2 = geturl2.content
	photoweb3 = geturl3.content
	photoweb4 = geturl4.content

	# convet byte to bytearray
	photobyte1 = bytearray(photoweb1)
	photobyte2 = bytearray(photoweb2)
	photobyte3 = bytearray(photoweb3)
	photobyte4 = bytearray(photoweb4)

	# convert bytearray to 1d array
	image1 = np.array(photobyte1)
	image2 = np.array(photobyte2)
	image3 = np.array(photobyte3)
	image4 = np.array(photobyte4)

	# convert 1d to 3d array
	frame1 = cv2.imdecode(image1,-1)
	resize_vid = cv2.resize(frame1 , (1000,600) ,interpolation = cv2.INTER_AREA)
	
	resize_vid1 = cv2.resize(frame1 , (500,300) ,interpolation = cv2.INTER_AREA)
	frame2 = cv2.imdecode(image2,-1)
	resize_vid2 = cv2.resize(frame2 , (500,300) ,interpolation = cv2.INTER_AREA)
	frame3 = cv2.imdecode(image3,-1)
	resize_vid3 = cv2.resize(frame3 , (500,300) ,interpolation = cv2.INTER_AREA)
	frame4 = cv2.imdecode(image4,-1)
	resize_vid4 = cv2.resize(frame4 , (500,300) ,interpolation = cv2.INTER_AREA)
	
	resize_vid[0:300,0:500] = resize_vid1
	resize_vid[300:600,0:500] = resize_vid2
	resize_vid[0:300,500:1000] = resize_vid3
	resize_vid[300:600,500:1000] = resize_vid4
	
	cv2.imshow("MyMobileVideoCam",resize_vid)
	if cv2.waitKey(1) == 13:
		break

cv2.destroyAllWindows()
print("CAMERA'S CLOSED")


