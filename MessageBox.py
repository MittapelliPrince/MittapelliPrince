import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QMessageBox, QLabel, QAction, qApp, QTextEdit


class MessageBox(QMainWindow):
    def __init__(self):
        super().__init__()

        buttonReply = QMessageBox.question(self, 'Window', '<b>Do you Want to Open Popup ?<b>',
                                           QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('Clicked Yes')
            self.setWindowTitle('Message Box')
            self.setGeometry(800, 400, 300, 200)
            self.label = QLabel(self)
            self.label.setText('<b>Hello!<b>')
            self.label.move(100, 75)
            self.label.setFont(QFont('Arial', 13))

            self.menuBar = self.menuBar()
            filemenu = self.menuBar.addMenu('&File')

            exit_action = QAction('&Exit', self)
            exit_action.setShortcut('Ctrl+Q')
            exit_action.triggered.connect(qApp.quit)
            filemenu.addAction(exit_action)

            self.Button = QPushButton('Exit', self)
            self.Button.setGeometry(125, 110, 50, 25)
            self.Button.clicked.connect(qApp.quit)

        else:
            print('Clicked No')
            sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = MessageBox()
    Window.show()
    sys.exit(app.exec_())
