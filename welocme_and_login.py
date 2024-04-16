import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QLineEdit,
    QDesktopWidget,
    QSpacerItem,
    QSizePolicy,
    QMainWindow,
    QMessageBox,
    QCheckBox,
    QSplashScreen,
)
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt
from landing import ImageUploader
import firebase_admin
from firebase_admin import credentials, auth, firestore, initialize_app

cred = credentials.Certificate("ecocraft-team-firebase-adminsdk-c931h-31a37bfd3f.json")
fapp = firebase_admin.initialize_app(
    cred, {"storageBucket": "ecocraft-team.appspot.com"}
)
db = firestore.client()


class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome")
        self.setWindowIcon(QIcon("assets/images/hand-made.png"))
        self.setStyleSheet("background-color: #f0f0f0;")

        # Retrieve the width and height of the monitor
        desktop = QDesktopWidget()
        primary_screen = desktop.screenGeometry(desktop.primaryScreen())
        monitor_width = primary_screen.width()
        monitor_height = primary_screen.height()

        # Set the screen size to the widget
        self.setObjectName("Widget")
        self.resize(monitor_width, monitor_height)

        # Create a main horizontal layout for the window
        main_layout = QHBoxLayout(self)

        # Add horizontal spacer before the card frame
        main_layout.addSpacerItem(
            QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Fixed)
        )

        # Create a frame to act as the card
        card_frame = QFrame(self)
        card_frame.setStyleSheet(
            "background-color: #ffffff; border-radius: 10px; padding: 10px; margin: 10px;"
        )
        card_frame.setFixedSize(550, 650)

        # Create a vertical layout for the card frame
        card_layout = QVBoxLayout(card_frame)

        # Add image
        image_label = QLabel()
        pixmap = QPixmap("assets/images/signupImg.jpg")
        pixmap = pixmap.scaledToWidth(400)  # Adjust width as needed
        pixmap = pixmap.scaledToHeight(400)  # Adjust height as needed
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(image_label)

        # Add title label
        title_label = QLabel("Welcome")
        title_label.setFont(QFont("Georgia", 14, QFont.Bold))
        title_label.setStyleSheet("font-weight: bold; font-size: 30px; color: black;")
        title_label.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(title_label)

        # Add description label
        description_label = QLabel("Please log in to manage waste efficiently.")
        description_label.setFont(QFont("Cursive", 14, QFont.Bold))
        description_label.setStyleSheet(
            "font-style: italic; color: #f5f5f5; font-size: 18px; color: black; margin: 0px 0px"
        )
        description_label.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(description_label)

        # Add buttons layout
        buttons_layout = QHBoxLayout()

        # Add Login button
        login_button = QPushButton("Login")
        login_button.setStyleSheet(
            "font-size: 18px; background-color: #008CBA; color: white; padding: 10px 20px; border: none; border-radius: 5px; margin: 5px;"
        )
        login_button.clicked.connect(self.login)
        buttons_layout.addWidget(login_button)

        # Add SignUp button
        signup_button = QPushButton("SignUp")
        signup_button.setStyleSheet(
            "font-size: 18px; background-color: #008CBA; color: white; padding: 10px 20px; border: none; border-radius: 5px; margin: 5px;"
        )
        signup_button.clicked.connect(self.signup)
        buttons_layout.addWidget(signup_button)

        card_layout.addLayout(buttons_layout)

        # Set layout of card frame
        card_frame.setLayout(card_layout)

        # Add card frame to the main layout
        main_layout.addWidget(card_frame)

        # Add horizontal spacer after the card frame
        main_layout.addSpacerItem(
            QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Fixed)
        )

    def login(self):
        login_window.showMaximized()
        welcome_screen.close()

    def signup(self):
        SignUp_window.showMaximized()
        welcome_screen.close()
        pass


class SignUp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SignUp")
        self.setWindowIcon(QIcon("assets/images/hand-made.png"))
        self.resize(800, 800)
        self.setStyleSheet("background-color: #f0f0f0;")

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignHCenter)

        # Create a frame to act as the card
        card_frame = QFrame(self)
        card_frame.setStyleSheet(
            "background-color: #ffffff; border-radius: 10px;  margin: 10px;"
        )
        card_frame.setFixedSize(550, 660)

        card_layout = QVBoxLayout(card_frame)

        image_label = QLabel(self)
        pixmap = QPixmap("assets/images/Mobile-login.jpg")
        pixmap = pixmap.scaledToHeight(400)
        pixmap = pixmap.scaledToWidth(400)
        image_label.setPixmap(pixmap)
        card_layout.addWidget(image_label)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        # self.username_input.setMaximumWidth(450)
        self.username_input.setStyleSheet(
            "font-size: 18px; background-color: #f0f0f0; color: black; border-radius: 10px; padding: 15px; margin: 5px;"
        )
        card_layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        # self.password_input.setMaximumWidth(450)
        self.password_input.setStyleSheet(
            "font-size: 18px; background-color: #f0f0f0; color: black; border-radius: 10px; padding: 15px; margin: 5px;"
        )
        card_layout.addWidget(self.password_input)

        show_password_checkbox = QCheckBox("Show Password", card_frame)
        show_password_checkbox.setStyleSheet(
            "font-size: 16px;  color:black; text-decoration: underline;"
        )
        show_password_checkbox.stateChanged.connect(
            lambda state: self.toggle_password_visibility(self.password_input, state)
        )

        card_layout.addWidget(show_password_checkbox)

        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("Confirm Password")
        self.confirm_password_input.setStyleSheet(
            "font-size: 18px; background-color: #f0f0f0; color: black; border-radius: 10px; padding: 15px; margin: 5px;"
        )
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        #  self.confirm_password_input.setMaximumWidth(450)
        card_layout.addWidget(self.confirm_password_input)

        forgot_password_button = QPushButton("Forgot Password?")
        forgot_password_button.setStyleSheet(
            "font-style: italic; font-size: 16px; color:black;text-decoration: underline;"
        )
        forgot_password_button.clicked.connect(self.forgot_password)
        card_layout.addWidget(forgot_password_button)

        sign_button = QPushButton("SignUp")
        sign_button.setStyleSheet(
            "font-size: 22px; background-color: #7D7C7C; color: white; padding: 10px 20px; border: none; border-radius: 5px;"
        )

        sign_button.clicked.connect(self.signup)
        card_layout.addWidget(sign_button)

        self.action_button = QPushButton("Back", self)
        self.action_button.setFixedSize(100, 30)  # Set width and height
        self.action_button.clicked.connect(self.signUpToWelcome)

        self.action_button.setStyleSheet(
            "font-size:12px; background-color: #7D7C7C; color: white; padding: 10px 20px; border: none; border-radius: 5px;"
        )
        main_layout.addWidget(self.action_button)
        main_layout.addWidget(card_frame)
        self.setLayout(main_layout)

    def signUpToWelcome(self):
        print("signuptowelcome")
        welcome_screen.showMaximized()
        SignUp_window.close()

    def signup(self):
        print("SignUp")
        if self.password_input.text() == "" or self.username_input.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Do not proceed with empty details!")
            msg.setWindowTitle("Prompt")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
        if self.confirm_password_input.text() != self.password_input.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(
                "passwords you entered don't match! Please, Enter right details"
            )
            msg.setWindowTitle("Prompt")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
        elif (
            self.confirm_password_input.text() == self.password_input.text()
            and self.username_input.text() != ""
        ):
            doc_ref = db.collection("users").document(self.username_input.text())
            doc_ref.set(
                {
                    "username": self.username_input.text(),
                    "password": self.password_input.text(),
                }
            )

            print("User signed up successfully!")
            # self.accept()  #................

            SignUp_window.close()
            login_window.showMaximized()

    def toggle_password_visibility(self, password_input, state):
        if state == Qt.Checked:
            self.password_input.setEchoMode(QLineEdit.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.Password)

    def forgot_password(self):
        print("Forgot Password button clicked")


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setStyleSheet("background-color: #f0f0f0;")
        self.setWindowIcon(QIcon("assets/images/hand-made.png"))
        # Initialize Firebase Admin SDK
        # cred = credentials.Certificate(
        #     "ecocraft-team-firebase-adminsdk-c931h-31a37bfd3f.json"
        # )  # Replace with your service account key
        self.firebase_app = fapp

        self.init_ui()

    def init_ui(self):
        # Retrieve the width and height of the monitor
        desktop = QDesktopWidget()
        primary_screen = desktop.screenGeometry(desktop.primaryScreen())
        monitor_width = primary_screen.width()
        monitor_height = primary_screen.height()

        # Set the screen size to the widget
        self.setObjectName("Widget")
        self.resize(monitor_width, monitor_height)

        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)

        # Create a frame to act as the card
        card_frame = QFrame(self)
        card_frame.setStyleSheet(
            "background-color: #ffffff; border-radius: 10px; padding: 15px; margin: 10px;"
        )
        card_frame.setFixedSize(500, 600)

        # Create a vertical layout for the card frame
        card_layout = QVBoxLayout(card_frame)
        card_layout.setAlignment(Qt.AlignCenter)

        welcome_label = QLabel("Welcome Back !!")
        welcome_label.setFont(QFont("Georgia", 14, QFont.Bold))
        welcome_label.setStyleSheet("font-weight: bold; font-size: 28px; ")
        welcome_label.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(welcome_label)

        image_label = QLabel()
        pixmap = QPixmap("assets/images/loginImg.jpg")
        pixmap = pixmap.scaledToHeight(300)
        pixmap = pixmap.scaledToWidth(300)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(image_label)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet(
            "font-size: 18px; background-color: #D2E3C8; color: black; border-radius: 10px; padding: 15px; margin: 10px;"
        )
        # self.username_input.setMaximumWidth(250)
        card_layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(
            "font-size: 18px; background-color: #D2E3C8; color: black; border-radius: 10px; padding: 15px; margin: 10px;"
        )
        # self.password_input.setMaximumWidth(250)
        card_layout.addWidget(self.password_input)

        login_button = QPushButton("Login")
        login_button.setStyleSheet(
            "font-size: 22px; background-color: #4F6F52; border-radius: 10px; padding: 8px;"
        )
        login_button.clicked.connect(self.login)
        card_layout.addWidget(login_button)

        self.action_button = QPushButton("Back", self)
        self.action_button.setFixedSize(100, 30)  # Set width and height
        self.action_button.clicked.connect(self.loginToSignUp)
        main_layout.addWidget(self.action_button)

        self.action_button.setStyleSheet(
            "font-size:12px; background-color: #7D7C7C; color: white; padding: 10px 20px; border: none; border-radius: 5px;"
        )

        # Set layout of card frame
        card_frame.setLayout(card_layout)

        # Add card frame to the main layout
        main_layout.addWidget(card_frame)

    def loginToSignUp(self):
        print("loginToSignUp")
        SignUp_window.showMaximized()
        login_window.close()

    def show_prompt_message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Invalid Credentials! Please, Enter right details")
        msg.setWindowTitle("Prompt")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()

    def authenticate_user(self):
        email = self.username_input.text()
        password = self.password_input.text()

        doc_ref = db.collection("users").document(self.username_input.text())
        doc = doc_ref.get()
        if doc.exists:
            user_data = doc.to_dict()
            if user_data["password"] == password:
                # self.accept()  #................
                return True
            else:
                QMessageBox.warning(
                    self, "Login Error", "Invalid username or password!"
                )
        else:
            try:
                user = auth.get_user_by_email(email)
                # If the user exists, attempt to verify the password
                auth_user = auth.update_user(user.uid, password=password)
                print("User authenticated successfully:", auth_user.uid)
                print(auth_user)
                return auth_user
            except ValueError as e:
                # Handle authentication errors

                self.show_prompt_message()
                print("Authentication failed:", e)

    def login(self):
        if self.authenticate_user():
            self.uploder = ImageUploader()
            self.uploder.show()
            self.close()

        print("Login button clicked")


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


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    welcome_screen = WelcomeScreen()
    login_window = Login()
    SignUp_window = SignUp()
    splash = SplashScreen()
    splash.showMaximized()
    time.sleep(2)
    # splash.close()
    welcome_screen.showMaximized()

    sys.exit(app.exec_())
