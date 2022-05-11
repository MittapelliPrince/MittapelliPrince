from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic
from PyQt5 import QtWidgets
import sys


class Login(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('Lgin.ui', self)
        self.loginbtn.clicked.connect(self.loginfun)
        self.EditPassword.setEchoMode(QtWidgets.QLineEdit.Password)

    def loginfun(self):
        email = self.email.text()
        password = self.password.text()
        print('Successfully Loggedin with emailid:', email, 'and password:', password)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Win = Login()
    Win.show()
    sys.exit(app.exec_())
