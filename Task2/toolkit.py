import cv2 as cv
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog ,QApplication, QMainWindow, QLabel ,QVBoxLayout, QHBoxLayout,QWidget, QPushButton

from PySide6.QtGui import QPixmap, QImage

STYLE = """
QMainWindow { background-color: #1e1f26; }
QPushButton { background-color: #2b2d3a; border: 1px solid #ccc; padding: 5px; color: #fff; font-size: 14px; }
QPushButton:hover { background-color: #383b4d; }
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Toolkit")
        self.resize(700, 600)

        self.original_frame = None
        self.image_label = QLabel(
            "no image loaded"
        )

        btn_upload = QPushButton("Upload Image")
        btn_gray = QPushButton("Convert to Grayscale")
        btn_resize = QPushButton("Resize Image")
        btn_rotate = QPushButton("Rotate Image")
        btn_blur = QPushButton("Blur Image")


        btn_upload.clicked.connect(self.open_upload)
        # btn_gray.clicked.connect(self.open_gray)
        # btn_resize.clicked.connect(self.open_resize)
        # btn_rotate.clicked.connect(self.open_rotate)
        # btn_blur.clicked.connect(self.open_blur)

        button_layout = QVBoxLayout()
        
        for btn in (btn_upload, btn_gray, btn_resize, btn_rotate, btn_blur):
            button_layout.addWidget(btn, Qt.AlignmentFlag.AlignHCenter)
        

        layout = QHBoxLayout()
        layout.addWidget(self.image_label, stretch=1)
        layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def open_upload(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        if path:
            self.original_frame = cv.imread(path)
            self.display_image(self.original_frame)

    def display_image(self, frame):
        rgb_image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        qimage = QImage(rgb_image.data, w, h, ch * w, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        scaled_pixmap = pixmap.scaled(980,720, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)



app = QApplication(sys.argv)
app.setStyleSheet(STYLE)
window = MainWindow()
window.show()
app.exec()