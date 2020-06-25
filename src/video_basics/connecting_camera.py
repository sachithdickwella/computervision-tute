#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

# Argument '0' implies to OpenCV to take default camera connected.
capture = cv2.VideoCapture(0)
# Get required properties.
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
# CODEC of the VIDEO. If windows code should be 'DIVX' and on Linux 'XVID' is more preferable, although
# other codecs also available [https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html].
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# Write video frames to a file.
writer = cv2.VideoWriter('C:/Users/Sachith/Videos/opencv_capture.mp4', fourcc, 20, (width, height))

while capture.isOpened():
    # This statement return a boolean value True/False along with the frame read.
    # True if the frame read correctly in the tuple unpacking.
    _, frame = capture.read()
    # Before showing the frame write to the file using 'cv2.VideoWriter(...)'.
    writer.write(frame)
    # Operations before show. Not mandatory, if just showing the frame, but use for
    # realtime analysis/object detection.
    frame = cv2.cvtColor(frame, code=cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(frame, ddepth=cv2.CV_64F, ksize=5)
    # Show the image using OpenCV.
    cv2.imshow('frame', laplacian)
    # 0xFF bitwise AND keep only the last 8-bits of the key value whatever that
    # key is.
    if cv2.waitKey(20) & 0xFF == 27:
        break

capture.release()
writer.release()
cv2.destroyWindow('frame')
