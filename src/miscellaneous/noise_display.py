#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

while True:

    img = np.random.randint(low=0, high=2, size=(height, width, 3), dtype=np.uint8) * 255

    cv2.imshow('noise', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyWindow('noise')
