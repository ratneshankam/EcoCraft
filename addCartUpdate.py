import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QTabWidget,
    QMessageBox,
    QSizePolicy,
    QMainWindow,
    QStackedWidget
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

# from purchase import MainWindow


class CartView(QWidget):
    def __init__(self, landing_image_label, description):

        super().__init__()

        self.landing_image_label = landing_image_label
        self.description = description
        self.cart_items = []

        self.setStyleSheet("background-color: #ffffff;")

        self.setWindowIcon(QIcon("assets/images/hand-made.png"))

        self.init_ui()

    def init_ui(self):

        self.cart_label = QLabel(f"Selected Products for Payment: {self.description}")
        self.cart_display = QLabel()
        self.cart_label.setStyleSheet(
            "font-weight: bold;color: #000000;font-size: 25px;"
        )

        self.payment_button = QPushButton("Proceed to Payment")
        self.payment_button.setMaximumWidth(350)
        self.payment_button.setStyleSheet(
            """background-color: #27ae60;
            color: white;
            border: 1px solid #27ae60;
            padding: 8px;
            font-size: 25px;border-radius: 5px;"""
        )
        self.payment_button.clicked.connect(self.proceed_to_payment)

        layout = QVBoxLayout()
        layout.addWidget(self.cart_label)
        info_layout = QHBoxLayout()

        self.setLayout(layout)

        image_label = QLabel(self)
        image_label.setFixedSize(300, 400)  # Adjust size as needed
        image_label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(f"assets/" + self.landing_image_label)

        pixmap = pixmap.scaledToHeight(200, Qt.SmoothTransformation)
        pixmap = pixmap.scaledToWidth(200, Qt.SmoothTransformation)

        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)

        info_layout.addWidget(self.cart_display)
        info_layout.addWidget(image_label)
        info_layout.addWidget(QLabel("\n\n"))
        layout.addLayout(info_layout)
        layout.addWidget(self.payment_button)
        layout.addWidget(QLabel("\n\n\n\n"))

    def is_cart_empty(self):
        return not bool(self.cart_items)

    def add_to_cart(self, product_name, price, quantity):
        self.cart_items.append(
            {"Product": product_name, "Price": price, "Quantity": quantity}
        )
        self.update_cart_display()

    def update_cart_display(self):
        cart_text = "\n".join(
            [
                f"{item['Quantity']}x {item['Product']} - ${float(item['Price'][1:]) * int(item['Quantity']):.2f}"
                for item in self.cart_items
            ]
        )

        self.cart_display.setText(cart_text)
        self.cart_display.setAlignment(Qt.AlignCenter)
        self.cart_display.setStyleSheet("font-size: 18px;")

    def clear_cart(self):
        self.cart_items = []
        self.update_cart_display()

    def proceed_to_payment(self):
        if self.is_cart_empty():
            self.show_notification(
                "Please select at least one product before proceeding to payment"
            )
        else:

            total_amount = sum(
                [
                    float(item["Price"][1:]) * int(item["Quantity"])
                    for item in self.cart_items
                ]
            )
            # print(f"Total Amount: ${total_amount:.2f}")                   #.................
            self.show_notification("Payment Successful")
            self.clear_cart()

    def show_notification(self, message):
        QMessageBox.information(self, "Notification", message)


class AddToCartUI(QWidget):
    def __init__(self, cart_view, mrp, landing_image_label, description):
        super().__init__()

        self.cart_view = cart_view
        self.mrp = mrp
        self.landing_image_label = landing_image_label
        self.description = description
        self.setStyleSheet("background-color: #ffffff;")
        self.setWindowIcon(QIcon("assets/images/hand-made.png"))

        if (self.landing_image_label == f"images/{self.description}1.jpg") or (self.landing_image_label == f"images/{self.description}s1.jpg"):
            self.mrp = 2 * 1
        elif self.landing_image_label == f"images/{self.description}2.jpg" or (self.landing_image_label == f"images/{self.description}s2.jpg"):
            self.mrp = 2 * 2
        elif self.landing_image_label == f"images/{self.description}3.jpg" or (self.landing_image_label == f"images/{self.description}s3.jpg"):
            self.mrp = 2 * 3
        elif self.landing_image_label == f"images/{self.description}4.jpg" or (self.landing_image_label == f"images/{self.description}s4.jpg"):
            self.mrp = 2 * 4
        elif self.landing_image_label == f"images/{self.description}5.jpg" or (self.landing_image_label == f"images/{self.description}s5.jpg"):
            self.mrp = 2 * 5
        elif self.landing_image_label == f"images/{self.description}6.jpg" or (self.landing_image_label == f"images/{self.description}s6.jpg"):
            self.mrp = 2 * 6
        elif self.landing_image_label == f"images/{self.description}7.jpg" or (self.landing_image_label == f"images/{self.description}s7.jpg"):
            self.mrp = 2 * 7
        elif self.landing_image_label == f"images/{self.description}8.jpg" or (self.landing_image_label == f"images/{self.description}s8.jpg"):
            self.mrp = 2 * 8

        self.product_label = QLabel(f"Product Name: {self.description}")
        self.price_label = QLabel(f"Price: ${self.mrp}")
        self.price_label.setStyleSheet(
            """
            color: #e74c3c; /* Red color for price label */
            font-size: 18px;
            """
        )
        self.price_label.setAlignment(Qt.AlignCenter)

        self.quantity_label = QLabel("Quantity:")
        self.quantity_label.setAlignment(Qt.AlignCenter)
        self.quantity_label.setStyleSheet("font-size: 18px;")
        self.quantity_button = QPushButton("+")
        self.quantity_display = QLabel("0")
        self.add_to_cart_button = QPushButton("Add to Cart")

        self.setStyleSheet(
            """
            background-color: #ffffff;
            color: #333;
            font-family: 'Arial', sans-serif;
            font-size: 14px;
        """
        )

        self.product_label.setStyleSheet(
            "font-weight: bold; color: #000000; font-size: 25px;"
        )

        self.quantity_button.setStyleSheet(
            """
            background-color: #27ae60;
            color: white;
            border: 1px solid #27ae60;
            padding: 8px;
            font-size: 25px;border-radius: 5px;
                                           
                                           
        """
        )

        self.add_to_cart_button.setStyleSheet(
            """
            background-color: #3498db;
            color: white;
            border: 1px solid #3498db;
            padding: 12px;
            font-size: 16px;
            font-weight: bold;border-radius: 5px;
                                              
        """
        )

        layout = QVBoxLayout()

        info_layout = QHBoxLayout()
        info_layout.addWidget(self.product_label)
        image_label = QLabel(self)
        image_label.setFixedSize(300, 400)  # Adjust size as needed
        image_label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(f"assets/" + self.landing_image_label)

        pixmap = pixmap.scaledToHeight(200, Qt.SmoothTransformation)
        pixmap = pixmap.scaledToWidth(200, Qt.SmoothTransformation)

        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        info_layout.addWidget(image_label)
        info_layout.addWidget(QLabel("\n\n"))

        # info_layout.addWidget(self.price_label)

        quantity_layout = QHBoxLayout()

        quantity_layout.addWidget(self.price_label)
        quantity_layout.addWidget(self.quantity_label)
        quantity_layout.addWidget(self.quantity_button)
        quantity_layout.addWidget(self.quantity_display)

        button_layout = QVBoxLayout()
        button_layout.addWidget(
            self.add_to_cart_button,
        )
        # button_layout.addWidget(self.add_to_cart_button, 550, Qt.AlignHCenter)
        # button_layout.setAlignment(Qt::AlignCenter)

        layout.addLayout(info_layout)
        # layout.addWidget(self.product_label)
        # layout.addWidget(self.price_label)
        layout.addLayout(quantity_layout)
        layout.addLayout(button_layout)
        layout.addWidget(QLabel("\n\n\n\n"))

        self.quantity_button.setMaximumWidth(150)
        self.add_to_cart_button.setMaximumWidth(250)

        self.quantity_button.clicked.connect(self.increment_quantity)
        self.add_to_cart_button.clicked.connect(self.add_to_cart)

        self.setLayout(layout)

    def increment_quantity(self):
        current_quantity = int(self.quantity_display.text())
        new_quantity = current_quantity + 1
        self.quantity_display.setText(str(new_quantity))

    def add_to_cart(self):
        if int(self.quantity_display.text()) == 0:
            self.cart_view.show_notification(
                "Please select at least one product before adding to cart"
            )
        else:
            product_name = self.product_label.text().split(":")[1].strip()
            price = self.price_label.text().split(":")[1].strip()
            quantity = self.quantity_display.text()

            self.cart_view.add_to_cart(product_name, price, quantity)
            self.cart_view.show_notification(
                f"Added to Cart: {quantity}x {product_name}"
            )
            # Clear the quantity display after adding to cart
            self.quantity_display.setText("0")


class MainCartApp(QMainWindow):
    def __init__(self, mrp, landing_image_label, description, mainwindow_obj):
        super().__init__()
        self.mainwindow_obj = mainwindow_obj
        self.mrp = mrp
        self.description = description
        self.landing_image_label = landing_image_label
        self.setStyleSheet("background-color: white;")
        self.stacked_widget = QStackedWidget()
        
        self.setCentralWidget(self.stacked_widget)
        
        self.main_window_widget = QWidget()
        
        tab_widget = QTabWidget(self)
        self.setWindowTitle("Welcome")


        self.setWindowIcon(QIcon("assets/images/hand-made.png"))

        cart_view_tab = CartView(self.landing_image_label, self.description)
        add_to_cart_tab = AddToCartUI(
            cart_view_tab, self.mrp, self.landing_image_label, self.description
        )

        tab_widget.addTab(add_to_cart_tab, "Add to Cart")
        tab_widget.addTab(cart_view_tab, "Cart View")

        layout = QVBoxLayout()
        # self.action_button = QPushButton("Back", self)
        # self.action_button.setFixedSize(100, 30)  # Set width and height
        # self.action_button.clicked.connect(self.open_second_window)
        # layout.addWidget(self.action_button)
        
        # Create a layout for the app bar
        appbar_layout = QHBoxLayout()

        # Add additional buttons or widgets as needed
        # For example, a button for some action
        self.action_button = QPushButton("Back", self)
        self.action_button.setFixedSize(100, 30)  # Set width and height
        self.action_button.clicked.connect(self.open_second_window)
        
        self.action_button.setStyleSheet(
            "background-color: #7D7C7C; color: white; padding: 10px 20px; border: none; border-radius: 5px;"
        )
        appbar_layout.addWidget(self.action_button)

        # Create a label for the app bar title
        appbar_title = QLabel("EcoCraft(payment)", self)
        appbar_title.setStyleSheet("font-size: 16px;")
        appbar_title.setAlignment(Qt.AlignCenter)
        appbar_layout.addWidget(appbar_title)
        # Set the background color of the app bar
        appbar_widget = QWidget()
        appbar_widget.setStyleSheet(
            "background-color: #F1EFEF; color: Black; border: none; border-radius: 5px;"
        )  # Set background color to black
        appbar_widget.setLayout(appbar_layout)
        
        
        # adding layout
        layout.addWidget(appbar_widget)
        layout.addWidget(tab_widget)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # self.setLayout(vertical_widget)
        self.main_window_widget.setLayout(layout)
        
        self.stacked_widget.addWidget(self.main_window_widget)
        

        self.action_button.setStyleSheet(
            "font-size:12px; background-color: #7D7C7C; color: white; padding: 10px 20px; border: none; border-radius: 5px;"
        )
        
    def show_main_window(self):
        self.stacked_widget.setCurrentWidget(self.main_window_widget)

    def open_second_window(self):
        self.second_window = self.mainwindow_obj
        self.action_button.clicked.connect(self.show_main_window)
        self.stacked_widget.addWidget(self.second_window)
        self.stacked_widget.setCurrentWidget(self.second_window)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainCartApp()
    main_app.showMaximized()
    sys.exit(app.exec_())
