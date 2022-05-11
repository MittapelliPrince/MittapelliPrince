from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QToolBar, QAction, QApplication, QMainWindow, qApp
from PyQt5.QtGui import QIcon
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Tool Bar')
        self.setGeometry(800, 200, 300, 250)

    def ToolBar(self):
        self.toolbar = QToolBar()
        self.toolbar.setIconSize(QSize(25, 25))
        self.addToolBar(self.toolbar)

        open_action = QAction(QIcon("C:\\Users\\sentryeagle\\Desktop\\Open.png"), 'Open', self)
        open_action.setToolTip('Open')
        open_action.setShortcut('Crtl+S')
        self.toolbar.addAction(open_action)

        save_action = QAction(QIcon("C:\\Users\\sentryeagle\\Desktop\\Save.png"), 'Save', self)
        save_action.setToolTip('Save')
        save_action.setShortcut('Crtl+O')
        self.toolbar.addAction(save_action)

        exit_action = QAction(QIcon("C:\\Users\\sentryeagle\\Desktop\\Exit.PNG"), 'Exit', self)
        exit_action.setToolTip('Exit')
        exit_action.setShortcut('Crtl+Q')
        exit_action.triggered.connect(qApp.quit)
        self.toolbar.addAction(exit_action)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    w = Window()
    w.ToolBar()
    w.show()
    sys.exit(App.exec_())
