#full face+resize face
import cv2

face_detect = cv2.CascadeClassifier("/root/Desktop/jupyter/haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)

while True:
    ret,photo=cap.read()
    faces = face_detect.detectMultiScale(photo)
    if faces is not ():
    
        x=faces[0][0]
        y=faces[0][1]
        w=faces[0][2]
        h=faces[0][3]
        #photo=cv2.rectangle(photo,(x,y),(x+w,y+h),(0,255,0),4)
        r_photo=photo[y-20:y+h+20,x-20:x+w+20]
        resize=cv2.resize(r_photo,(200,200))
        photo[0:200,0:200]=resize
    
    
    cv2.imshow("hi",photo)
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()
cap.release()
