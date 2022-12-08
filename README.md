# AirCanvas

First, I detected the HSV values of my highlighter color pens using a different project and hardcode these values along with their BGR values. Then, I captured a frame using the webcam and call ‘findColors’ method (which calls ‘getContours’ method) which returns the coordinates of pen pointer detected. Then, these new points ‘ll be added to ‘my_points’ list and, finally, ‘drawOnCanvas’ method was called to draw circle on the captured frame.
