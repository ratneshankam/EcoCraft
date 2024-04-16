import sys
import firebase_admin
from firebase_admin import credentials, storage
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QDesktopWidget,
    QGroupBox,
    QListWidget,
    QListWidgetItem,
    QSplitter,
    QScrollArea,
    QGridLayout,
    QGraphicsDropShadowEffect,
)
from PyQt5.QtGui import QPixmap,QColor
from PyQt5.QtCore import Qt
from addCartUpdate import CartView, AddToCartUI, MainCartApp


class MainWindow(QMainWindow):
    def __init__(self, firebase_app, description, image_label, show_main_window):

        super().__init__()
        self.setWindowTitle("Product Purchase")

        # # Initialize Firebase Admin SDK
        # cred = credentials.Certificate("ecocraft-team-firebase-adminsdk-c931h-31a37bfd3f.json")  # Replace with your service account key
        # self.firebase_app = firebase_admin.initialize_app(cred, {'storageBucket': 'ecocraft-team.appspot.com'})
        self.firebase_app = firebase_app
        self.description = description

        self.file_path = image_label
        # self.image_path = image_label


        # added now
        self.show_main_window1 = show_main_window
        desktop = QDesktopWidget()
        primary_screen = desktop.screenGeometry(desktop.primaryScreen())
        # Retrieve the width and height of the monitor
        monitor_width = primary_screen.width()
        monitor_height = primary_screen.height()

        self.setObjectName("Widget")
        self.resize(monitor_width, monitor_height)
        self.c2w_widget = QWidget(self)
        self.c2w_widget.setGeometry(0, 0, monitor_width, 50)

        self.setStyleSheet("background-color: white;")

        self.init_ui()

    def init_ui(self):
        # Set up the app bar
        self.setup_appbar()

        # Set up the main content
        self.setup_content()

    def setup_appbar(self):
        # Create a central widget
        central_widget = QWidget()
        self.setMenuWidget(central_widget)

        # Create a layout for the app bar
        appbar_layout = QHBoxLayout()

        # Add additional buttons or widgets as needed
        # For example, a button for some action
        self.action_button = QPushButton("Back", self)
        self.action_button.setFixedSize(100, 30)  # Set width and height
        self.action_button.setStyleSheet(
            "background-color: #7D7C7C; color: white; padding: 10px 20px; border: none; border-radius: 5px;"
        )
        appbar_layout.addWidget(self.action_button)

        # Create a label for the app bar title
        appbar_title = QLabel("EcoCraft", self)
        appbar_title.setStyleSheet("font-size: 16px;")
        appbar_title.setAlignment(Qt.AlignCenter)
        appbar_layout.addWidget(appbar_title)
        # Set the background color of the app bar
        appbar_widget = QWidget()
        appbar_widget.setStyleSheet(
            "background-color: #F1EFEF; color: Black; border: none; border-radius: 5px;"
        )  # Set background color to black
        appbar_widget.setLayout(appbar_layout)

        layout = QHBoxLayout(central_widget)
        layout.addWidget(appbar_widget)

    def setup_content(self):
        # Create a central widget for the main content
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main horizontal layout
        main_layout = QHBoxLayout(central_widget)

        # Left side: Procedure
        procedure_box = QGroupBox("Basic Idea Procedure", self)
        procedure_box.setStyleSheet("background-color: #f888f0; padding: 10px; ")
        procedure_layout = QVBoxLayout()
        self.image_label = QLabel()
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
        if self.file_path:
            pixmapUpload = QPixmap(self.file_path)
            pixmapUpload = pixmapUpload.scaledToWidth(200, Qt.SmoothTransformation)
            self.image_label.setPixmap(pixmapUpload)
            self.image_label.setAlignment(Qt.AlignCenter)
        procedure_layout.addWidget(self.image_label)

        if self.description == "bottles" or self.description == "bottle":
            procedure_label = QLabel(
                """
Step1 (Prepare the Bottle):
    Clean the bottle thoroughly and remove labels and adhesive residue.\n
Step2 (Design and Plan):
    Decide on the artifact you want to create and sketch out your design.\n
Step3 (Cut and Shape):
    Use appropriate tools to cut and shape the bottle according to your design.\n
Step4 (Decorate):
    Paint or decorate the bottle as desired.\n
Step5 (Finish and Display):
    Smooth out any rough edges, apply a sealant if needed, and display your finished artifact.""",
                self,
            )
        elif self.description == "pens" or self.description == "pen":
            procedure_label = QLabel(
                """
Step1 (Disassemble):
    Disassemble the pens, separating the components such as the outer casing, ink cartridge, and spring.\n
Step2 (Reassemble Creatively):
    Arrange the pen components in a creative way to form a new artifact, such as a sculpture or functional item like a pen holder.\n
Step3 (Secure and Adhere):
    Use glue, tape, or other adhesives to secure the pen components together in the desired configuration.\n
Step4 (Decorate):
    Add embellishments or paint the pen artifact to customize its appearance.\n
Step5 (Display or Use):
    Once finished, display your pen artifact as a unique piece of art or use it for its intended purpose.""",
                self,
            )
        elif self.description == "bangles" or self.description == "bangle":
            procedure_label = QLabel(
                """
Step1 (Clean and Sort):
    Clean the bangles and sort them based on size, color, and material.\n
Step2 (Design Concept):
    Determine the type of artifact you want to create from the bangles, such as a decorative wall hanging, jewelry, or a mosaic.\n
Step3 (Arrange and Adhere):
    Arrange the bangles in the desired pattern or configuration for your artifact.
    Use glue, wire, or other adhesives to secure the bangles together.\n
Step4 (Embellish):
    Add additional elements like beads, sequins, or ribbons to enhance the appearance of the bangle artifact.\n
Step5 (Embellish and Display):
    Ensure all bangles are securely attached and any embellishments are firmly in place.
    Your finished bangle artifact is ready to be displayed as a unique piece of decor or worn as jewelry.""",
                self,
            )
        elif self.description == "Clothes" or self.description == "clothes" or self.description == "cloth":
            procedure_label = QLabel(
                """
Step1 (Sort and Clean):
	Sort through the clothes, separating them based on material, color, and condition.
	Wash and dry the clothes to ensure they are clean and free from stains or odors.

Step2 (Design Concept):
	Determine what type of artifact you want to create from the clothes, such as a quilt, bag, or patchwork art.

Step3 (Cut and Sew):
	Cut the clothes into pieces according to your design.
	Use a sewing machine or needle and thread to stitch the pieces together to create the desired artifact.

Step4 (Embellish):
	Add embellishments like buttons, embroidery, or patches to enhance the appearance of the artifact.

Step5 (Finish and Use):
	Trim any loose threads and ensure all seams are secure.
	Your finished artifact is ready to use or display.
""",
                self,
            )
        elif self.description == "papers" or self.description == "paper":
            procedure_label = QLabel(
                """
Step1 (Select and Prepare):
	Gather various types of paper waste such as newspapers, magazines, or cardboard.
	Flatten and smooth out the paper to remove wrinkles and creases.

Step2 (Design and Fold):
	Decide on the type of paper artifact you want to create, such as origami, paper sculpture, or papier-mâché.

Step3 (Fold and Shape):
	Fold the paper according to your chosen design, following instructions for origami or shaping techniques for sculptures.

Step4 (Adorn):
	Add color, paint, or decorative elements to the paper artifact to enhance its appearance.

Step5 (Display or Use):
	Once completed, display your paper artifact as a piece of art or use it for its intended purpose.""",
                self,
            )
        else:
            procedure_label = QLabel(
                "Here goes the basic idea procedure.",
                self,
            )

        procedure_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        procedure_label.setWordWrap(True)
        procedure_label.setAlignment(Qt.AlignTop)
        procedure_layout.addWidget(procedure_label)
        procedure_box.setLayout(procedure_layout)
        procedure_box.setStyleSheet(
            "font-size: 12px; background-color: #f0f0f0; padding: 10px; margin: 10px;"
        )
        procedure_box.setMaximumWidth(600)

        # Right side: Scrollable containers
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        containers_widget = QListWidget(self)

        # Add containers
        for i in range(1, 8):  # Example: Adding 15 containers
            container_item = QListWidgetItem(containers_widget)
            if self.description == "bottles":
                container_box = self.create_container(
                    f"Container {i}", f"images/{self.description}{i}.jpg", i*2
                )
            elif self.description == "bottle":
                container_box = self.create_container(
                    f"Container {i}", f"images/{self.description}s{i}.jpg", i*2
                )
            elif self.description == "pen":
                container_box = self.create_container(
                    f"Container {i}", f"images/{self.description}s{i}.jpg", i*2
                )
            elif self.description == "bangle":
                container_box = self.create_container(
                    f"Container {i}", f"images/{self.description}s{i}.jpg", i*2
                )
            elif self.description == "paper":
                container_box = self.create_container(
                    f"Container {i}", f"images/{self.description}s{i}.jpg", i*2
                )
            elif self.description == "cloth":
                self.description = "Clothes"
                container_box = self.create_container(
                    f"Container {i}", f"images/Clothes{i}.jpg", i*2
                )
            elif self.description == "clothes":
                self.description = "Clothes"
                container_box = self.create_container(
                    f"Container {i}", f"images/Clothes{i}.jpg", i*2
                )
            elif self.description == "pens":
                container_box = self.create_container(
                    f"Container {i}", f"images/{self.description}{i}.jpg", i*2
                )
            elif self.description == "bangles":
                container_box = self.create_container(
                    f"Container {i}", f"images/{self.description}{i}.jpg", i*2
                )
            elif self.description == "Clothes":
                container_box = self.create_container(
                    f"Container {i}", f"images/{self.description}{i}.jpg", i*2
                )
            elif self.description == "papers":
                container_box = self.create_container(
                    f"Container {i}", f"images/{self.description}{i}.jpg", i*2
                )
            else:
                container_box = self.create_container(
                    f"Container {i}", f"images/{i}.jpg", i*2
                )
            container_item.setSizeHint(container_box.sizeHint())
            containers_widget.addItem(container_item)
            containers_widget.setItemWidget(container_item, container_box)

        scroll_area.setWidget(containers_widget)

        # Add procedure box and scroll area to splitter
        splitter = QSplitter(self)
        splitter.addWidget(procedure_box)
        splitter.addWidget(scroll_area)

        main_layout.addWidget(splitter)

    def create_container(self, name, image_path, mrp):
        # print("value is ", mrp)           #.................
        container_box = QGroupBox(name, self)
        container_layout = QVBoxLayout()  # Vertical layout for the container

        # Horizontal layout for the row
        row_layout = QHBoxLayout()

        # Add image label
        image_label = QLabel(self)
        self.download_image(
            image_label,
            image_path,
        )

        # Set fixed size for the image label
        image_label.setFixedSize(300, 400)  # Adjust size as needed
        image_label.setAlignment(Qt.AlignCenter)

        # Add the image label to the row layout
        row_layout.addWidget(image_label)

        # Vertical layout for the labels and button
        label_button_layout = QVBoxLayout()

        # MRP label
        self.mrp = mrp
        # print(self.mrp)                           #.................
        mrp_label = QLabel(f"MRP: ${self.mrp}", self)
        mrp_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        mrp_label.setAlignment(Qt.AlignCenter)
        mrp_label.setFixedSize(270, 100)

        # Buy Now button
        buy_now_button = QPushButton("Buy Now", self)
        buy_now_button.clicked.connect(lambda: self.add_cart(image_path, self.mrp))
        buy_now_button.setStyleSheet(
            "font-size: 18px; background-color: #008CBA; color: white; padding: 10px 20px; border: none; border-radius: 5px;"
        )

        # Add MRP label and Buy Now button to the vertical layout
        label_button_layout.addWidget(mrp_label)
        label_button_layout.addWidget(buy_now_button)

        # Add the label and button layout to the row layout
        row_layout.addLayout(label_button_layout)

        # Add the row layout to the container layout
        container_layout.addLayout(row_layout)

        container_box.setLayout(container_layout)
        container_box.setStyleSheet(
            "padding: 10px; margin: 10px; background-color: #f8f8f8; border: 1px solid #d0d0d0; border-radius: 5px;"
        )

        return container_box

    def add_cart(self, buy_image_path, value):
        self.mainwindow =  MainWindow(
            self.firebase_app, self.description, self.file_path, self.show_main_window1
        )
        self.main_app = MainCartApp(value, buy_image_path, self.description, self.mainwindow)
        self.main_app.showMaximized()
        self.mainwindow.close()
        # print(self.close())

    def download_image(self, label, image_path):
        try:
            bucket = storage.bucket(
                app=self.firebase_app
            )  # Access Firebase Storage bucket
            blob = bucket.blob(
                image_path
            )  # Replace with the correct path to your image

            image_bytes = blob.download_as_bytes()
            pixmap = QPixmap()
            pixmap.loadFromData(image_bytes)
            pixmap = pixmap.scaledToWidth(400, Qt.SmoothTransformation)

            label.setPixmap(pixmap)
            label.setAlignment(Qt.AlignCenter)
        except Exception as e:
            print("Error downloading image:", e)
            label.setText("Image Not Found")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
