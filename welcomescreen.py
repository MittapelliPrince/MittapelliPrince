from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtWidgets
from PyQt5 import uic
import psycopg2
import sys


class Welcome(QDialog):
    def __init__(self):
        super(Welcome, self).__init__()
        uic.loadUi('welcomescrn.ui', self)
        self.signin.clicked.connect(self.gotosignin)
        self.Createacc.clicked.connect(self.gotocreateacc)

    def gotosignin(self):
        login = Loginscrn()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreateacc(self):
        create = Createscrn()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Loginscrn(QDialog):
    def __init__(self):
        super(Loginscrn, self).__init__()
        uic.loadUi('loginscrn.ui', self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signinbtn.clicked.connect(self.loginfun)

    def loginfun(self):
        user = self.usernamefield.text()
        password = self.passwordfield.text()

        if len(user) == 0 or len(password) == 0:
            self.error.setText('Please Enter Username and Password.')
        else:
            conn = psycopg2.connect(user='postgres', database='postgres', password='admin', host='localhost', port='6543')
            cursor = conn.cursor()
            query = 'SELECT password FROM login_db WHERE username = \''+user+"\'"
            cursor.execute(query)
            result_pass = cursor.fetchone()[0]
            if result_pass == password:
                print('Successfully logged in.')
                self.error.setText("")
            else:
                self.error.setText('Invalid Username or Password.')


class Createscrn(QDialog):
    def __init__(self):
        super(Createscrn, self).__init__()
        uic.loadUi('createnewaccount.ui', self)
        self.signupbtn.clicked.connect(self.gotosignup)
        self.createpassword.setEchoMode(QtWidgets.QLineEdit.Password)

    def gotosignup(self):
        user = self.createusername.text()
        password = self.createpassword.text()
        confmpass = self.confmpassword.text()

        if len(user) == 0 or len(password) == 0 or len(confmpass) == 0:
            self.error_2.setText('Please fill the above details.')
        elif password != confmpass:
            self.error_2.setText('Password do not Match.')
        else:
            conn = psycopg2.connect(database='postgres', user='postgres', password='admin', host='localhost', port='6543')
            cursor = conn.cursor()
            userdetails = [user, password]
            cursor.execute('INSERT INTO logindb(username, password) VALUES(%s, %s)', userdetails)

            conn.commit()
            cursor.close()

            signupbtn = GotoLoginscrn()
            widget.addWidget(signupbtn)
            widget.setCurrentIndex(widget.currentIndex()+1)


class GotoLoginscrn(QDialog):
    def __init__(self):
        super(GotoLoginscrn, self).__init__()
        uic.loadUi('loginscrn2.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcome = Welcome()
    loginscreen = Loginscrn()
    createscrn = Createscrn()
    gotologin = GotoLoginscrn()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome)
    widget.show()
    sys.exit(app.exec_())
