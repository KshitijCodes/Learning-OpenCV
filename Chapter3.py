import cv2
import numpy as np

img = cv2.imread("Resources/Flat.JPG")
print(img.shape)

imgResize = cv2.resize(img,(1000,600))
print(imgResize.shape)

imgCropped = img[0:200,200:500]

cv2.imshow("Image",img)
#cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)