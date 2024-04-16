from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
# from firstwindow import MainWindow

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.back_button = QPushButton("Back")
        # self.back_button.clicked.connect(MainWindow())
        self.layout.addWidget(self.back_button)
