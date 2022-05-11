from PyQt5.QtWidgets import QWidget, QInputDialog, QApplication, QLineEdit
import sys


class App(QWidget):
    def __init__(self):
        super().__init__()

    def getInteger(self):
        i, okpressed = QInputDialog.getInt(self, 'Get integer', 'percentage:', 28, 0, 100, 1)
        if okpressed:
            print(i)
        else:
            print('Clicked Cancelled')

    def getDouble(self):
        d, okpressed = QInputDialog.getDouble(self, 'Get Double', 'Values:', 5.50, 0, 100, 10)
        if okpressed:
            print(d)
        else:
            print('Clicked Cancelled')

    def getChoice(self):
        items = ('White', 'Black', 'Red')
        item, okpressed = QInputDialog.getItem(self, 'Get item', 'Color:', items)
        if okpressed and item:
            print(item)
        else:
            print('Clicked Cancelled')

    def getText(self):
        text, okpressed = QInputDialog.getText(self, 'Get Text', 'Your Name:', QLineEdit.Normal, '')
        if okpressed and text != '':
            print(text)
        else:
            print('Clicked Cancelled')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Win = App()
    Win.getInteger()
    Win.getDouble()
    Win.getChoice()
    Win.getText()
    sys.exit(app.exec_())
