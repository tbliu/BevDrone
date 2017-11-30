import numpy as np
import cv2
import cv2.aruco as aruco
import os

"""
Takes a single image an determines whether an aruco tag is in the frame
"""
while True:
    # take image and load/process it in opencv
    os.system("fswebcam -r 1280x720 --no-banner /home/pi/bevdrone/img/$frame.jpg") 
    gray = cv2.imread("../img/frame.jpg", 0) # load image in grayscale
    detected = 0

    # load aruco tags
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
    parameters =  aruco.DetectorParameters_create()

    # find corners of aruco tags and draw axes at center of each tag detected
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    if corners is not None:
        tagCorner = corners[0]
        uR = tagCorner[0]
        bL = tagCorner[2]
        newX = (uR.x + bL.x) / 2
        newY = (uR.y + bL.y) / 2
        center = (newX, newY) 
        gray = aruco.drawDetectedMarkers(gray, corners)
        cv2.circle(gray, center, 2, 0)
        detected = 1

    cv2.imshow('Detected Corners', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
print("Shutting down")

