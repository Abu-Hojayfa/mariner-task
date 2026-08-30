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
        path = os.path.join(os.path.dirname(__file__), "face_recogniton.py")
        subprocess.Popen([sys.executable, path])
        
    
    def open_face_tracking(self):
        path = os.path.join(os.path.dirname(__file__), "face_tracking.py")
        subprocess.Popen([sys.executable, path])
        
    
    def open_age_gender(self):
        path = os.path.join(os.path.dirname(__file__), "age_gender.py")
        subprocess.Popen([sys.executable, path])
        
    
    def open_counting(self):
        path = os.path.join(os.path.dirname(__file__), "counting.py")
        subprocess.Popen([sys.executable, path])
        
    
    def open_toolkit(self):
        path = os.path.join(os.path.dirname(__file__), "toolkit.py")
        subprocess.Popen([sys.executable, path])
        



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()