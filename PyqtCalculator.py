from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QGraphicsColorizeEffect
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(800, 300, 350, 335)
        self.setStyleSheet('background-color : white')

    def UiComponents(self):
        self.label = QLabel(self)
        self.label.setGeometry(5, 5, 340, 80)
        self.label.setStyleSheet('QLabel{border : 2px solid black; background: white;}')
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('Arial', 20))

        clr_btn = QPushButton('Clear', self)
        clr_btn.setGeometry(5, 100, 160, 35)
        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.darkMagenta)
        clr_btn.setGraphicsEffect(c_effect)
        del_btn = QPushButton('Delete', self)
        del_btn.setGeometry(180, 100, 165, 35)
        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        del_btn.setGraphicsEffect(c_effect)
        btn7 = QPushButton('7', self)
        btn7.setGeometry(5, 145, 75, 35)
        btn8 = QPushButton('8', self)
        btn8.setGeometry(90, 145, 75, 35)
        btn9 = QPushButton('9', self)
        btn9.setGeometry(180, 145, 75, 35)
        plus_btn = QPushButton('+', self)
        plus_btn.setGeometry(270, 145, 75, 35)
        btn4 = QPushButton('4', self)
        btn4.setGeometry(5, 190, 75, 35)
        btn5 = QPushButton('5', self)
        btn5.setGeometry(90, 190, 75, 35)
        btn6 = QPushButton('6', self)
        btn6.setGeometry(180, 190, 75, 35)
        mul_btn = QPushButton('*', self)
        mul_btn.setGeometry(270, 190, 75, 35)
        btn1 = QPushButton('1', self)
        btn1.setGeometry(5, 235, 75, 35)
        btn2 = QPushButton('2', self)
        btn2.setGeometry(90, 235, 75, 35)
        btn3 = QPushButton('3', self)
        btn3.setGeometry(180, 235, 75, 35)
        minus_btn = QPushButton('-', self)
        minus_btn.setGeometry(270, 235, 75, 35)
        btn0 = QPushButton('0', self)
        btn0.setGeometry(5, 280, 75, 35)
        point_btn = QPushButton('.', self)
        point_btn.setGeometry(90, 280, 75, 35)
        div_btn = QPushButton('/', self)
        div_btn.setGeometry(180, 280, 75, 35)
        equal_btn = QPushButton('=', self)
        equal_btn.setGeometry(270, 280, 75, 35)
        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.red)
        equal_btn.setGraphicsEffect(c_effect)

        clr_btn.clicked.connect(self.action_clr)
        del_btn.clicked.connect(self.action_del)
        btn7.clicked.connect(self.action7)
        btn8.clicked.connect(self.action8)
        btn9.clicked.connect(self.action9)
        plus_btn.clicked.connect(self.action_plus)
        btn4.clicked.connect(self.action4)
        btn5.clicked.connect(self.action5)
        btn6.clicked.connect(self.action6)
        mul_btn.clicked.connect(self.action_mul)
        btn1.clicked.connect(self.action1)
        btn2.clicked.connect(self.action2)
        btn3.clicked.connect(self.action3)
        minus_btn.clicked.connect(self.action_minus)
        btn0.clicked.connect(self.action0)
        point_btn.clicked.connect(self.action_point)
        div_btn.clicked.connect(self.action_div)
        equal_btn.clicked.connect(self.action_equal)

    def action_clr(self):
        self.label.setText('')

    def action_del(self):
        text = self.label.text()
        self.label.setText(text[:len(text) - 1])

    def action7(self):
        text = self.label.text()
        self.label.setText(text + '7')

    def action8(self):
        text = self.label.text()
        self.label.setText(text + '8')

    def action9(self):
        text = self.label.text()
        self.label.setText(text + '9')

    def action_plus(self):
        text = self.label.text()
        self.label.setText(text + '+')

    def action4(self):
        text = self.label.text()
        self.label.setText(text + '4')

    def action5(self):
        text = self.label.text()
        self.label.setText(text + '5')

    def action6(self):
        text = self.label.text()
        self.label.setText(text + '6')

    def action_mul(self):
        text = self.label.text()
        self.label.setText(text + '*')

    def action1(self):
        text = self.label.text()
        self.label.setText(text + '1')

    def action2(self):
        text = self.label.text()
        self.label.setText(text + '2')

    def action3(self):
        text = self.label.text()
        self.label.setText(text + '3')

    def action_minus(self):
        text = self.label.text()
        self.label.setText(text + '-')

    def action0(self):
        text = self.label.text()
        self.label.setText(text + '0')

    def action_point(self):
        text = self.label.text()
        self.label.setText(text + '.')

    def action_div(self):
        text = self.label.text()
        self.label.setText(text + '/')

    def action_equal(self):
        equation = self.label.text()
        try:
            ans = eval(equation)
            self.label.setText(str(ans))
        except:
            self.label.setText('Invalid Input')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    W = Calculator()
    W.UiComponents()
    W.show()
    sys.exit(app.exec_())
