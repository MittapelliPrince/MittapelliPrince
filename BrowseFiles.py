from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QVBoxLayout, QPushButton, QLabel
import sys


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Browse Files')
        self.setGeometry(800, 400, 200, 100)

        vbox = QVBoxLayout()
        self.btn = QPushButton('Browse File')
        self.btn.clicked.connect(self.Browse_file)
        vbox.addWidget(self.btn)

        self.label = QLabel()
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def Browse_file(self):
        f_name = QFileDialog.getOpenFileName(self, 'Browse File', 'C:\\', 'All files (*.*)')
        path = f_name[0]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
