from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTime, QTimer, Qt
import sys


class LabelTime(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Label Time')
        self.setGeometry(QtCore.QRect(600, 400, 400, 200))

        self.vbox = QVBoxLayout()

        font = QFont('Arial', 50)

        self.lbl = QLabel()
        self.lbl.setAlignment(Qt.AlignCenter)
        self.lbl.setFont(font)
        self.vbox.addWidget(self.lbl)

        self.setLayout(self.vbox)

        timer = QTimer()
        timer.timeout.connect(self.Time)
        timer.start(1000)

    def Time(self):
        time = QTime.currentTime()
        display = time.toString('hh:mm:ss')
        print(display)

        self.lbl.setText(display)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LabelTime()
    win.Time()
    win.show()
    sys.exit(app.exec_())
