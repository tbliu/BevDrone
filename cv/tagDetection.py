import numpy as np
import cv2
import cv2.aruco as aruco
import generate as g
import subprocess

"""
Takes a single image an determines whether an aruco tag is in the frame
"""

aruco_dict = g.generate()
parameters = aruco.DetectorParameters_create()
while True:
    # take image and load it in OpenCV
    subprocess.call(["fswebcam", "-S", "2", "image.jpg"])
    img = cv2.imread("./image.jpg") 

    # find corners and draw circle around center if aruco tag detected
    corners, ids, rejectedImgPoints = aruco.detectMarkers(img, aruco_dict, parameters=parameters)
    if corners != []:
        tagCorner = corners[0][0]
        uL = tagCorner[0]
        bR = tagCorner[2]
        newX = (uL[0] + bR[0]) / 2
        newY = (uL[1] + bR[1]) / 2
        center = (int(newX), int(newY)) 
    
        img = aruco.drawDetectedMarkers(img, corners)
        img = cv2.circle(img, center, 5, 0)
        
    cv2.imshow('Detected Corners', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
print("Shutting down")

