import cv2
import numpy as np
import cvui
import os


path = os.path.abspath(os.path.dirname(__file__))
src = cv2.imread(path + "/image/1.jpg")
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

cvui.init("opencv")
frame = np.zeros((800, 800, 3), np.uint8)
floatValue_min = [20.]
floatValue_max = [30.]
h_min = [20.]
h_max = [140.]
while True:
    frame[:] = (49, 52, 49)
    
    cvui.trackbar(frame, 10, 60, 300, h_min, 0, 179)
    cvui.trackbar(frame, 320, 60, 300, h_max, 0, 179)

    lower_blue = np.array([h_min[0], 90, 90])
    upper_blue = np.array([h_max[0], 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = ~mask
    dest = cv2.bitwise_and(src,src, mask= mask)
    cvui.image(frame, 20, 120, dest)

    cvui.update()
    cv2.imshow("opencv", frame)
    cv2.waitKey(20)
