import sys
import cv2
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer


# Chck avlable port for cam 
# for i in range(5):
#     cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
#     print(i, cap.isOpened())
#     cap.release()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CV Toolkit")

        # self.cap = cv2.VideoCapture(0) 
        self.cap = cv2.VideoCapture("./data/test.mp4")   
        self.video_label = QLabel()
        self.setCentralWidget(self.video_label)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)                    # ~33 fps

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return
        
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        qimg = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
        self.video_label.setPixmap(QPixmap.fromImage(qimg))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()