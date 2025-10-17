from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtCore import Qt
import sys

app = QApplication(sys.argv)


#font = QFont('Tahoma',14)
regular_id = QFontDatabase.addApplicationFont('./fonts/Vazirmatn-regular.ttf')
bold_id = QFontDatabase.addApplicationFont('./fonts/Vazirmatn-bold.ttf')
medium_id = QFontDatabase.addApplicationFont('./fonts/Vazirmatn-medium.ttf')
light_id = QFontDatabase.addApplicationFont('./fonts/Vazirmatn-light.ttf')

font_families = QFontDatabase.applicationFontFamilies(regular_id)
font_family = font_families[0] if font_families else "Tahoma"

font_regular = QFont(font_family, 12, QFont.Weight.Normal)
font_bold = QFont(font_family, 12, QFont.Weight.Bold)
font_light = QFont(font_family, 12, QFont.Weight.Light)

window = QWidget()
window.setWhatsThis('فرم لاگین...')
window.resize(400, 250)


# font = QFont('Vazirmatn',14)
# font.setWeight(QFont.Bold)
# font.setStyle(QFont.StyleNormal)

label_title = QLabel('فرم ورود کاربران')
label_title.setFont(font_bold)
label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
label_title.setStyleSheet('color: #ffffff;')
label_title.setStyleSheet('background-color:rgb(231, 11, 11);')
label_title.setStyleSheet('padding: 10px;')
label_title.setStyleSheet('margin: 10px;')
label_title.setStyleSheet('border-radius: 5px;')
label_title.setStyleSheet('border: 1px solidrgb(145, 4, 4);')
label_title.setStyleSheet('border-radius: 5px;')

label_user = QLabel('نام کاربری:')
label_user.setFont(font_regular)

input_username = QLineEdit()
input_username.setPlaceholderText('نام کاربری خود را وارد کنید')
input_username.setFont(font_light)
input_username.setAlignment(Qt.AlignmentFlag.AlignCenter)
input_username.setStyleSheet('border: 1px solid #000000;')
input_username.setStyleSheet('border-radius: 5px;')

label_password = QLabel('رمز عبور:')
label_password.setFont(font_regular)

input_password = QLineEdit()
input_password.setPlaceholderText('رمز عبور خود را وارد کنید')
input_password.setFont(font_light)
input_password.setAlignment(Qt.AlignmentFlag.AlignCenter)
input_password.setStyleSheet('border: 1px solid #000000;')
input_password.setStyleSheet('border-radius: 5px;')

button_login = QPushButton('ورود')
button_login.setFont(font_regular)


layout = QVBoxLayout()
layout.addWidget(label_title)
layout.addWidget(label_user)
layout.addWidget(input_username)
layout.addWidget(label_password)
layout.addWidget(input_password)
layout.addWidget(button_login)
window.setLayout(layout)

window.show()
sys.exit(app.exec())
