
import requests
import cv2
import numpy as np


url ="http://100.107.5.216:8080/shot.jpg"
while True:
    geturl=requests.get(url)
    photoweb=geturl.content
    photobyte=bytearray(photoweb)
    image=np.array(photobyte)
    frame=cv2.imdecode(image,-1)
    cv2.imshow("hi",frame)
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()
