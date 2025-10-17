import sys,os
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import (
    QApplication, QGridLayout, QLabel, QLineEdit, QMessageBox, QPushButton,QWidget
)


app = QApplication(sys.argv)

base_dir = os.path.dirname(os.path.abspath(__file__))
font_path = os.path.join(base_dir,'../fonts/Vazirmatn-regular.ttf')

font_id = QFontDatabase.addApplicationFont(font_path)
if font_id == -1:
    print("Failed to load font")
font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
app.setFont(QFont(font_family,12))

window = QWidget()
window.setWindowTitle('فرم ثبت نام کاربران - layouts')
window.resize(500, 350)

lbl_name = QLabel("نام:")
txt_name = QLineEdit()

lbl_family = QLabel("نام خانوادگی:")
txt_family = QLineEdit()

lbl_email = QLabel("ایمیل:")
txt_email = QLineEdit()

lbl_password = QLabel("رمز عبور:")
txt_password = QLineEdit()
txt_password.setEchoMode(QLineEdit.EchoMode.Password)

btn_submit = QPushButton("ثبت نام")

layout = QGridLayout()
layout.addWidget(lbl_name,0,0)
layout.addWidget(txt_name,0,1)

layout.addWidget(lbl_family,1,0)
layout.addWidget(txt_family,1,1)

layout.addWidget(lbl_email,2,0)
layout.addWidget(txt_email,2,1)

layout.addWidget(lbl_password,3,0)
layout.addWidget(txt_password,3,1)

layout.addWidget(btn_submit,4,0,1,2,Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.setLayoutDirection(Qt.RightToLeft)
layout.setSpacing(12)
layout.setContentsMargins(20, 20, 20, 20)

def register():
    if not txt_name.text() or not txt_family.text() or not txt_email.text() or not txt_password.text():
        QMessageBox.warning(window,"هشدار","لطفا همه فیلدها را پر کنید")
        return
    QMessageBox.information(window,"اطلاع","ثبت نام با موفقیت انجام شد")

btn_submit.clicked.connect(register)


window.show()
sys.exit(app.exec())