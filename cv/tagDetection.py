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
    # take image and load/process it in opencv
    subprocess.call(["fswebcam", "image.jpg"])
    img = cv2.imread("./image.jpg") 
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = img

    # load aruco tags
#    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)
#    parameters = aruco.DetectorParameters_create()

    # find corners of aruco tags and draw axes at center of each tag detected
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    if corners != []:
        tagCorner = corners[0][0]
        uL = tagCorner[0]
        bR = tagCorner[2]
        newX = (uL[0] + bR[0]) / 2
        newY = (uL[1] + bR[1]) / 2
        center = (int(newX), int(newY)) 
    
        gray = aruco.drawDetectedMarkers(gray, corners)
        gray = cv2.circle(gray, center, 5, 0)
        
    cv2.imshow('Detected Corners', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
print("Shutting down")

