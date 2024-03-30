import cv2 as cv
import numpy as np

##CREATE A BLANK IMAGE
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)
cv.waitKey(0)


##PAINT IT RED
blank[:] = 0,0,255
cv.imshow('Red', blank)
cv.waitKey(0)



##RED SQUARE IN THE BLANK IMAGE
blank[200:300, 300:400] = 0,0,255
cv.imshow('Red', blank)
cv.waitKey(0)


#DRAW RECTANGLE
cv.rectangle(blank, (0,0), (300, 200), (0, 0, 255), thickness=2)
cv.imshow('rectangle', blank)
cv.waitKey(0)


#FILL the rectangle
cv.rectangle(blank, (0,0), (300, 200), (0, 0, 255), thickness=-1)
cv.imshow('rectangle', blank)
cv.waitKey(0)


##DRAW CIRCLE
cv.circle(blank, (250, 250), 40, (0,0,255), thickness=2)
cv.imshow('Circle', blank)
cv.waitKey(0)



###DRAW BANGLADESH FLAG
flag = np.zeros((500, 500, 3), dtype='uint8')
cv.rectangle(flag, (0,0), (300, 180), (32,46,9), thickness=-1)
cv.circle(flag, (135, 90), 60, (0,0,255), thickness=-1)
cv.imshow('Flag', flag)
cv.waitKey(0)



###DRAW LINE
cv.line(blank, (0,0), (250,250), (0,0,255), thickness=2)
cv.imshow('Line', blank)
cv.waitKey(0)


##PUT TEXT
cv.putText(blank, "HELLO, I AM NADEEF", (10,250), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)
cv.waitKey(0)