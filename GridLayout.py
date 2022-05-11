from PyQt5.QtWidgets import QDialog, QVBoxLayout, QGroupBox, QGridLayout, QPushButton, QApplication
import sys


class App(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Grid Layout')
        self.setGeometry(800, 350, 32, 10)

    def WinLayout(self):
        WindowLayout = QVBoxLayout()
        WindowLayout.addWidget(self.HGroupBox)
        self.setLayout(WindowLayout)

    def createGridLayout(self):
        self.HGroupBox = QGroupBox('Grid')
        layout = QGridLayout()

        layout.addWidget(QPushButton('1'), 0, 0)
        layout.addWidget(QPushButton('2'), 0, 1)
        layout.addWidget(QPushButton('3'), 0, 2)
        layout.addWidget(QPushButton('4'), 1, 0)
        layout.addWidget(QPushButton('5'), 1, 1)
        layout.addWidget(QPushButton('6'), 1, 2)
        layout.addWidget(QPushButton('7'), 2, 0)
        layout.addWidget(QPushButton('8'), 2, 1)
        layout.addWidget(QPushButton('9'), 2, 2)
        layout.addWidget(QPushButton('0'), 3, 1)

        self.HGroupBox.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    W = App()
    W.createGridLayout()
    W.WinLayout()
    W.show()
    sys.exit(app.exec_())
