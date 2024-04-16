import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget
from Demo.second_window import SecondWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 300)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.main_window_widget = QWidget()
        self.init_main_window()
        self.stacked_widget.addWidget(self.main_window_widget)

    def init_main_window(self):
        self.layout = QVBoxLayout(self.main_window_widget)
        self.next_button = QPushButton("Next", self.main_window_widget)
        self.next_button.clicked.connect(self.open_second_window)
        self.layout.addWidget(self.next_button)

    def open_second_window(self):
        self.second_window = SecondWindow()
        self.second_window.back_button.clicked.connect(self.show_main_window)
        self.stacked_widget.addWidget(self.second_window)
        self.stacked_widget.setCurrentWidget(self.second_window)

    def show_main_window(self):
        self.stacked_widget.setCurrentWidget(self.main_window_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
