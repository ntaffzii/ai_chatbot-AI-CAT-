from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import os
import Language as ln

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.lang_manager = ln.Language_all()
        self.image_logo = os.path.join("./Photo", "CatLogo.png")
        self.image_eEarth = os.path.join("./Photo", "earth.png")
        self.setWindowIcon(QIcon(self.image_logo))
        self.setWindowTitle("Sign in Cat! ChatBot")
        self.setGeometry(300, 200, 300, 150)

        layout = QVBoxLayout()

        # สร้าง QToolBar
        self.create_toolbar(layout)

        self.label = QLabel(self.lang_manager.translate("label_login"))
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText(self.lang_manager.translate("username_input"))
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText(self.lang_manager.translate("password_input"))
        self.password_input.setEchoMode(QLineEdit.Password)  
        self.login_button = QPushButton(self.lang_manager.translate("login_Button"))

        layout.addWidget(self.label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        
        self.setLayout(layout)

        self.login_button.clicked.connect(self.login)  # กดแล้วปิด Dialog

    def create_toolbar(self, layout):
        toolbar = QToolBar("Login Toolbar")
        layout.addWidget(toolbar)

        # เพิ่มปุ่มใน QToolBar
        lang_button = QAction(QIcon(self.image_eEarth), self.lang_manager.translate("language"), self)
        lang_button.triggered.connect(self.toggle_language)
        toolbar.addAction(lang_button)

        # เพิ่มข้อความด้านข้างของปุ่ม
        self.lang_label = QLabel(self.lang_manager.translate("language_Change"))
        toolbar.addWidget(self.lang_label)

    def toggle_language(self):
        """เปลี่ยนภาษาไทย ↔ อังกฤษ"""
        new_lang = "en" if self.lang_manager.language == "th" else "th"
        self.lang_manager.set_language(new_lang)
        self.update_ui()

    def update_ui(self):
        self.label.setText(self.lang_manager.translate("label_login"))
        self.username_input.setPlaceholderText(self.lang_manager.translate("username_input"))
        self.password_input.setPlaceholderText(self.lang_manager.translate("password_input"))
        self.login_button.setText(self.lang_manager.translate("login_Button"))
        self.lang_label.setText(self.lang_manager.translate("language_Change"))

    def login(self):
        self.user_password = {"Admin": "123456","Goku":"2548","stu67": "1234"}
        
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        if username in self.user_password:
            if password == self.user_password[username]:
                QMessageBox.information(self, "Login", self.lang_manager.translate("userpass_login"))
                self.accept()
            else:
                QMessageBox.information(self, "Login", self.lang_manager.translate("userpass_loginF"))
        else:
            QMessageBox.information(self, "Login", self.lang_manager.translate("fulluser_login"))