import sys
import os
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QStackedWidget,
    QLabel,
    QTextEdit,
    QHBoxLayout,
    QFileDialog,
    QGraphicsDropShadowEffect,
    QDesktopWidget,
    QMessageBox,
)
from PyQt5.QtGui import QPixmap, QColor, QIcon, QFont
from PyQt5.QtCore import Qt, QRect
from purchase import MainWindow
import firebase_admin
from firebase_admin import credentials, storage


class ImageUploader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EcoCraft")
        self.setWindowIcon(QIcon("assets/images/hand-made.png"))
        self.setStyleSheet("background-color: white;")
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.main_window_widget = QWidget()
        self.init_main_window()
        self.stacked_widget.addWidget(self.main_window_widget)

        self.description = ""
        self.file_path = ""
        

    def show_main_window(self):
        self.stacked_widget.setCurrentWidget(self.main_window_widget)

    def open_second_window(self):
        self.second_window = MainWindow(
            self.firebase_app, self.description, self.file_path, self.show_main_window
        )
        self.second_window.action_button.clicked.connect(self.show_main_window)
        self.stacked_widget.addWidget(self.second_window)
        self.stacked_widget.setCurrentWidget(self.second_window)

    def init_firebase_app(self):
        try:
            self.firebase_app = (
                firebase_admin.get_app()
            )  # Check if Firebase app already exists
        except ValueError:
            # Firebase app does not exist, initialize it
            cred = credentials.Certificate(
                "ecocraft-team-firebase-adminsdk-c931h-31a37bfd3f.json"
            )  # Replace with your service account key
            self.firebase_app = firebase_admin.initialize_app(
                cred, {"storageBucket": "ecocraft-team.appspot.com"}
            )

    def init_main_window(self):
        self.init_firebase_app()  # Initialize Firebase app

        desktop = QDesktopWidget()
        primary_screen = desktop.screenGeometry(desktop.primaryScreen())
        # Retrieve the width of the monitor
        monitor_width = primary_screen.width()
        monitor_height = primary_screen.width()
        self.setObjectName("Widget")
        self.resize(monitor_width, monitor_height)
        self.setStyleSheet("background-color: white;")

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Column layout for image box and description edit
        image_label = QLabel()
        pixmap = QPixmap("assets/images/landingImg1.jpg")

        pixmap = pixmap.scaledToHeight(600)
        pixmap = pixmap.scaledToWidth(600)

        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(image_label)

        column_layout = QVBoxLayout()

        self.image_label = QLabel(
            "Transforming Waste into Crafting Art for Your Service!"
        )
        self.image_label.setFont(QFont("Georgia", 14, QFont.Bold))
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedHeight(150)
        self.image_label.setStyleSheet(
            "color: #4F6F52; font-weight:bold; font-style: italic; font-size:40px; border: 2px solid black; padding: 5px; border-radius: 10px; background-color: white;"
        )

        # Create a drop shadow effect for image_label
        image_shadow_effect = QGraphicsDropShadowEffect()
        image_shadow_effect.setBlurRadius(5)  # Set the blur radius of the shadow
        image_shadow_effect.setOffset(5, 5)  # Set the blur radius of the shadow
        image_shadow_effect.setColor(
            QColor(0, 0, 0, 80)
        )  # Set the color and opacity of the shadow

        # Apply the drop shadow effect to the image label
        self.image_label.setGraphicsEffect(image_shadow_effect)

        column_layout.addWidget(self.image_label)
        column_layout.addSpacing(20)  # Adds 20 pixels of space between widgets

        self.description_edit = QTextEdit()
        self.description_edit.setPlaceholderText(
            "Please! Enter a word describing the type of waste you want to transform:"
        )

        self.description_edit.setFixedHeight(100)
        self.description_edit.setStyleSheet(
            "font-size:18px; border: 2px solid black; padding: 10px; border-radius: 10px; background-color: white;"
        )

        # Apply the drop shadow effect to the description edit
        description_shadow_effect = QGraphicsDropShadowEffect()
        description_shadow_effect.setBlurRadius(5)  # Set the blur radius of the shadow
        description_shadow_effect.setOffset(5, 5)  # Set the blur radius of the shadow
        description_shadow_effect.setColor(
            QColor(0, 0, 0, 80)
        )  # Set the color and opacity of the shadow

        # Apply the drop shadow effect to the description edit
        self.description_edit.setGraphicsEffect(description_shadow_effect)

        column_layout.addWidget(self.description_edit)

        main_layout.addLayout(column_layout)

        # Horizontal layout for upload button and next button
        button_layout = QHBoxLayout()

        self.upload_button = QPushButton("Upload Image")
        self.upload_button.setStyleSheet(
            "font-size:18px; background-color: #4CAF50; padding: 10px 20px; border: none; border-radius: 5px; margin: 0px 10px;"
        )
        self.upload_button.clicked.connect(self.upload_image)
        button_layout.addWidget(self.upload_button)

        # Create a drop shadow effect for image_label
        upload_shadow_effect = QGraphicsDropShadowEffect()
        upload_shadow_effect.setBlurRadius(4)  # Set the blur radius of the shadow
        upload_shadow_effect.setColor(
            QColor(0, 0, 0, 80)
        )  # Set the color and opacity of the shadow
        upload_shadow_effect.setOffset(5, 5)

        # Apply the drop shadow effect to the image label
        self.upload_button.setGraphicsEffect(upload_shadow_effect)

        self.next_button = QPushButton("Next")
        self.next_button.setStyleSheet(
            "font-size:18px; background-color: #008CBA; color: white; padding: 10px 20px; border: none; border-radius: 5px; margin: 0px 10px;"
        )
        self.next_button.clicked.connect(self.next_action)
        button_layout.addWidget(self.next_button)
        column_layout.addSpacing(20)  # Adds 20 pixels of space between widgets

        # Create a drop shadow effect for image_label
        next_shadow_effect = QGraphicsDropShadowEffect()
        next_shadow_effect.setBlurRadius(4)  # Set the blur radius of the shadow
        next_shadow_effect.setColor(
            QColor(0, 0, 0, 80)
        )  # Set the color and opacity of the shadow
        next_shadow_effect.setOffset(5, 5)
        # Apply the drop shadow effect to the image label
        self.next_button.setGraphicsEffect(next_shadow_effect)

        main_layout.addLayout(button_layout)

        # message_label = QLabel("We can help you to design and art for you from waste")
        # message_label.setAlignment(Qt.AlignCenter)
        # message_label.setStyleSheet("font-size:18px; font-style: italic; color: #808080;")
        # main_layout.addWidget(message_label)
        
        # Add a label to display the file path
        self.file_path_label = QLabel()
        main_layout.addWidget(self.file_path_label)

        self.main_window_widget.setLayout(main_layout)

    def upload_image(self):
        self.file_path, _ = QFileDialog.getOpenFileName(
            self, "Open Image File", "", "Image files (*.jpg *.png)"
        )
        # if file_path:
        #     # Display the file path in a label
        #     self.file_path_label.setText(f"File Path: {file_path}")
        if self.file_path:
            pixmapUpload = QPixmap(self.file_path)
            pixmapUpload = pixmapUpload.scaledToWidth(200, Qt.SmoothTransformation)
            self.image_label.setPixmap(pixmapUpload)
            self.image_label.setAlignment(Qt.AlignCenter)
            

    def next_action(self):
        self.description = self.description_edit.toPlainText()
        print("Description:", self.description)
        print(self.description)
        if self.description == "":
            self.show_prompt_message()
        else:
            self.open_second_window()

        return self.description

    def show_prompt_message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Please! Enter Something")
        msg.setWindowTitle("Prompt")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if not self.image_label.pixmap():
            return
        self.image_label.setPixmap(
            self.image_label.pixmap().scaledToWidth(self.width() / 2 - 20)
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    uploader = ImageUploader()
    uploader.show()
    sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import (
#     QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget,
#     QLabel, QTextEdit, QHBoxLayout, QFileDialog, QGraphicsDropShadowEffect, QDesktopWidget,
# )
# from PyQt5.QtGui import QPixmap, QColor, QIcon
# from PyQt5.QtCore import Qt
# from procedure import MainWindow
# import firebase_admin
# from firebase_admin import credentials

# class ImageUploader(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("EcoCraft")
#         self.setWindowIcon(QIcon("assets/images/hand-made.png"))
#         self.setStyleSheet("background-color: white;")
#         self.stacked_widget = QStackedWidget()
#         self.setCentralWidget(self.stacked_widget)

#         self.main_window_widget = QWidget()
#         self.init_main_window()
#         self.stacked_widget.addWidget(self.main_window_widget)

#     def show_main_window(self):
#         self.stacked_widget.setCurrentWidget(self.main_window_widget)

#     def open_second_window(self):
#         self.second_window = MainWindow(self.firebase_app)
#         self.second_window.action_button.clicked.connect(self.show_main_window)
#         self.stacked_widget.addWidget(self.second_window)
#         self.stacked_widget.setCurrentWidget(self.second_window)

#     def init_firebase_app(self):
#         try:
#             self.firebase_app = firebase_admin.get_app()  # Check if Firebase app already exists
#         except ValueError:
#             # Firebase app does not exist, initialize it
#             cred = credentials.Certificate("ecocraft-team-firebase-adminsdk-c931h-31a37bfd3f.json")  # Replace with your service account key
#             self.firebase_app = firebase_admin.initialize_app(cred, {'storageBucket': 'ecocraft-team.appspot.com'})

#     def init_main_window(self):
#         self.init_firebase_app()  # Initialize Firebase app

#         desktop = QDesktopWidget()
#         primary_screen = desktop.screenGeometry(desktop.primaryScreen())
#         # Retrieve the width of the monitor
#         monitor_width = primary_screen.width()
#         monitor_height = primary_screen.width()
#         self.setObjectName("Widget")
#         self.resize(monitor_width, monitor_height)
#         self.setStyleSheet("background-color: white;")

#         main_layout = QVBoxLayout()
#         main_layout.setContentsMargins(20, 20, 20, 20)

#         # Column layout for image box and description edit
#         image_label = QLabel()
#         pixmap = QPixmap("assets/images/landingImg1.jpg")

#         pixmap = pixmap.scaledToHeight(600)
#         pixmap = pixmap.scaledToWidth(600)

#         image_label.setPixmap(pixmap)
#         image_label.setAlignment(Qt.AlignCenter)

#         main_layout.addWidget(image_label)

#         column_layout = QVBoxLayout()

#         self.image_label = QLabel()
#         self.image_label.setAlignment(Qt.AlignCenter)
#         self.image_label.setFixedHeight(100)
#         self.image_label.setStyleSheet(
#             "border: 2px solid black; padding: 5px; border-radius: 10px; background-color: white;"
#         )

#         # Create a drop shadow effect for image_label
#         image_shadow_effect = QGraphicsDropShadowEffect()
#         image_shadow_effect.setBlurRadius(5)  # Set the blur radius of the shadow
#         image_shadow_effect.setOffset(5, 5)  # Set the blur radius of the shadow
#         image_shadow_effect.setColor(QColor(0, 0, 0, 80))  # Set the color and opacity of the shadow

#         # Apply the drop shadow effect to the image label
#         self.image_label.setGraphicsEffect(image_shadow_effect)

#         column_layout.addWidget(self.image_label)
#         column_layout.addSpacing(20)  # Adds 20 pixels of space between widgets

#         self.description_edit = QTextEdit()
#         self.description_edit.setPlaceholderText(
#             "Please! Enter a word describing the type of waste you want to transform:"
#         )
#         self.description_edit.setFixedHeight(100)
#         self.description_edit.setStyleSheet(
#             "border: 2px solid black; padding: 10px; border-radius: 10px; background-color: white;"
#         )

#         # Apply the drop shadow effect to the description edit
#         description_shadow_effect = QGraphicsDropShadowEffect()
#         description_shadow_effect.setBlurRadius(5)  # Set the blur radius of the shadow
#         description_shadow_effect.setOffset(5, 5)  # Set the blur radius of the shadow
#         description_shadow_effect.setColor(QColor(0, 0, 0, 80))  # Set the color and opacity of the shadow

#         # Apply the drop shadow effect to the description edit
#         self.description_edit.setGraphicsEffect(description_shadow_effect)

#         column_layout.addWidget(self.description_edit)

#         main_layout.addLayout(column_layout)

#         # Horizontal layout for upload button and next button
#         button_layout = QHBoxLayout()

#         self.upload_button = QPushButton("Upload Image")
#         self.upload_button.setStyleSheet(
#             "background-color: #4CAF50; padding: 10px 20px; border: none; border-radius: 5px;"
#         )
#         self.upload_button.clicked.connect(self.upload_image)
#         button_layout.addWidget(self.upload_button)

#         # Create a drop shadow effect for image_label
#         upload_shadow_effect = QGraphicsDropShadowEffect()
#         upload_shadow_effect.setBlurRadius(4)  # Set the blur radius of the shadow
#         upload_shadow_effect.setColor(QColor(0, 0, 0, 80))  # Set the color and opacity of the shadow
#         upload_shadow_effect.setOffset(5, 5)

#         # Apply the drop shadow effect to the image label
#         self.upload_button.setGraphicsEffect(upload_shadow_effect)

#         self.next_button = QPushButton("Next")
#         self.next_button.setStyleSheet(
#             "background-color: #008CBA; color: white; padding: 10px 20px; border: none; border-radius: 5px;"
#         )
#         self.next_button.clicked.connect(self.open_second_window)
#         button_layout.addWidget(self.next_button)
#         column_layout.addSpacing(20)  # Adds 20 pixels of space between widgets

#         # Create a drop shadow effect for image_label
#         next_shadow_effect = QGraphicsDropShadowEffect()
#         next_shadow_effect.setBlurRadius(4)  # Set the blur radius of the shadow
#         next_shadow_effect.setColor(QColor(0, 0, 0, 80))  # Set the color and opacity of the shadow
#         next_shadow_effect.setOffset(5, 5)
#         # Apply the drop shadow effect to the image label
#         self.next_button.setGraphicsEffect(next_shadow_effect)

#         main_layout.addLayout(button_layout)

#         message_label = QLabel("We can help you to design and art for you from waste")
#         message_label.setAlignment(Qt.AlignCenter)
#         message_label.setStyleSheet("font-style: italic; color: #808080;")
#         main_layout.addWidget(message_label)

#         # Add a label to display the file path
#         self.file_path_label = QLabel()
#         main_layout.addWidget(self.file_path_label)

#         self.main_window_widget.setLayout(main_layout)

#     def upload_image(self):
#         file_path, _ = QFileDialog.getOpenFileName(
#             self, "Open Image File", "", "Image files (*.jpg *.png)"
#         )
#         if file_path:
#             # Display the file path in a label
#             self.file_path_label.setText(f"File Path: {file_path}")

#     def next_action(self):
#         description = self.description_edit.toPlainText()
#         print("Description:", description)

#     def resizeEvent(self, event):
#         super().resizeEvent(event)
#         if not self.image_label.pixmap():
#             return
#         self.image_label.setPixmap(
#             self.image_label.pixmap().scaledToWidth(self.width() / 2 - 20)
#         )

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     uploader = ImageUploader()
#     uploader.show()
#     sys.exit(app.exec_())
