import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel


class PlaceholderLabelLineEdit(QWidget):
    def __init__(self, placeholder="", parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        self.label = QLabel(placeholder)
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText(placeholder)

        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    layout = QVBoxLayout(window)

    placeholder_widget = PlaceholderLabelLineEdit("Enter your text here...")
    layout.addWidget(placeholder_widget)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())


# import sys
# import firebase_admin
# from firebase_admin import credentials, storage
# from PyQt5.QtWidgets import (
#     QApplication,
#     QWidget,
#     QMainWindow,
#     QHBoxLayout,
#     QLabel,
#     QPushButton,
#     QVBoxLayout,
#     QDesktopWidget,
#     QGroupBox,
#     QListWidget,
#     QListWidgetItem,
#     QSplitter,
#     QScrollArea,
#     QGridLayout,
# )
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtCore import Qt
# # from addCart import CartView, AddToCartUI, MainCartApp

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Product Purchase")
#         self.setObjectName("Widget")
#         self.setStyleSheet("background-color: white;")

#         self.init_ui()

#     def init_ui(self):
#         # Set up the app bar
#         self.setup_appbar()

#         # Set up the main content
#         # self.setup_content()

#     def setup_appbar(self):
#         # Create a central widget
#         central_widget = QWidget()
#         self.setMenuWidget(central_widget)

#         # Create a layout for the app bar
#         appbar_layout = QHBoxLayout()

#         # Add additional buttons or widgets as needed
#         # For example, a button for some action
#         self.action_button = QPushButton("Back", self)
#         self.action_button.setFixedSize(100, 30)  # Set width and height
#         self.action_button.setStyleSheet(
#             "background-color: #7D7C7C; color: white; padding: 10px 20px; border: none; border-radius: 5px;"
#         )
#         appbar_layout.addWidget(self.action_button)

#         # Create a label for the app bar title
#         appbar_title = QLabel("EcoCraft", self)
#         appbar_title.setStyleSheet("font-size: 16px;")
#         appbar_title.setAlignment(Qt.AlignCenter)
#         appbar_layout.addWidget(appbar_title)
#         # Set the background color of the app bar
#         appbar_widget = QWidget()
#         appbar_widget.setStyleSheet(
#             "background-color: #F1EFEF; color: Black; border: none; border-radius: 5px;"
#         )  # Set background color to black
#         appbar_widget.setLayout(appbar_layout)

#         layout = QHBoxLayout(central_widget)
#         layout.addWidget(appbar_widget)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.showMaximizedMaximized()
#     sys.exit(app.exec_())
