import ollama
import re
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class OllamaWorker(QThread):
    response_ready = Signal(str)

    def __init__(self, user_message):
        super().__init__()
        self.user_message = user_message

    def run(self):
        try:
            response = ollama.chat(model="deepseek-r1:8b", messages=[{"role": "user", "content": self.user_message}])
            reply_text = response.get("message", {}).get("content", "Error: No response received.")
            cleaned_response = self.clean_response(reply_text)
        except Exception as e:
            cleaned_response = f"Error: {str(e)}"

        self.response_ready.emit(cleaned_response)

    def clean_response(self, text):
        # ลบข้อความที่ไม่ต้องการออก
        text = re.sub(r"</?think>", "", text)  # ลบ <think> และ </think>
        text = re.sub(r"[<>/\[\]]", "", text)  # ลบ <, >, /, [, และ ]
        text = re.sub(r"\\", " ", text)  # ลบเครื่องหมาย backslash
        text = re.sub(r"boxed", " ", text)  # ลบคำว่า boxed
        text = re.sub(r"( )", " ", text)  # ลบวงเล็บที่ไม่มีข้อมูล
        return text.strip()  # ลบช่องว่างด้านหน้าและด้านหลัง