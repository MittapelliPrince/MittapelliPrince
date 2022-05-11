from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My First Window')
        self.setGeometry(800, 200, 350, 340)

    def CreateButton(self):
        self.Button = QPushButton('keep Cursor Here', self)
        self.Button.setGeometry(125, 140, 100, 30)
        self.Button.setToolTip('<i><b>Click Button')
        self.Button.clicked.connect(self.actionclicked)

    def actionclicked(self):
        print('Hello! Prince ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = Window()
    Window.CreateButton()
    Window.show()
    sys.exit(app.exec())
