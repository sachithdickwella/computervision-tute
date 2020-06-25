#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import time

capture = cv2.VideoCapture('C:/Users/Sachith/Videos/opencv_capture.mp4')

if not capture.isOpened():
    print('Video file is not opened, check the file path or codec.')

while capture.isOpened():

    ret, frame = capture.read()

    if ret:

        # The video is playing much faster than the human can watch it, hence computer can read it quickly for
        # further processing. Therefore, if we want to slow down the video into a slower rate that a person can
        # watch, just sleep the thread for a while. More idle sleeping time would be the time for single frame.
        # This source video record in 20 frames, so wait 20th of a second until next frame.
        time.sleep(1 / 20)
        cv2.imshow('frame', frame)

        if cv2.waitKey(20) & 0xff == 27:
            break
    else:
        break

capture.release()
cv2.destroyWindow('frame')
