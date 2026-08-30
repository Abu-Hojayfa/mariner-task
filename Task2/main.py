import os
import sys
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CV Toolkit Launcher")
        self.resize(400, 350)

        btn_face_recognition = QPushButton("Face Recognition")
        btn_tracking = QPushButton("Face Tracking")
        btn_age_gender = QPushButton("Age & Gender")
        btn_counting = QPushButton("Counting")
        btn_toolkit = QPushButton("Toolkit")


        btn_face_recognition.clicked.connect(self.open_face_recognition)
        btn_tracking.clicked.connect(self.open_face_tracking)
        btn_age_gender.clicked.connect(self.open_age_gender)
        btn_counting.clicked.connect(self.open_counting)
        btn_toolkit.clicked.connect(self.open_toolkit)

        button_layout = QVBoxLayout()
        for btn in (btn_face_recognition, btn_tracking, btn_age_gender, btn_counting, btn_toolkit):
            button_layout.addWidget(btn)

        container = QWidget()
        container.setLayout(button_layout)
        self.setCentralWidget(container)

    def open_face_recognition(self):
        if hasattr(self, "face_recognition_process") and self.face_recognition_process.poll() is None:        
            return
        
        path = os.path.join(os.path.dirname(__file__), "face_recogniton.py")
        self.face_recognition_process = subprocess.Popen([sys.executable, path])
        
    
    def open_face_tracking(self):
        if hasattr(self, "face_tracking_process") and self.face_tracking_process.poll() is None:
        
            return
        path = os.path.join(os.path.dirname(__file__), "face_tracking.py")
        self.face_tracking_process = subprocess.Popen([sys.executable, path])
        
    
    def open_age_gender(self):
        if hasattr(self, "age_gender_process") and self.age_gender_process.poll() is None:
        
            return
        path = os.path.join(os.path.dirname(__file__), "age_gender.py")
        self.age_gender_process =   subprocess.Popen([sys.executable, path])
        
    
    def open_counting(self):
        if hasattr(self, "counting_process") and self.counting_process.poll() is None:
            return
        path = os.path.join(os.path.dirname(__file__), "counting.py")
        self.counting_process = subprocess.Popen([sys.executable, path])
        
    
    def open_toolkit(self):
        if hasattr(self, "toolkit_process") and self.toolkit_process.poll() is None:
        
            return
        path = os.path.join(os.path.dirname(__file__), "toolkit.py")
        self.toolkit_process = subprocess.Popen([sys.executable, path])
        



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()