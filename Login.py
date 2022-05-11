from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout
from PyQt5 import QtWidgets
import sys


class Loginpage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Page')
        self.resize(300, 200)

        layout = QGridLayout()

        label_name = QLabel('<font size = "4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Enter Username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size = "4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Enter Password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)

        login_btn = QPushButton('Login')
        login_btn.clicked.connect(self.check_login)
        layout.addWidget(login_btn, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def check_login(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        print('You are Successfully Logged In with Username:', username, 'and Password:', password)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Win = Loginpage()
    Win.check_login()
    Win.show()
    sys.exit(app.exec_())
