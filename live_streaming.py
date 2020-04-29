import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,photo=cap.read()
    crop_photo=photo[150:350,250:450]
    photo[0:200,0:200]=crop_photo
    cv2.imshow("hi",photo)
    if cv2.waitKey(1)==13:
        break
    
cv2.destroyAllWindows()
cap.release()
