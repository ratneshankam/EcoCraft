import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase Admin SDK
cred = credentials.Certificate(
    "A:/Core2Web/PythonProject/Core2Web_pythonProject/EcoCraft/ecocraft-team-firebase-adminsdk-c931h-31a37bfd3f.json"
)  # Replace with your service account key
firebase_admin.initialize_app(cred)


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.resize(400, 500)
        self.setStyleSheet("background-color: white;")

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        welcome_label = QLabel("Welcome Back !!")
        welcome_label.setFont(QFont("Arial", 14, QFont.Bold))
        main_layout.addWidget(welcome_label)

        image_label = QLabel()
        # A:\Core2Web\PythonProject\Core2Web_pythonProject\EcoCraft\assets\images\loginImg.jpg
        pixmap = QPixmap(
            "A:/Core2Web/PythonProject/Core2Web_pythonProject/EcoCraft/assets/images/loginImg.jpg"
        )
        pixmap = pixmap.scaledToHeight(300)
        pixmap = pixmap.scaledToWidth(300)
        image_label.setPixmap(pixmap)
        main_layout.addWidget(image_label)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setMaximumWidth(250)
        main_layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMaximumWidth(250)
        main_layout.addWidget(self.password_input)

        login_button = QPushButton("Login")
        login_button.setStyleSheet("font-size: 16px;")
        login_button.clicked.connect(self.login)
        main_layout.addWidget(login_button)

        self.setLayout(main_layout)

    def authenticate_user(self):
        email = self.username_input.text()
        password = self.password_input.text()
        try:
            user = auth.get_user_by_email(email)
            # If the user exists, attempt to verify the password
            auth_user = auth.update_user(user.uid, password=password)
            print("User authenticated successfully:", auth_user.uid)
            return auth_user
        except auth.AuthError as e:
            # Handle authentication errors
            print("Authentication failed:", e)

    def login(self):
        self.authenticate_user()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = Login()
    login_window.show()
    sys.exit(app.exec_())
