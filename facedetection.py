import cv2

face_Cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread ('C:\\Users\\hp\\Pictures\\bhaia1.jpg')
gray_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces= face_Cascade.detectMultiScale(gray_img,scaleFactor =1.5, minNeighbors=2)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img=cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)
    resized=cv2.resize(img, (1000,1000))

    cv2.imshow("gray",resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows();


