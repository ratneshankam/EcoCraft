        # cred = credentials.Certificate("A:/Core2Web/PythonProject/Core2Web_pythonProject/EcoCraft/ecocraft-team-firebase-adminsdk-c931h-31a37bfd3f.json")
        # firebase_admin.initialize_app(cred, {'storageBucket': 'gs://ecocraft-team.appspot.com'})

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QImage
import firebase_admin
from firebase_admin import credentials, storage
from io import BytesIO
from PIL import Image


class FirebaseImageDisplay(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Firebase Image Display")
        self.setGeometry(100, 100, 400, 300)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        self.image_label = QLabel()
        layout.addWidget(self.image_label)

        self.download_button = QPushButton("Download Image")
        self.download_button.clicked.connect(self.download_image)
        layout.addWidget(self.download_button)

        # Initialize Firebase app
        cred = credentials.Certificate("A:/Core2Web/PythonProject/Core2Web_pythonProject/EcoCraft/ecocraft-team-firebase-adminsdk-c931h-31a37bfd3f.json")
        app = firebase_admin.initialize_app(cred, {'storageBucket': 'ecocraft-team.appspot.com'})
        self.bucket = storage.bucket()
# cred = credentials.Certificate("A:/Core2Web/PythonProject/Core2Web_pythonProject/EcoCraft/ecocraft-team-firebase-adminsdk-c931h-31a37bfd3f.json")
        # firebase_admin.initialize_app(cred, {'storageBucket': 'gs://ecocraft-team.appspot.com'})
    def download_image(self):
        blob = self.bucket.get_blob("images/bottleart1.jpg")
        if blob is not None:
            image_data = blob.download_as_bytes()
            image = Image.open(BytesIO(image_data))
            q_image = self.convert_pil_image_to_qimage(image)
            pixmap = QPixmap.fromImage(q_image)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)  # Adjusts the image to fit the label
        else:
            print("Image not found")

    def convert_pil_image_to_qimage(self, pil_image):
        # Convert PIL Image to QImage
        image_rgb = pil_image.convert("RGB")
        width, height = image_rgb.size
        q_image = QImage(image_rgb.tobytes(), width, height, QImage.Format_RGB888)
        return q_image


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FirebaseImageDisplay()
    window.show()
    sys.exit(app.exec_())
