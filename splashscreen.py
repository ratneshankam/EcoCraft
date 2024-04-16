import sys
from PyQt5.QtWidgets import QApplication, QSplashScreen, QWidget
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer
from welocme_and_login import WelcomeScreen
import time


class SplashScreen(QSplashScreen):
    def __init__(self):
        super().__init__()
        self.setPixmap(
            QPixmap("assets/images/handCraft.png").scaled(
                QApplication.primaryScreen().size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
        )  # Adjust image size to fit the screen
        font = QFont("Helvetica", 14)
        self.setFont(font)


class Main(QWidget):
    def __init__(self):
        super().__init__()

        # Create a plain white background window
        self.setStyleSheet("background-color: white;")
        self.setGeometry(100, 100, 800, 600)
        self.splashWindowing()

    def splashWindowing(self):
        splash = SplashScreen()
        splash.showMaximized()

        # Simulate some initialization process (e.g., loading resources)
        # QTimer.singleShot(3000, splash.close)
        time.sleep(3)  # Wait for 3 seconds
        splash.close()
        
        obj = WelcomeScreen()
        obj.showMaximized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    obj = Main()
    obj.showMaximized()

    sys.exit(app.exec_())
