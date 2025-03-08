# สร้างหน้าต่าง SettingsDialog สำหรับเปลี่ยนโหมดสี
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setFixedSize(300, 200)
        self.setWindowModality(Qt.ApplicationModal)
        self.lang_manager = parent.lang_manager  # ใช้อินสแตนซ์ของ OOPChat


        # Layout หลัก
        layout = QVBoxLayout()

        # ตัวเลือกโหมด
        self.dark_mode_radio = QRadioButton(self.lang_manager.translate("dark_mode_radio"))
        self.light_mode_radio = QRadioButton(self.lang_manager.translate("light_mode_radio"))

        # ปุ่มบันทึก
        self.save_button = QPushButton(self.lang_manager.translate("save_settings"))
        self.save_button.clicked.connect(self.apply_settings)
        
        # เพิ่ม Widget ลงใน Layout
        layout.addWidget(self.dark_mode_radio)
        layout.addWidget(self.light_mode_radio)
        layout.addWidget(self.save_button)

        # ตั้งค่า Layout ให้กับหน้าต่าง
        self.setLayout(layout)

        # ตั้งค่าเริ่มต้น (โหมดธรรมดา)
        self.light_mode_radio.setChecked(True)

    def apply_settings(self):
        if self.dark_mode_radio.isChecked():
            if not self.parent().dark_mode_enabled:
                self.parent().toggle_dark_mode() 
                QMessageBox.information(self, "Settings", self.lang_manager.translate("dark_mode"))
        elif self.light_mode_radio.isChecked():
            if self.parent().dark_mode_enabled: 
                self.parent().toggle_dark_mode()  
                QMessageBox.information(self, "Settings", self.lang_manager.translate("light_mode"))
        self.close()

    def update_ui(self):
        """อัปเดต UI หลังจากเปลี่ยนภาษา"""
        self.dark_mode_radio.setText(self.lang_manager.translate("dark_mode_radio"))
        self.light_mode_radio.setText(self.lang_manager.translate("light_mode_radio"))
        self.save_button.setText(self.lang_manager.translate("save_settings"))