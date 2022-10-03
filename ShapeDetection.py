import cv2
import numpy as np

#Shape Detection/ Contours

# RETR_EXTERNAL -> It retrieves the external contour (details/ corners)
# CHAIN_APPROX_NONE -> It 'll not approx (reduce) the corners found
def getContours(func_img, fun_contour):
    #Our contours got saved in 'contours'
    contours, hierarchy = cv2.findContours(func_img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #TO look into each individual contour
    for cnt in contours:
        #Drawing contours
        #Negative value (i.e. -1) means draw all contours
        cv2.drawContours(fun_contour, cnt,-1, (255,0,0),3)
        #Calculating the perimeters of all contours
        peri = cv2.arcLength(cnt,True)
        #Calculating the approximate no. of points of each contour
        approx_points = cv2.approxPolyDP(cnt,0.01*peri,True)
        #Printing coordinates of each countour
        print(approx_points)
        #Accessing the shape of a contour by looking at the no. of points of a contour
        no_of_coord = len(approx_points)
        #print(len(approx_points))

        if no_of_coord == 3:
            object_type ='Triangle'
        elif no_of_coord ==4:
            #Calculating the ratio of width & height
            aspect_ratio = w/float(h)
            #Formatting float value to upto 2 digits
            format_float = "{:.2f}".format(aspect_ratio)
            if aspect_ratio > 0.80 and aspect_ratio < 1.50:
                object_type = "Rhombus" + str(format_float)
            else:
                object_type = "Rectangle" + str(format_float)
        elif no_of_coord == 5:
            object_type = "Pentagon" + str(no_of_coord)
        elif no_of_coord == 6:
            object_type = "Hexagon"
        elif no_of_coord == 7:
            object_type = "Septagon"
        elif no_of_coord == 8:
            object_type = "Octagon"
        elif no_of_coord >7 and no_of_coord <11:
            object_type = 'Other'
        else:
            object_type = "Circle" + str(no_of_coord)

        #Getting coordinates and width & height of the rectangle to be drawn
        x, y, w, h = cv2.boundingRect(approx_points)
        #Drawing rectangles
        cv2.rectangle(fun_contour,(x,y),(x+w,y+h),(255,0,0),2)
        #Putting text for each shape
        cv2.putText(fun_contour,object_type,(x+(w//2),y+h+30),
                    cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.5,(0,0,0),1)


img = cv2.imread('Resources/Shapes.jpg')
contour_img = img.copy()

img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_grey,(7,7),1)
img_canny = cv2.Canny(img_blur,50,60)

#Calling function to get contours & draw rectangle around them
getContours(img_canny, contour_img)

cv2.imshow("Original Image",img)
# cv2.imshow("Grey Image",img_grey)
# cv2.imshow("Blur Image",img_blur)
cv2.imshow("Canny Image",img_canny)
cv2.imshow("Contoured Image",contour_img)

cv2.waitKey(0)
