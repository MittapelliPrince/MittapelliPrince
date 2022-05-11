from PyQt5 import QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QToolBar
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('C:\\users\\sentryeagle\\Desktop\\home.png'))
        self.setWindowTitle('New Window')
        self.setGeometry(400, 300, 500, 400)

    def MenuBar(self):
        self.statusBar = self.statusBar()
        self.statusBar.showMessage('')
        self.menuBar = self.menuBar()
        fileMenu = self.menuBar.addMenu('&File')

        New = QAction('&New', self)
        New.setShortcut('Ctrl+N')
        New.setStatusTip('New file')
        fileMenu.addAction(New)

        Open = QAction('&Open', self)
        Open.setShortcut('Ctrl+O')
        Open.setStatusTip('Open a file')
        fileMenu.addAction(Open)

        Save = QAction('&Save', self)
        Save.setShortcut('Ctrl+S')
        Save.setStatusTip('Save a file')
        fileMenu.addAction(Save)

        Exit = QAction('&Exit', self)
        Exit.setShortcut('Ctrl+Q')
        Exit.setStatusTip('Exit')
        Exit.triggered.connect(qApp.quit)
        fileMenu.addAction(Exit)

    def EditMenu(self):
        editMenu = self.menuBar.addMenu('&Edit')

        Copy = QAction('&Copy', self)
        Copy.setShortcut('Ctrl+C')
        Copy.setStatusTip('Copy')
        editMenu.addAction(Copy)

        Paste = QAction('&Paste', self)
        Paste.setShortcut('Ctrl+V')
        Paste.setStatusTip('Paste')
        editMenu.addAction(Paste)

        Cut = QAction('&Cut', self)
        Cut.setShortcut('Ctrl+X')
        Cut.setStatusTip('Cut')
        editMenu.addAction(Cut)

    def HelpMenu(self):
        helpMenu = self.menuBar.addMenu('&Help')

        About = QAction('&About', self)
        About.setShortcut('Ctrl+H')
        About.setStatusTip('for Help')
        helpMenu.addAction(About)

    def ToolBar(self):
        self.toolbar = QToolBar()
        self.toolbar.setIconSize(QSize(24, 24))
        self.addToolBar(self.toolbar)

        open = QAction(QIcon('C:\\users\\sentryeagle\\Desktop\\Open.png'), 'Open', self)
        open.setShortcut('Ctrl+O')
        open.setStatusTip('Open a file')
        self.toolbar.addAction(open)

        save = QAction(QIcon('C:\\users\\sentryeagle\\Desktop\\Save.png'), 'Save', self)
        save.setShortcut('Ctrl+S')
        save.setStatusTip('Save a file')
        self.toolbar.addAction(save)

        exit = QAction(QIcon('C:\\users\\sentryeagle\\Desktop\\Exit.png'), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit')
        self.toolbar.addAction(exit)
        exit.triggered.connect(qApp.quit)

        print = QAction(QIcon('C:\\users\\sentryeagle\\Desktop\\Print.jpg'), 'Print', self)
        print.setShortcut('Ctrl+P')
        print.setStatusTip('Print a file')
        self.toolbar.addAction(print)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.MenuBar()
    win.EditMenu()
    win.HelpMenu()
    win.ToolBar()
    win.show()
    sys.exit(app.exec_())
