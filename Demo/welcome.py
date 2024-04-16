# Welcome.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome")
        self.setWindowIcon(QIcon("icon.png"))
        self.setStyleSheet("background-color: white;")

        main_layout = QVBoxLayout()

        image_label = QLabel()
        pixmap = QPixmap("A:/Core2Web/PythonProject/Core2Web_pythonProject/EcoCraft/assets/images/signupImg.jpg")
        pixmap = pixmap.scaledToWidth(400)  # Adjust width as needed
        pixmap = pixmap.scaledToHeight(400)  # Adjust height as needed
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(image_label)

        title_label = QLabel("Welcome")
        title_label.setStyleSheet("font-size: 20px; color: black;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        description_label = QLabel("Please login to access your account and start managing waste efficiently.")
        description_label.setStyleSheet("font-size: 10px; color: black;")
        description_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(description_label)

        buttons_layout = QHBoxLayout()

        login_button = QPushButton("Login")
        login_button.setStyleSheet("font-size: 15px; font-weight: bold;")
        login_button.clicked.connect(self.login)
        buttons_layout.addWidget(login_button)

        signup_button = QPushButton("SignUp")
        signup_button.clicked.connect(self.signup)
        buttons_layout.addWidget(signup_button)

        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

    def login(self):
        # Add your login functionality here
        pass

    def signup(self):
        # Add your signup functionality here
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcome_screen = WelcomeScreen()
    welcome_screen.show()
    sys.exit(app.exec_())
