from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLCDNumber
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTimer
from datetime import datetime
import sys


class LcdTime(QDialog):
    def __init__(self):
        super(LcdTime, self).__init__()
        self.setWindowTitle('QLcd Time')
        self.setGeometry(QtCore.QRect(800, 300, 500, 120))

        self.timer = QTimer()
        self.timer.timeout.connect(self.lcd_num)
        self.timer.start(1000)

    def lcd_num(self):
        vbox = QVBoxLayout()

        self.lcd = QtWidgets.QLCDNumber()

        self.time = datetime.now()
        self.text = self.time.strftime('%H:%M:%S')
        self.lcd.setDigitCount(12)
        vbox.addWidget(self.lcd)

        self.lcd.display(self.text)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LcdTime()
    win.lcd_num()
    win.show()
    sys.exit(app.exec_())
