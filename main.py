import sys
import DataChat as d
import os
import json
import Language as ln
import Settings_dialog as sd
import Chat_Bubble as cb
import Chat_Manager as cm
import LoginDialog as ld
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class OOPChat(QMainWindow):
    def __init__(self):
        super().__init__()

        # สถานะของโหมดมืด
        self.dark_mode_enabled = False
        self.toggle_dark_mode()
        # ✅ เรียก LoginDialog เพื่อให้ผู้ใช้ใส่ชื่อก่อน
        self.username = self.show_login_dialog()
        
        if not self.username:
            sys.exit(0)  # ปิดโปรแกรมถ้าไม่ได้ใส่ชื่อ
            
        self.lang_manager = ln.Language_all()
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.image_logo = os.path.join("./Photo", "user.png")
        self.image_logoai = os.path.join("./Photo", "CatLogo.png")
        self.setWindowTitle("CAT! Chatbot")
        self.setGeometry(100, 100, 700, 800)
        self.setWindowIcon(QIcon(self.image_logoai))
        self.create_central_widget()
        self.load_chat_list()
        self.show()

    def show_login_dialog(self):
        dialog = ld.LoginDialog()
                
        if dialog.exec():
            return dialog.username_input.text().strip()
        return None

    def toggle_dark_mode(self):
        """เปิด/ปิดโหมดมืด"""
        if self.dark_mode_enabled:
            # กลับไปโหมดสว่าง
            self.setStyleSheet("""
                QListWidget {
                    background-color: #bdbdbd;
                    border-radius: 5px;
                    padding: 5px;
                    font-size: 16px;
                    color: black;
                }
                QMainWindow {
                    background-color: #f5f5f5; /* สีพื้นหลังโหมดสว่าง */
                }

                QLabel {
                    font-size: 16px;
                }
                QLabel#username_label {
                    color: black; font-size: 16px; font-weight: bold;
                }
                
                QLabel#Sender_name {
                    font-size: 16px; 
                    font-weight: bold; 
                    color: black;
                }

                QLineEdit {
                    background-color: #ffffff; /* สีพื้นหลังช่องข้อความ */
                    color: black;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    padding: 5px;
                }

                QPushButton {
                    background-color: #e0e0e0;
                    color: black;
                    border: 1px solid #bbb;
                    border-radius: 5px;
                    padding: 5px;
                }
                QPushButton#delete_button {
                    font-size: 16px;    
                }
                QPushButton:hover {
                    background-color: #d6d6d6;
                    border: 1px solid #aaa;
                }

                /* ปรับสีของ ChatBubble */
                QWidget#ChatBubbleUser {
                    background-color: #e0e0e0; /* พื้นหลังของข้อความผู้ใช้ */
                    color: black;
                    border-radius: 10px;
                    padding: 10px;
                    font-size: 16px;
                }

                QWidget#ChatBubbleAI {
                    background-color: #dcdcdc; /* พื้นหลังของข้อความ AI */
                    color: black;
                    border-radius: 10px;
                    padding: 10px;
                    font-size: 16px;
                }
                QWidget#Chat_layout {
                    background-color: #bdbdbd;
                    border-radius: 5px;
                    padding: 5px;
                }
                
            """)
            self.dark_mode_enabled = False
        else:
            # เปลี่ยนเป็นโหมดมืด
            self.setStyleSheet("""
                QListWidget {
                    background-color: #1E1E1E;
                    border-radius: 5px;
                    padding: 5px;
                    font-size: 16px;
                    color: white;
                }
                QMainWindow {
                    background-color: #000000; /* พื้นหลังสีดำ */
                }
                QLabel {
                    color: white; /* ข้อความสีขาว */
                    font-size: 16px;
                }
                QLabel#username_label {
                    color: white; font-size: 16px; font-weight: bold;
                }
                QLabel#Sender_name {
                    font-size: 16px; 
                    font-weight: bold; 
                    color: white;
                }

                QLineEdit {
                    background-color: #1E1E1E;
                    color: white;
                    border: 1px solid #333;
                    border-radius: 5px;
                    padding: 5px;
                }

                QPushButton {
                    background-color: #1E1E1E;
                    color: white;
                    border: 1px solid #444;
                    border-radius: 5px;
                    padding: 5px;
                }
                QPushButton#delete_button {
                    font-size: 16px;    
                }
                QPushButton:hover {
                    background-color: #444;
                    border: 1px solid #555;
                }

                /* ปรับสีของ ChatBubble */
                QWidget#ChatBubbleUser {
                    background-color: #424242; /* พื้นหลังของข้อความผู้ใช้ */
                    color: white;
                    border-radius: 10px;
                    padding: 10px;
                    font-size: 16px;
                }

                QWidget#ChatBubbleAI {
                    background-color: #333333; /* พื้นหลังของข้อความ AI */
                    color: white;
                    border-radius: 10px;
                    padding: 10px;
                    font-size: 16px;
                }
                """)
                
            self.dark_mode_enabled = True

    def create_central_widget(self):
        central_widget = QWidget(self)
        main_layout = QHBoxLayout()

        left_sidebar = QVBoxLayout()
        left_sidebar.setAlignment(Qt.AlignTop)

        # ✅ แสดงชื่อผู้ใช้
        self.username_label = QLabel(f"👤 {self.username}")
        self.username_label.setAlignment(Qt.AlignCenter)
        self.username_label.setObjectName("username_label")

        # ✅ รูปโปรไฟล์
        self.logo_label = QLabel()
        pixmap = QPixmap(self.image_logo).scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_label.setPixmap(pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)

        left_sidebar.addWidget(self.username_label)  # แสดงชื่อ
        left_sidebar.addWidget(self.logo_label)  # แสดงรูป

        # ✅ ปุ่มเมนู
        self.chat_button = QPushButton(self.lang_manager.translate("chat_button"))
        self.chat_button.clicked.connect(self.load_chat_list)
        self.settings_button = QPushButton(self.lang_manager.translate("settings_button"))
        self.logout_button = QPushButton(self.lang_manager.translate("logout_button"))
        self.logout_button.clicked.connect(self.exit_login)
        
        self.lang_button = QPushButton(self.lang_manager.translate("language"))
        self.lang_button.clicked.connect(self.toggle_language)
        
        self.chat_list = QListWidget()
        self.chat_list.itemClicked.connect(self.load_selected_chat)
        self.chat_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.chat_list.customContextMenuRequested.connect(self.show_context_menu)
        left_sidebar.addWidget(self.chat_list)

        # เพิ่มปุ่มลบไฟล์
        self.delete_button = QPushButton(self.lang_manager.translate("🗑️ Delete Chat"))
        self.delete_button.setObjectName("delete_button")
        self.delete_button.clicked.connect(self.delete_selected_chat)
        left_sidebar.addWidget(self.delete_button)
        
        for button in [self.chat_button, self.lang_button]:
            button.setStyleSheet("font-size: 16px; padding: 10px;")
            left_sidebar.addWidget(button)

        left_sidebar.addStretch()

        # ✅ ปุ่ม "บันทึกแชท" พร้อมเมนู
        self.save_button = QPushButton(self.lang_manager.translate("save_button"))
        self.save_button.setStyleSheet("font-size: 16px; padding: 10px;")

        # ✅ สร้างเมนูสำหรับปุ่ม
        save_menu = QMenu(self)
        self.save_json_action = QAction(self.lang_manager.translate("save_json_action"), self)
        self.save_json_action.triggered.connect(self.save_chat_json)
        
        self.save_txt_action = QAction(self.lang_manager.translate("save_txt_action"), self)
        self.save_txt_action.triggered.connect(self.save_chat_to_file)

        self.save_png_action = QAction(self.lang_manager.translate("save_png_action"), self)
        self.save_png_action.triggered.connect(self.save_chat_to_image)
        
        self.settings_button.clicked.connect(self.open_settings_dialog)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        save_menu.addAction(self.save_json_action)
        save_menu.addAction(self.save_txt_action)
        save_menu.addAction(self.save_png_action)

        # ✅ ทำให้ปุ่มมีเมนู
        self.save_button.setMenu(save_menu)

        for button2 in [self.save_button, self.settings_button, self.logout_button]:
            button2.setStyleSheet("font-size: 16px; padding: 10px;")
            left_sidebar.addWidget(button2)

        # ✅ ส่วนของแชท (ด้านขวา)
        chat_layout = QVBoxLayout()
        
        self.chat_display_area = QScrollArea()
        self.chat_display_area.setWidgetResizable(True)

        self.chat_display = QWidget()
        self.chat_layout = QVBoxLayout(self.chat_display)
        self.chat_display.setObjectName("Chat_layout")
        self.chat_layout.setAlignment(Qt.AlignTop)

        self.chat_display_area.setWidget(self.chat_display)
        chat_layout.addWidget(self.chat_display_area)
        
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText(self.lang_manager.translate("input_field"))
        self.input_field.setStyleSheet("font-size: 18px; padding: 10px;")
        self.input_field.returnPressed.connect(self.send_message)
        chat_layout.addWidget(self.input_field)

        self.send_button = QPushButton(self.lang_manager.translate("send_button"))
        self.send_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.send_button.clicked.connect(self.send_message)
        chat_layout.addWidget(self.send_button)

        main_layout.addLayout(left_sidebar, 1)
        main_layout.addLayout(chat_layout, 3)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # ✅ Chat Manager
        self.chat_manager = cm.ChatManager(self.chat_layout, self.chat_display_area, self.lang_manager)
    
    def toggle_language(self):
        """เปลี่ยนภาษาไทย ↔ อังกฤษ"""
        new_lang = "en" if self.lang_manager.language == "th" else "th"
        self.lang_manager.set_language(new_lang)
        self.update_ui()
        self.chat_manager.update_ui()

    def update_ui(self):
        """อัปเดต UI หลังจากเปลี่ยนภาษา"""
        self.chat_button.setText(self.lang_manager.translate("chat_button"))
        self.settings_button.setText(self.lang_manager.translate("settings_button"))
        self.logout_button.setText(self.lang_manager.translate("logout_button"))
        self.save_button.setText(self.lang_manager.translate("save_button"))
        self.save_json_action.setText(self.lang_manager.translate("save_json_action"))
        self.save_txt_action.setText(self.lang_manager.translate("save_txt_action"))
        self.save_png_action.setText(self.lang_manager.translate("save_png_action"))
        self.input_field.setPlaceholderText(self.lang_manager.translate("input_field"))
        self.send_button.setText(self.lang_manager.translate("send_button"))
        self.lang_button.setText(self.lang_manager.translate("language"))
    
    def show_context_menu(self, position):
        menu = QMenu()
        delete_action = QAction("Delete", self)
        delete_action.triggered.connect(self.delete_selected_chat)
        menu.addAction(delete_action)
        menu.exec(self.chat_list.viewport().mapToGlobal(position))

    def delete_selected_chat(self):
        selected_item = self.chat_list.currentItem()
        if selected_item:
            chat_name = selected_item.text()
            base_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(base_dir, "saved_chats", f"{chat_name}.json")
            if os.path.exists(file_path):
                os.remove(file_path)
                self.chat_list.takeItem(self.chat_list.row(selected_item))
                QMessageBox.information(self, "Deleted", f"{self.lang_manager.translate("delete_chat")}: {chat_name}")
            else:
                QMessageBox.warning(self, "Error", f"{self.lang_manager.translate("delete_chat_warning")}: {chat_name}")
    
    def load_selected_chat(self, item):
        chat_name = item.text()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "saved_chats", f"{chat_name}.json")

        # แสดงข้อความจาก JSON
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    chat_data = json.load(file)  # โหลด JSON

                if "chats" in chat_data:
                    self.clear_chat()  # ล้างแชทเก่าก่อน
                    for chat in chat_data["chats"]:
                        sender = chat["sender"]  # 'user' หรือ 'ai'
                        username = chat["username"]
                        message = chat["message"]
                        self.add_chat_bubble(sender, username, message)  # เพิ่มข้อความเข้า UI
                else:
                    QMessageBox.warning(None, "An error occurred.", self.lang_manager.translate("load_warning"))

            except Exception as e:
                QMessageBox.critical(None, "Error", self.lang_manager.translate("load_critical"))
    
    def load_chat_list(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        folder = os.path.join(base_dir, "saved_chats")  # กำหนดชื่อโฟลเดอร์เก็บแชท
        QMessageBox.information(None, "Settings", self.lang_manager.translate("load_chat_list1"))
        
        # ตรวจสอบว่ามีโฟลเดอร์ไหม ถ้าไม่มีให้สร้าง
        if not os.path.exists(folder):
            print("❌ ไม่มีโฟลเดอร์ saved_chats, กำลังสร้างใหม่...")
            os.makedirs(folder)
            print("✅ สร้างโฟลเดอร์ saved_chats สำเร็จ!")
        else:
            print("✅ พบโฟลเดอร์ saved_chats แล้ว")

        self.chat_list.clear()  # ล้างรายการเก่า
        files = [f for f in os.listdir(folder) if f.endswith(".json")]
    
        if not files:
            print("❌ ไม่มีไฟล์ JSON ในโฟลเดอร์")
        else:
            print("📂 พบไฟล์:", files)
    
        for filename in files:
            item = QListWidgetItem(filename.replace(".json", ""))
            self.chat_list.addItem(item)
    
    def save_chat_json(self):  
        base_dir = os.path.dirname(os.path.abspath(__file__))
        folder = os.path.join(base_dir, "saved_chats")
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(None, "บันทึกเป็น .json (saved_chats)", os.path.join(folder, "saved_chats.json"), "JSON Files (*.json)", options=options)

        if file_path:
            chat_data = {"chats": []}  # สร้างโครงสร้าง JSON
            for i in range(self.chat_layout.count()):
                widget = self.chat_layout.itemAt(i).widget()
                if isinstance(widget, cb.ChatBubble):  # ตรวจสอบว่าเป็น ChatBubble หรือไม่
                    chat_data["chats"].append({
                        "sender": widget.sender,  # 'user' หรือ 'ai'
                        "username": widget.username if widget.sender == "user" else "CAT AI",
                        "message": widget.message
                    })

            # บันทึกเป็น JSON
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(chat_data, file, ensure_ascii=False, indent=4)  # จัดรูปแบบ JSON สวยงาม

            QMessageBox.information(None, "Successful", self.lang_manager.translate("save_chat_information"))
    
    def open_settings_dialog(self):
        """เปิดหน้าต่างการตั้งค่า"""
        self.settings_dialog = sd.SettingsDialog(self)
        self.settings_dialog.exec()
        
    def clear_chat(self):
        while self.chat_layout.count():
            widget = self.chat_layout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

    def add_chat_bubble(self, sender, username, message):
        chat_bubble = cb.ChatBubble(sender, username, message)
        self.chat_layout.addWidget(chat_bubble)
        
    def send_message(self):
        user_text = self.input_field.text().strip()
        if not user_text:
            return

        # ✅ แสดงข้อความของผู้ใช้ทันที
        self.chat_manager.add_chat_bubble("user", self.username, user_text)
        
        # ✅ ล้างช่องพิมพ์และปล่อยให้พิมพ์ต่อได้ทันที
        self.input_field.clear()
        self.input_field.setFocus()

        # ✅ เรียก Worker เพื่อให้ AI ตอบกลับในพื้นหลัง
        self.worker = d.OllamaWorker(user_text)
        self.worker.response_ready.connect(self.display_response)  # รอรับข้อความจาก AI
        self.worker.start()

    def display_response(self, response):
        # ✅ แสดงข้อความของ AI
        self.chat_manager.add_chat_bubble("CAT AI", self.username, response)

    def save_chat_to_file(self):
        self.chat_manager.save_chat_to_file()

    def save_chat_to_image(self):
        self.chat_manager.save_chat_to_image()

    def exit_login(self):
        """ฟังก์ชันออกจากระบบ"""
        self.confirm = QMessageBox.question(self, "Confirm", self.lang_manager.translate("exit"), 
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if self.confirm == QMessageBox.Yes:
            self.close()  # ปิดหน้าต่างปัจจุบัน
            self.restart_program()  # เปิดหน้าต่างล็อกอินใหม่

    def restart_program(self):
        """เปิดหน้าต่างล็อกอินใหม่"""
        global window  # ใช้ global เพื่อเก็บอ้างอิงของหน้าต่างใหม่
        self.window = OOPChat()  # สร้างหน้าต่างใหม่
        self.window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OOPChat()
    sys.exit(app.exec())
