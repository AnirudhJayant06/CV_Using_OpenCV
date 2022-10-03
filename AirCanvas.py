import cv2
import numpy as np

# Defining width & height of the video
video_width = 640
video_height = 480

cap = cv2.VideoCapture(0)

cap.set(3, video_width)
cap.set(4, video_height)

# Setting brightness of the video
cap.set(10, 180)

# HSV values used for masking - Parrot, Orange, Green
my_pens = [[23, 72, 75, 255, 97, 255],
           [0, 9, 171, 255, 94, 255],
           [78, 104, 75, 211, 64, 255]]

# BGR Values of pen pointers - Parrot, Orange & Green
my_colors = [
    [51, 255, 204],
    [0, 102, 255],
    [102, 153, 51]
]

# x, y, colorID
my_points = []


def findColors(img, my_pens, my_colors):
    HSV_Img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    """
    This counter is helpful when there are multiple pens at a time because let say 1st pen appear -> count becomes '1'.
    Then, 2nd pen appear -> count becomes '2' and , then, 3rd pen appears so count becomes '3'
    """
    count = 0

    """
    Whenever new points are identified, it 'll be added to this list.
    This initializes an empty list so that old points get deleted every time this function is called i.e. 
    whenever a new pen is introduced at the screen
    """
    new_points = []


    for colors in my_pens:
        # H_min, S_min & V_min
        lower = np.array(colors[0:6:2])
        # H_max, S_max & V_max
        upper = np.array(colors[1:7:2])
        mask = cv2.inRange(HSV_Img, lower, upper)

        # Getting points/ coordinates of the pen pointer
        x, y = getContours(mask, img_result)

        #Drawing circle at the extratced points of the same color as of the marker
        cv2.circle(img_result, (x, y), 10, my_colors[count], cv2.FILLED)

        #This is to make sure that [0,0] coordinates (i.e. when marker is not on the screen) shouldn't get
        #added to the list of points which we are going to draw
        #This adds new points to the list of 'my_points'
        if x != 0 and y != 0:
            # Adding points of the list with colorID
            new_points.append([x, y, count])
        count += 1
    # This returns it as a list
    #print("New Points: ", new_points)
    return new_points


def getContours(func_img, fun_contour):
    # Our contours got saved in 'contours'
    contours, hierarchy = cv2.findContours(func_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    # TO look into each individual contour
    for cnt in contours:
        area = cv2.contourArea(cnt)

        # Calculating the area of contours so that small (error) boxes shouldn't get included
        if area > 500:

            #Drawing contours
            # Negative value (i.e. -1) means draw all contours
            # cv2.drawContours(fun_contour, cnt,-1, (255,0,0),3)

            # Calculating the perimeters of all contours
            peri = cv2.arcLength(cnt, True)

            # Calculating the approximate no. of points of each contour
            approx_points = cv2.approxPolyDP(cnt, 0.01 * peri, True)

            # Getting coordinates and width & height of the rectangle to be drawn
            x, y, w, h = cv2.boundingRect(approx_points)
    return x + w // 2, y


# Drawing circles on canvas
def drawOnCanvas(my_points, my_colors):
    for points in my_points:
        print("Points on canvas: ",points)
        cv2.circle(img_result, (points[0], points[1]),10, my_colors[points[2]],cv2.FILLED)


# Displaying a video - It 'll play the video frame by frame
while True:
    # This loads each frame into an img
    Success, temp_img = cap.read()
    # Flipping the captured video
    img = cv2.flip(temp_img, 1)
    img_result = img.copy()
    # Reading color pens
    new_points = findColors(img, my_pens, my_colors)
    # We are adding new points to our list of points 'my_points'
    if len(new_points) != 0:
        for points in new_points:
            my_points.append(points)

    """
    Why we draw using 'my_points' & not 'new_points'?
    -> Because new points are the points of the pen pointer & they keep changing with the pens. The old values gets
     deleted everytime you move your pens.So, even if we draw these new points, they 'll get erased as soon as we move
      our pen. So, it gives a feeling that it's not drawing. Whereas if we draw 'my_points', which gets updated (appended)
      everytime we move our pens as well as keeping the old points, we are able to see all the points on the screen as
       it has all the old points in the list.  
    """
    if len(my_points)!=0:
        drawOnCanvas(my_points,my_colors)
    print("New Points: ",new_points)
    print("My Points: ",my_points)

    # Inseting text on video
    cv2.putText(img_result,"Pens - Parrot, Orange & Green", ((video_width // 2) - 150, 30), cv2.FONT_HERSHEY_PLAIN,
                1, (0, 0, 255), 2)
    cv2.putText(img_result, "Press S to stop ", ((video_width // 2) - 100, 60), cv2.FONT_HERSHEY_PLAIN,
                1, (0, 0, 255), 2)
    # Displaying each frame
    cv2.imshow("Video", img_result)

    # This defines the waiting time & sets exit key to 's'
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
