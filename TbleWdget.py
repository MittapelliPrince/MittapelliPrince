from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5 import QtGui
import sys


class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Table Widget')
        self.setWindowIcon(QtGui.QIcon('C:/users/sentryeagle/Desktop/home.png'))
        self.setFixedSize(340, 168)

    def CreateTable(self):
        vbox = QVBoxLayout()
        table = QTableWidget()
        table.setRowCount(4)
        table.setColumnCount(3)

        table.setHorizontalHeaderItem(0, QTableWidgetItem('Id'))
        table.setHorizontalHeaderItem(1, QTableWidgetItem('Names'))
        table.setHorizontalHeaderItem(2, QTableWidgetItem('Email'))

        table.setItem(0, 0, QTableWidgetItem('101'))
        table.setItem(0, 1, QTableWidgetItem('Prince'))
        table.setItem(0, 2, QTableWidgetItem('prince@gmail.com'))

        table.setItem(1, 0, QTableWidgetItem('102'))
        table.setItem(1, 1, QTableWidgetItem('Sajeev'))
        table.setItem(1, 2, QTableWidgetItem('sajeev@gmail.com'))

        table.setItem(2, 0, QTableWidgetItem('103'))
        table.setItem(2, 1, QTableWidgetItem('Ashrith'))
        table.setItem(2, 2, QTableWidgetItem('ashrith@gmail.com'))

        table.setItem(3, 0, QTableWidgetItem('104'))
        table.setItem(3, 1, QTableWidgetItem('Vamshi'))
        table.setItem(3, 2, QTableWidgetItem('vamshi@gmail.com'))

        vbox.addWidget(table)
        self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Table()
    win.CreateTable()
    win.show()
    sys.exit(app.exec_())
