from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import Chat_Bubble as cb

class ChatManager():
    def __init__(self, chat_layout, chat_display_area, lang_manager):
        self.chat_layout = chat_layout
        self.chat_display_area = chat_display_area
        self.lang_manager = lang_manager

    def add_chat_bubble(self, sender, username, message):
        bubble_widget = cb.ChatBubble(sender, username, message)
        self.chat_layout.addWidget(bubble_widget)
        self.chat_display_area.verticalScrollBar().setValue(
            self.chat_display_area.verticalScrollBar().maximum()
        )
        
    def save_chat_to_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(None, "บันทึกแชท", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                for i in range(self.chat_layout.count()):
                    widget = self.chat_layout.itemAt(i).widget()
                    if isinstance(widget, cb.ChatBubble):  # ตรวจสอบว่าเป็น ChatBubble หรือไม่
                        # ดึงข้อความและผู้ส่งจาก ChatBubble
                        sender_name = widget.username if widget.sender == "user" else "CAT AI"
                        message = widget.message
                        file.write(f"{sender_name}: {message}\n")
            QMessageBox.information(None, "Successful", self.lang_manager.translate("save_chat_to_file"))

    def save_chat_to_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(None, "บันทึกเป็นภาพ", "", "PNG Files (*.png);;All Files (*)", options=options)

        if file_path:
            pixmap = QPixmap(self.chat_layout.parentWidget().size())  # สร้างภาพตามขนาดของแชท
            self.chat_layout.parentWidget().render(pixmap)  # แคปหน้าจอเฉพาะพื้นที่ของแชท
            pixmap.save(file_path, "PNG")  # บันทึกเป็นไฟล์ PNG
            QMessageBox.information(None, "Successful", self.lang_manager.translate("save_chat_to_image"))

    def update_ui(self):
        """อัปเดต UI หลังจากเปลี่ยนภาษา"""
        # อัปเดตข้อความใน UI ที่เกี่ยวข้องกับ ChatManager
        pass  # เพิ่มโค้ดที่จำเป็นสำหรับการอัปเดต UI ที่นี่