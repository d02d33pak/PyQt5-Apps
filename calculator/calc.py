#!usr/bin/env Python3

"""
Calculator Clone Application

Author: Deepak Talan
Github: @d02d33pak
"""

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg

from ui import MainUI
import operator
import sys

# calculator states
READY = 0
INPUT = 1

class MainWindow(qtw.QWidget, MainUI):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Calgulator')
        self.move(400, 200)
        self.init_ui()
        self.setLayout(self.main_v_layout)

        # input numbers on lcd display
        for i in range(10):
            getattr(self, f'n{i}').pressed.connect(lambda num=i: self.input_num(num))

        self.mod.pressed.connect(lambda: self.operation(operator.mod))
        self.add.pressed.connect(lambda: self.operation(operator.add))
        self.sub.pressed.connect(lambda: self.operation(operator.sub))
        self.mul.pressed.connect(lambda: self.operation(operator.mul))
        self.div.pressed.connect(lambda: self.operation(operator.truediv))

        self.bs.pressed.connect(self.backspace)
        self.ac.pressed.connect(self.reset)
        self.eq.pressed.connect(self.equals)

        self.reset()
        self.show()

    def display(self):
        self.lcd_display.display(self.stack[-1])

    def reset(self):
        self.state          = READY
        self.stack          = [0]
        self.last_operation = None
        self.current_op     = None
        self.display()

    def input_num(self, n):
        if self.state == READY:
            self.state = INPUT
            self.stack[-1] = n
        else:
            self.stack[-1] = self.stack[-1] * 10 + n

        self.display()

    def backspace(self):
        self.state = INPUT
        self.stack[-1] = self.stack[-1] // 10
        self.display()


    def operation(self, op):
        if self.current_op:
            self.equals()

        self.stack.append(0) # place for second input to go in to
        self.state = INPUT
        self.current_op = op

    def equals(self):
        if self.current_op:
            try:
                self.stack = [self.current_op(*self.stack)]
            except Exception:
                self.lcd_display.display('Err')
                self.stack = [0]
            else:
                self.current_op = None
                self.state = READY
                self.display()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
