# AirCanvas

Steps:

1. Hardcore the HSV values of highlighter pens along with their BGR values (These HSV values of highlighter color pens is detected using a different project).
2. Captured a frame using the webcam and call ‘findColors’ method (which calls ‘getContours’ method) which returns the coordinates of pen pointer detected.
3. These new points ‘ll be added to ‘my_points’ list
4. ‘drawOnCanvas’ method was called to draw circle on the captured frame.

Project Demo: https://drive.google.com/file/d/1430bVFAydB9dYfb3qguqAYvOJB3j2_Z8/view?usp=sharing

# Document Scanner

Steps:

1. Capture the frame containing the document using external webcam.
2. 'getEdges' function is called (which uses gaussian blur, canny, dialation and errosion to get all the edges) which returns an image with edges.
3. This image (image with edges) is passed onto an another function called 'getContours' which draws & return the biggest contour. 
4. 'getWarp' function is called which calls another function 'reorder' which 'll arrange all the four points in the right order and returns reordered points. 'getWarp' function 'll use the reordered points to crop the background from the image and rotate the image as per our requirement. It 'll return this cropped & rotated image.
5. 'rescaleImg' function is called to rescale the images so that we can place them side-by-side. 
6. Finally, 'combine2Images' function is called to combine all the 4 images and displayed as an output.

Project Demo: https://drive.google.com/file/d/1482qkEXQWHyGDW4eI1lyT2UgHmRmlw0g/view?usp=sharing
