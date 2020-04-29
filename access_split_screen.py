import cv2
import subprocess

cap = cv2.VideoCapture(0)

while True:
    ret , photo = cap.read()
    resize_vid = cv2.resize(photo, None , fx=0.5 , fy = 0.5 , interpolation = cv2.INTER_AREA)
    photo[0:240,0:320] = resize_vid
    subprocess.getoutput("ret , photo1 = cap.read()")
    subprocess.getoutput("resize_vid1 = cv2.resize(photo1, None , fx=0.5 , fy = 0.5 , interpolation = cv2.INTER_AREA)")
    subprocess.getoutput("")
    cv2.imshow("MyVideoCam",photo)
    if cv2.waitKey(1) == 13:
        break

cv2.destroyAllWindows()
cap.release()
