from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import*
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('New Window')
        self.setGeometry(800, 400, 300, 200)
        self.label = QLabel(self)
        self.label.setText("Hello ! there,\nThis is Prince")
        self.label.move(125, 80)
        self.label.setFont(QFont('Times New Roman', 14))
        self.menuBar = self.menuBar()
        fileMenu = self.menuBar.addMenu('File')
        editMenu = self.menuBar.addMenu('Edit')

        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')
        fileMenu.addAction(new_action)

        open_action = QAction('Open', self)
        open_action.triggered.connect(lambda: QApplication.open())
        fileMenu.addAction(open_action)

        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        fileMenu.addAction(save_action)

        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(lambda: QApplication.quit())
        fileMenu.addAction(exit_action)

        copy_action = QAction('Copy', self)
        copy_action.setShortcut('Ctrl+C')
        editMenu.addAction(copy_action)

        paste_action = QAction('Paste', self)
        paste_action.setShortcut('Ctrl+V')
        editMenu.addAction(paste_action)

        undo_action = QAction('Undo', self)
        undo_action.setShortcut('Ctrl+Z')
        editMenu.addAction(undo_action)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    Window = Window()
    Window.show()
    sys.exit(App.exec())
