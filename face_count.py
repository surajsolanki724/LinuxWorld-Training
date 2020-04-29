import cv2

face_detect = cv2.CascadeClassifier("/root/Desktop/jupyter/haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)

while True:
	ret,photo=cap.read()
	faces = face_detect.detectMultiScale(photo)
	cv2.imshow("hi",photo)
	if cv2.waitKey(1)==13:
		break

print("no of student are: ",end='')
print(len(faces))
        
cv2.destroyAllWindows()
cap.release()

    
