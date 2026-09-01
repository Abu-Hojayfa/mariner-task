import cv2 as cv
import os
path = cv.data.haarcascades + "haarcascade_frontalface_default.xml"
print(path)
print(os.path.exists(path))