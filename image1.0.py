import cv2

img = cv2.imread ('C:\\Users\\hp\\Pictures\\bhaia1.jpg',1)
resized =cv2.resize(img,(800,800))
cv2.imshow("Legend",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
