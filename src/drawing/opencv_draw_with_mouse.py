#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

##############################################################################
# FUNCTION
###############################################################################


def draw_circle(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, center=(x, y), radius=50, color=(0, 255, 0), thickness=-1)

    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, center=(x, y), radius=20, color=(255, 0, 0), thickness=-1)


cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_circle)


###############################################################################
# SHOWING IMAGE WITH OpenCV
###############################################################################

# Depending on the 'dtype' value, image's base color decided. With 'dtype=int8',
# base image looks like gray color. Without the data type, we can see true colors.
image = np.zeros((512, 512, 3))

while True:

    cv2.imshow('my_drawing', image)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()