from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTime, QTimer
import sys


class LcdWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Lcd Number')
        self.setGeometry(QtCore.QRect(800, 300, 400, 150))

        timer = QTimer()
        timer.timeout.connect(self.lcd_num)
        timer.start(1000)

    def lcd_num(self):
        vbox = QVBoxLayout()

        self.lcd = QtWidgets.QLCDNumber()
        self.lcd.setStyleSheet('background-color : rgb(31, 170, 28);')
        self.lcd.setDigitCount(8)
        vbox.addWidget(self.lcd)

        self.time = QTime.currentTime()
        self.text = self.time.toString('hh:mm:ss')

        self.lcd.display(self.text)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LcdWindow()
    win.lcd_num()
    win.show()
    sys.exit(app.exec_())
