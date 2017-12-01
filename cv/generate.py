import numpy as np
import cv2
import cv2.aruco as aruco

"""
Generates an aruco tag and saves it
"""

# generate the aruco tag
def generate():
    d = aruco.Dictionary_get(aruco.DICT_4X4_100)

    # display the aruco tag
    img = aruco.drawMarker(d, 1, 2000)
    cv2.imwrite("../img/aruco.jpg", img)
    cv2.imshow('Aruco tag', img)

    # clean up
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.waitkey(0)
        cv2.destroyAllWindows()
        return d
generate()
