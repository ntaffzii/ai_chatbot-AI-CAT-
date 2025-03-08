from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import os

class ChatBubble(QWidget):
    def __init__(self, sender, username, message):
        super().__init__()
        self.sender = sender  # เก็บข้อมูลผู้ส่ง (user หรือ ai)
        self.message = message  # เก็บข้อความ
        self.username = username  # เก็บชื่อผู้ส่ง (สำหรับผู้ใช้)

        bubble_layout = QHBoxLayout()

        # ชื่อของผู้ส่ง (User หรือ AI)
        sender_name = QLabel(username if sender == "user" else "CAT AI")
        sender_name.setAlignment(Qt.AlignCenter)

        image_path = os.path.join("./Photo", "user.png")  # สร้างเส้นทางแบบสมบูรณ์
        image_pathAI = os.path.join("./Photo", "CatLogo.png")
        avatar = QLabel()
        avatar_ai = QLabel()
        avatar.setFixedSize(50, 50)
        avatar.setPixmap(QPixmap(image_path).scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        avatar_ai.setPixmap(QPixmap(image_pathAI).scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        # กล่องข้อความ
        message_box = QLabel(message)
        message_box.setWordWrap(True)
        message_box.setFixedWidth(300)

        # ตั้งค่า objectName เพื่อใช้กับ stylesheet
        if sender == "user":
            sender_name.setObjectName("Sender_name")
            message_box.setObjectName("ChatBubbleUser")
        else:
            sender_name.setObjectName("Sender_name")
            message_box.setObjectName("ChatBubbleAI")

        # Layout สำหรับ Avatar และชื่อผู้ส่ง
        avatar_layout = QVBoxLayout()
        avatar_layout_ai = QVBoxLayout()
        avatar_layout.addWidget(avatar)
        avatar_layout_ai.addWidget(avatar_ai)
        avatar_layout.addWidget(sender_name)
        avatar_layout_ai.addWidget(sender_name)
        
        # จัดวาง Layout ตามผู้ส่ง
        if sender == "user":
            chat_layout = QHBoxLayout()
            chat_layout.addStretch()
            chat_layout.addWidget(message_box)
            chat_layout.addLayout(avatar_layout)
            bubble_layout.addLayout(chat_layout)
        else:
            chat_layout = QHBoxLayout()
            chat_layout.addLayout(avatar_layout_ai)
            chat_layout.addWidget(message_box)
            chat_layout.addStretch()
            bubble_layout.addLayout(chat_layout)

        self.setLayout(bubble_layout)