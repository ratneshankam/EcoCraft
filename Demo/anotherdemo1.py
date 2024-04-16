import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from firebase_admin import credentials, firestore, auth, initialize_app

# Initialize Firestore
# cred = credentials.Certificate("A:/Core2Web/PythonProject/Core2Web_pythonProject/EcoCraft/ecocraft_ratnesh/ecocraft/ecocraft-team-firebase-adminsdk-c931h-31a37bfd3f.json")
# initialize_app(cred)
db = firestore.client()
class SignupDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Signup")
        self.parent = parent

        self.create_main_frame()
        self.create_entry_fields()
        self.create_signup_button()

    def create_main_frame(self):
        self.main_frame = QVBoxLayout()
        self.setLayout(self.main_frame)

    def create_entry_fields(self):
        labels = ["Name", "Email", "Phone", "Username", "Password"]
        self.entries = []
        for label in labels:
            hbox = QHBoxLayout()
            hbox.addWidget(QLabel(label + ":"))
            entry = QLineEdit()
            hbox.addWidget(entry)
            self.entries.append(entry)
            self.main_frame.addLayout(hbox)

    def create_signup_button(self):
        signup_button = QPushButton("Signup")
        signup_button.clicked.connect(self.signup)
        self.main_frame.addWidget(signup_button)

    def signup(self):
        name = self.entries[0].text()
        email = self.entries[1].text()
        phone = self.entries[2].text()
        username = self.entries[3].text()
        password = self.entries[4].text()

        doc_ref = db.collection('users').document(username)
        doc_ref.set({
            'name': name,
            'email': email,
            'phone': phone,
            'password': password,
            'first_time': True
        })

        print("User signed up successfully!")
        self.accept()

class WelcomeWindow(QMainWindow):
    def __init__(self, welcome_message):
        super().__init__()
        self.setWindowTitle("Welcome")
        self.setWindowState(Qt.WindowMaximized)

        central_widget = QLabel(self)
        central_widget.setAlignment(Qt.AlignCenter)
        central_widget.setStyleSheet("background-color: #192F44; color: white; font-size: 40pt;")
        central_widget.setText(welcome_message)
        self.setCentralWidget(central_widget)

class LoginWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login")

        self.create_main_frame()
        self.create_entry_fields()
        self.create_login_button()

    def create_main_frame(self):
        self.main_frame = QVBoxLayout()
        self.setLayout(self.main_frame)

    def create_entry_fields(self):
        self.username_entry = QLineEdit()
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.main_frame.addWidget(QLabel("Username:"))
        self.main_frame.addWidget(self.username_entry)
        self.main_frame.addWidget(QLabel("Password:"))
        self.main_frame.addWidget(self.password_entry)

    def create_login_button(self):
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.login)
        self.main_frame.addWidget(login_button)

    def login(self):
        username = self.username_entry.text()
        password = self.password_entry.text()

        doc_ref = db.collection('users').document(username)
        doc = doc_ref.get()

        if doc.exists:
            user_data = doc.to_dict()
            if user_data['password'] == password:
                welcome_message = ""
                if 'first_time' in user_data:
                    welcome_message = "You are visiting our page for the first time."
                    doc_ref.update({'first_time': firestore.DELETE_FIELD})
                else:
                    welcome_message = "Welcome back, " + user_data['name']

                welcome_window = WelcomeWindow(welcome_message)
                welcome_window.show()
                self.accept()
            else:
                QMessageBox.warning(self, "Login Error", "Invalid username or password!")
        else:
            QMessageBox.warning(self, "Login Error", "User does not exist!")

class RentWheels(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.setWindowState(Qt.WindowMaximized)
        self.central_widget = QLabel(self)
        self.central_widget.setStyleSheet("background-color: white;")
        self.setCentralWidget(self.central_widget)

        self.add_upper_frame()
        

    def add_upper_frame(self):
        self.upper_frame = QVBoxLayout()
        self.central_widget.setLayout(self.upper_frame)

        # Load image
        self.original_image_pil = QPixmap("C:/Users/prana/Downloads/rentwheels.png")
        self.resized_image_pil = self.original_image_pil.scaledToWidth(500)
        self.logo_label = QLabel()
        self.logo_label.setPixmap(self.resized_image_pil)
        self.upper_frame.addWidget(self.logo_label)

        # Add privacy policy button
        self.privacy_button = QPushButton("Privacy Policy")
        self.privacy_button.setStyleSheet("background-color: black; color: white; font-size: 14pt;")
        self.privacy_button.clicked.connect(self.show_privacy_policy)
        self.upper_frame.addWidget(self.privacy_button, alignment=Qt.AlignRight)

        # Add login/signup buttons
        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet("background-color: black; color: white; font-size: 14pt;")
        self.login_button.clicked.connect(self.open_login_window)
        self.upper_frame.addWidget(self.login_button, alignment=Qt.AlignRight)

        self.signup_button = QPushButton("Signup")
        self.signup_button.setStyleSheet("background-color: black; color: white; font-size: 14pt;")
        self.signup_button.clicked.connect(self.open_signup_window)
        self.upper_frame.addWidget(self.signup_button, alignment=Qt.AlignRight)

    def show_privacy_policy(self):
        # Implement privacy policy dialog
        pass

    def open_login_window(self):
        login_window = LoginWindow(self)
        login_window.exec_()

    def open_signup_window(self):
        signup_dialog = SignupDialog(self)
        signup_dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    rent_wheels = RentWheels()
    rent_wheels.show()
    sys.exit(app.exec_())
