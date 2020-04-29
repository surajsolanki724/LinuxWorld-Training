import requests
import cv2
import numpy as np
while True:
   
    url1="http://192.168.43.1:8080/shot.jpg"
    url2="http://192.168.43.228:8080/shot.jpg"
    url3="http://192.168.43.134:8080/shot.jpg"
   

    geturl1=requests.get(url1)
    geturl2=requests.get(url2)
    geturl3=requests.get(url3)

    photoweb1=geturl1.content
    photoweb2=geturl2.content
    photoweb3=geturl3.content
    
    photobyte1=bytearray(photoweb1)
    photobyte2=bytearray(photoweb2)
    photobyte3=bytearray(photoweb3)


    image1=np.array(photobyte1)
    image2=np.array(photobyte2)
    image3=np.array(photobyte3)

    frame1=cv2.imdecode(image1,-1)
    frame2=cv2.imdecode(image2,-1)
    frame3=cv2.imdecode(image3,-1)
    
    resize=cv2.resize(frame2,(300,300))
    resize1=cv2.resize(frame3,(300,300))

    frame1[0:300,0:300]=resize
    frame1[300:600,300:600]=resize1    
    cv2.imshow("hello",frame1)
    if cv2.waitKey(1) == 13:
        break
cv2.destroyAllWindows()
