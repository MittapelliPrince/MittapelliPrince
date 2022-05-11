from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5 import uic
import sys


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('Gui.ui', self)
        self.Browse.clicked.connect(self.Browsefile)

    def Browsefile(self):
        f_name = QFileDialog.getOpenFileName(self, 'Browse File', 'C:\\Users\\sentryeagle\\PycharProjects\\BasicAssignmets', 'All files (*.*)')
        self.filename.setText(f_name[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
