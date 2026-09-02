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
        btn_gray.clicked.connect(self.open_gray)
        btn_resize.clicked.connect(self.open_resize)
        btn_rotate.clicked.connect(self.open_rotate)
        btn_blur.clicked.connect(self.open_blur)

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

        max_w, max_h = 980, 720
        if w > max_w or h > max_h:
          pixmap = pixmap.scaled(max_w, max_h, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        self.image_label.setPixmap(pixmap)

    def open_gray(self):
        if self.original_frame is not None:
            gray_frame = cv.cvtColor(self.original_frame, cv.COLOR_BGR2GRAY)
            self.display_image(cv.cvtColor(gray_frame, cv.COLOR_GRAY2BGR))

    def open_resize(self):
        if self.original_frame is not None:
            resized_frame = cv.resize(self.original_frame, None, fx=0.3, fy=0.3)
            self.display_image(resized_frame)

    def open_rotate(self):
        if self.original_frame is not None:
            rotated_frame = cv.rotate(self.original_frame, cv.ROTATE_90_CLOCKWISE)
            self.display_image(rotated_frame)

    def open_blur(self):
        if self.original_frame is not None:
            blurred_frame = cv.GaussianBlur(self.original_frame, (15, 15), 0)
            self.display_image(blurred_frame)

app = QApplication(sys.argv)
app.setStyleSheet(STYLE)
window = MainWindow()
window.show()
app.exec()