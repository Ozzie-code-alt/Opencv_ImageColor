import cv2
import numpy as np

# img = 'Image/lena.jpg'
img = cv2.imread('Image/lena.jpg')
cv2.imshow('Image', img)
points = []


def mClick(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:

        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x, y), 3, (255, 0, 255), -1)
        myColor = np.zeros((512, 512, 3), np.uint8)#numpy zeros arguments(location, data type)
        # fills the image with bgr colors
        myColor [:] = [blue,green,red] # [:] notation means fills every point of the list with bgr

        cv2.imshow('color',myColor) # new window name = new window






cv2.setMouseCallback('Image', mClick)
cv2.waitKey(0)
cv2.destroyAllWindows()