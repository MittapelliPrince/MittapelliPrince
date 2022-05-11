from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtGui
from PyQt5 import uic
import sys


class TableWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('C:\\Users\\sentryeagle\\Desktop\\home.png'))
        uic.loadUi('Tablewidget.ui', self)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setColumnWidth(2, 150)

    def Insert_data(self):
        data = [{'id': 111, 'name': 'Santhosh', 'address': 'Vzg'}, {'id': 112, 'name': 'Kiran', 'address': 'Kerala'},
                {'id': 113, 'name': 'Suryam', 'address': 'Chennai'}, {'id': 114, 'name': 'Surender', 'address': 'Karnataka'}]
        row = 0
        self.tableWidget.setRowCount(len(data))
        for table in data:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(table['id'])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(table['name']))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(table['address']))
            row += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TableWidget()
    win.Insert_data()
    win.show()
    sys.exit(app.exec_())
