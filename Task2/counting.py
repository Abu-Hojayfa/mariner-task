import cv2 as cv
from ultralytics import YOLO

model = YOLO("model/yolov8n.pt")

vid = cv.VideoCapture("data/test3.mp4")

if not vid.isOpened():
    print("Error: Could not open video.")
    exit()

seen_id = set();

while cv.waitKey(1) != ord("x"):
    ret, frame = vid.read()
    
    if not ret:
        print("Error: Could not read frame.")
        break
      
    result = model.track(frame, imgsz=416, persist=True, verbose=False)
    
    if result[0].boxes.id is not None:
      ids = result[0].boxes.id.int().tolist()
      for id in ids:
        seen_id.add(id)
    
    count = len(seen_id)
    cv.putText(frame, f"Count: {count}", (10, 30),               
    cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    
    cv.imshow("Count Objects", result[0].plot())


print(f"Total unique objects counted: {len(seen_id)}")

vid.release()

cv.destroyAllWindows()
