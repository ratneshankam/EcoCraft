import sys
import os
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class CarouselSlider(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image_paths = [
            "assets/images/landingImg1.jpg",
            "assets/images/landingImg2.jpg",
            "assets/images/landingImg3.jpg",
            "assets/images/landingImg4.jpg",
        ]
        self.current_index = 0
        self.setObjectName("Widget")
        self.setStyleSheet("background-color: white;")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.image_label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.next_image)
        self.timer.start(1000)  # AutoPlay interval in milliseconds

        self.load_image()

    def load_image(self):
        pixmap = QPixmap(
            self.image_paths[self.current_index],
        ).scaled(
            QApplication.primaryScreen().size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation,
        )
        pixmap = pixmap.scaledToHeight(300)

        pixmap = pixmap.scaledToWidth(600)
        self.image_label.setPixmap(pixmap)

    def next_image(self):
        self.current_index = (self.current_index + 1) % len(self.image_paths)
        self.load_image()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EcoCraft")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        carousel_slider = CarouselSlider()
        main_layout.addWidget(carousel_slider)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
