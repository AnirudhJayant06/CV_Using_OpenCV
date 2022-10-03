import cv2

# Input Image path
img = cv2.imread('Resources/Faces.jpg')
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Initialize Cascade
Face_Cascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
#Detecting Face
faces = Face_Cascade.detectMultiScale(img_grey,1.1,2)

#Drawing rectangle around detected faces
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Original Image",img)
cv2.waitKey(0)