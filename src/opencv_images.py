#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

img = cv2.imread('../notebooks/DATA/00-puppy.jpg')

while True:
    cv2.imshow('Puppy', img)
    # If we've waited at least 1ms and wait key (ASCII 27 coded) pressed.
    if cv2.waitKey(1) & 0xff == 27:
        break

cv2.destroyAllWindows()
