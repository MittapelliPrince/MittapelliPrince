from PyQt5.QtWidgets import QApplication, QDialog, QGroupBox, QVBoxLayout, QHBoxLayout, QRadioButton
from PyQt5 import QtGui
import sys


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Radio Buttons')
        self.setGeometry(500, 400, 500, 200)

        vbox = QVBoxLayout()
        vbox.addWidget(self.HGroupBox)
        self.setLayout(vbox)

    def Radiobtn(self):
        self.HGroupBox = QGroupBox("What's your Favourite Programming Language?")
        self.HGroupBox.setFont(QtGui.QFont('Arial', 16))

        hboxlayout = QHBoxLayout()
        self.radiobtn1 = QRadioButton('Java')
        hboxlayout.addWidget(self.radiobtn1)

        self.HGroupBox.setLayout(hboxlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.Radiobtn()
    win.show()
    sys.exit(app.exec_())
