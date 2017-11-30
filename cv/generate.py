import numpy as np
import cv2
import cv2.aruco as aruco

"""
Generates an aruco tag and saves it
"""

# generate the aruco tag
d = aruco.Dictionary_get(aruco.DICT_4X4_250)
print(d)

# display the aruco tag
img = aruco.drawMarker(d, 2, 700)
cv2.imwrite("../img/aruco.jpg", img)
cv2.imshow('Aruco tag', img)

# clean up
cv2.waitkey(0)
cv2.destroyAllWindows()
