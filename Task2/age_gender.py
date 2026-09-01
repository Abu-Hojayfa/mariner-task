import cv2 as cv
from deepface import DeepFace 




vid = cv.VideoCapture("data/test2.mp4")

if not vid.isOpened():
    print("Error: Could not open video.")
    exit()


while cv.waitKey(1) != ord("x"):
    ret, frame = vid.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    
    try:
        result = DeepFace.analyze(frame, actions=['age', 'gender'], enforce_detection=False, silent=True)
        
        for face in result:
            (x,y,w,h) = face["region"]["x"], face["region"]["y"], face["region"]["w"], face["region"]["h"]
            age = face["age"]
            gender = face["dominant_gender"]
        
            cv.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
            cv.putText(frame, f"Age: {age}", (x, y-30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            cv.putText(frame, f"Gender: {gender}", (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        
    except Exception as e:
        print(f"Error analyzing frame: {e}")
        

    cv.imshow("Age and Gender Detection", frame)


vid.release()

cv.destroyAllWindows()
