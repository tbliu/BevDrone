import numpy as np
import cv2
import cv2.aruco as aruco

"""
Takes a single image an determines whether an aruco tag is in the frame
"""

cap = cv2.VideoCapture(0)
detected = 0
# get current frame and convert to grayscale
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
parameters =  aruco.DetectorParameters_create()

# find corners of aruco tags
corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

if corners is not None:
    detected = 1
# for debugging:
"""
print(corners)

gray = aruco.drawDetectedMarkers(gray, corners)

cv2.imshow('frame', gray)
"""
cap.release()
cv2.destroyAllWindows()
return detected
