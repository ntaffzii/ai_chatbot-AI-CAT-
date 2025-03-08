class Language_all:
    def __init__(self):
        self.language = "th"  # ค่าเริ่มต้นเป็นภาษาไทย
        self.translations = {
            "th": {
                "chat_button": "📂 แชททั้งหมด (Click)",
                "settings_button": "⚙️ การตั้งค่า",
                "logout_button": "❌ ออกจากระบบ",
                "save_button": "💾 บันทึกแชท",
                "save_json_action": "📑 บันทึกเป็น .json (saved_chats)",
                "save_txt_action": "📜 บันทึกเป็น .txt",
                "save_png_action": "📷 บันทึกเป็น .png",
                "input_field": "กรุณาพิมพ์ข้อความ....",
                "send_button": "ส่งข้อความ!",
                "language": "🌍 เปลี่ยนภาษา ไทย/อังกฤษ",
                "language_Change": "⬅️ เปลี่ยนภาษา ไทย/อังกฤษ",
                "exit": "คุณต้องการออกจากระบบหรือไม่?",
                "dark_mode": "เปิดโหมดมืดเรียบร้อยแล้ว! 🌙",
                "light_mode": "เปิดโหมดสว่างเรียบร้อยแล้ว! 🌞",
                "dark_mode_radio": "🌙 โหมดมืด",
                "light_mode_radio": "🌞 โหมดสว่าง",
                "save_settings": "บันทึกการตั้งค่า",
                "login_Button": "ลงชื่อเข้าใช้",
                "username_input": "ใส่ผู้ใช้ที่นี่...",
                "password_input": "รหัสผ่าน...",
                "label_login": "กรุณากรอกบัญชีผู้ใช้:",
                "userpass_login": "ล็อกอินสําเร็จ!!",
                "userpass_loginF": "รหัสไม่ถูกต้อง!!",
                "fulluser_login": "กรุณาลองใหม่อีกครั้ง!",
                "load_warning": "ไฟล์ JSON ไม่ถูกต้อง! 🚨",
                "load_critical": "ไม่สามารถโหลดแชทได้:",
                "save_chat_information": "บันทึกแชทเรียบร้อยแล้ว! ✅",
                "load_chat_list1": "เช็คประวัติแชททั้งหมดใน saved_chats folder... เรียบร้อย!",
                "save_chat_to_image": "บันทึกแชทเป็นรูปภาพ! 📷",
                "save_chat_to_file": "บันทึกแชทเป็นไฟล์! 📜",
                "Delete Chat": "🗑️ ลบแชท!",
                "delete_chat": "ไฟล์ถูกลบเรียบร้อยแล้ว!",
                "delete_chat_warning": "หาไฟล์ไม่เจอ!"
            },
            "en": {
                "chat_button": "📂 All Chats (Click)",
                "settings_button": "⚙️ Settings",
                "logout_button": "❌ Logout",
                "save_button": "💾 Save Chat",
                "save_json_action": "📑 Save as .json (saved_chats)",
                "save_txt_action": "📜 Save as .txt",
                "save_png_action": "📷 Save as .png",
                "input_field": "Please enter a message....",
                "send_button": "Send Message!",
                "language": "🌍 Change Language TH/EN",
                "language_Change": "⬅️ Change Language Thai/English",
                "exit": "Do you want to log out?",
                "dark_mode": "Dark mode enabled! 🌙",
                "light_mode": "Light mode enabled! 🌞",
                "dark_mode_radio": "🌙 Dark Mode",
                "light_mode_radio": "🌞 Light Mode",
                "save_settings": "Save Settings",
                "login_Button": "Login",
                "username_input": "Enter username here...",
                "password_input": "Password...",
                "label_login": "Please enter your account:",
                "userpass_login": "Login successful!!",
                "userpass_loginF": "Incorrect password!!",
                "fulluser_login": "Please try again!",
                "load_warning": "Invalid JSON file! 🚨",
                "load_critical": "Unable to load chat:",
                "save_chat_information": "Chat saved successfully! ✅",
                "load_chat_list1": "Checking all chat history in the saved_chats folder... Done!",
                "save_chat_to_image": "Chat saved as image! 📷",
                "save_chat_to_file": "Chat saved as file! 📜",
                "Delete Chat": "🗑️ Delete Chat!"
            }
        }

    def set_language(self, lang):
        """เปลี่ยนภาษา"""
        if lang in self.translations:
            self.language = lang

    def translate(self, key):
        """แปลข้อความ"""
        return self.translations[self.language].get(key, key)