import cv2 as cv
from ultralytics import YOLO

model = YOLO("model/yolov8m-face.pt")

vid = cv.VideoCapture("data/test.mp4")

if not vid.isOpened():
    print("Error: Could not open video.")
    exit()


while cv.waitKey(1) != ord("x"):
    ret, frame = vid.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    result = model(frame,  verbose=False)
    cv.imshow("Face Detection", result[0].plot())


vid.release()

cv.destroyAllWindows()
