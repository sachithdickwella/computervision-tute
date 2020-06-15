#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

#######################################################################################################################
# VARIABLES
#######################################################################################################################

# True while mouse button down, False, when mouse button up.
drawing = False
ix, iy = -1, -1

#######################################################################################################################
# Function
#######################################################################################################################


def draw_rectangle(event, x, y, flags, params):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 0), thickness=-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 0), thickness=-1)


cv2.namedWindow(winname='canvas')
cv2.setMouseCallback('canvas', draw_rectangle)

#######################################################################################################################
# Showing the image using OpenCV
#######################################################################################################################


img = np.zeros((512, 512, 3))

while True:

    cv2.imshow(winname='canvas', mat=img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
