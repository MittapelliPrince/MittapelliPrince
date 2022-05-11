from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
import sys


class MenuBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Bar')
        self.resize(400, 200)

        self.menuBar = self.menuBar()
        fileMenu = self.menuBar.addMenu('File')

        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')
        fileMenu.addAction(new_action)

        open_action = QAction('Open', self)
        fileMenu.addAction(open_action)

        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        fileMenu.addAction(save_action)

        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(qApp.quit)
        fileMenu.addAction(exit_action)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    menuBar = MenuBar()
    menuBar.show()
    sys.exit(App.exec_())
