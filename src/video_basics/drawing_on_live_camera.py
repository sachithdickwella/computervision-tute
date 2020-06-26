#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2


# Callback function to draw the image on mouse manipulations.
def draw_rect(event, x, y, flags, params):
    global pt1, pt2, topLeft_clicked, bottomRight_clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        # RESET THE RECTANGLE.
        if topLeft_clicked and bottomRight_clicked:
            topLeft_clicked = False
            bottomRight_clicked = False
            pt1 = (0, 0)
            pt2 = (0, 0)

        if not topLeft_clicked:
            pt1 = (x, y)
            topLeft_clicked = True
        elif not bottomRight_clicked:
            pt2 = (x, y)
            bottomRight_clicked = True


# Initial points of the screen.
pt1 = (0, 0)
pt2 = (0, 0)

# Tracking references to point reference collection.
topLeft_clicked = False
bottomRight_clicked = False

# Video capture and connect the callback.
capture = cv2.VideoCapture(0)

cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rect)

# width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
#
# x, y = width // 2, height // 2
#
# w, h = width // 4, height // 4

while True:

    _, frame = capture.read()

    # cv2.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=4)

    if topLeft_clicked:
        cv2.circle(frame, center=pt1, radius=5, color=(0, 0, 255), thickness=-1)

    if topLeft_clicked and bottomRight_clicked:
        cv2.rectangle(frame, pt1=pt1, pt2=pt2, color=(0, 0, 255), thickness=3)

    cv2.imshow('Test', frame)

    if cv2.waitKey(20) & 0xFF == 27:
        break

capture.release()
cv2.destroyWindow('Test')
