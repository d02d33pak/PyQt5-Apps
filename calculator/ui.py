"""
UI Doc for Calculator App
"""

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg


class MainUI:
    def init_ui(self):
        self.lcd_display = qtw.QLCDNumber()
        self.lcd_display.setDigitCount(10)
        self.lcd_display.setMinimumHeight(100)

        self.main_v_layout = qtw.QVBoxLayout()
        self.main_v_layout.addWidget(self.lcd_display)

        grid_layout = qtw.QGridLayout()
        grid_layout.setSpacing(8)
        grid_layout.setContentsMargins(4, 12, 4, 4)  # top margin from display

        font = qtg.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(60)

        self.n0 = qtw.QPushButton("0")
        self.n1 = qtw.QPushButton("1")
        self.n2 = qtw.QPushButton("2")
        self.n3 = qtw.QPushButton("3")
        self.n4 = qtw.QPushButton("4")
        self.n5 = qtw.QPushButton("5")
        self.n6 = qtw.QPushButton("6")
        self.n7 = qtw.QPushButton("7")
        self.n8 = qtw.QPushButton("8")
        self.n9 = qtw.QPushButton("9")
        self.mod = qtw.QPushButton("%")
        self.add = qtw.QPushButton("+")
        self.sub = qtw.QPushButton("-")
        self.mul = qtw.QPushButton("x")
        self.div = qtw.QPushButton("÷")
        self.eq = qtw.QPushButton("=")
        self.ac = qtw.QPushButton("AC")
        self.bs = qtw.QPushButton("DEL")
        self.n0.setFont(font)
        self.n1.setFont(font)
        self.n2.setFont(font)
        self.n3.setFont(font)
        self.n4.setFont(font)
        self.n5.setFont(font)
        self.n6.setFont(font)
        self.n7.setFont(font)
        self.n8.setFont(font)
        self.n9.setFont(font)
        self.mod.setFont(font)
        self.add.setFont(font)
        self.sub.setFont(font)
        self.mul.setFont(font)
        self.div.setFont(font)
        self.eq.setFont(font)
        self.ac.setFont(font)
        self.bs.setFont(font)
        # so the button can expand in Y axis
        self.eq.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
        self.ac.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
        # some simple styling
        self.mod.setStyleSheet("QPushButton{color:#1976D2}")
        self.add.setStyleSheet("QPushButton{color:#1976D2}")
        self.sub.setStyleSheet("QPushButton{color:#1976D2}")
        self.mul.setStyleSheet("QPushButton{color:#1976D2}")
        self.div.setStyleSheet("QPushButton{color:#1976D2}")
        self.eq.setStyleSheet("QPushButton{color:#4CAF50}")
        self.ac.setStyleSheet("QPushButton{color:#F44336}")
        self.bs.setStyleSheet("QPushButton{color:#FFC107}")
        # tooltip for operators only
        self.mod.setToolTip("Mod")
        self.add.setToolTip("Add")
        self.sub.setToolTip("Subract")
        self.mul.setToolTip("Multiply")
        self.div.setToolTip("Divide")
        self.eq.setToolTip("Equals")
        self.bs.setToolTip("Backspace")
        self.ac.setToolTip("All Clear")
        # first row on calc
        grid_layout.addWidget(self.div, 0, 0)
        grid_layout.addWidget(self.mul, 0, 1)
        grid_layout.addWidget(self.sub, 0, 2)
        grid_layout.addWidget(self.bs, 0, 3)
        # second row on calc
        grid_layout.addWidget(self.n7, 1, 0)
        grid_layout.addWidget(self.n8, 1, 1)
        grid_layout.addWidget(self.n9, 1, 2)
        grid_layout.addWidget(self.ac, 1, 3)
        # third row on calc
        grid_layout.addWidget(self.n4, 2, 0)
        grid_layout.addWidget(self.n5, 2, 1)
        grid_layout.addWidget(self.n6, 2, 2)
        grid_layout.addWidget(self.eq, 2, 3, 3, 1)
        # fourth row on calc
        grid_layout.addWidget(self.n1, 3, 0)
        grid_layout.addWidget(self.n2, 3, 1)
        grid_layout.addWidget(self.n3, 3, 2)
        # fifth row on calc
        grid_layout.addWidget(self.mod, 4, 0)
        grid_layout.addWidget(self.n0, 4, 1)
        grid_layout.addWidget(self.add, 4, 2)

        self.main_v_layout.addLayout(grid_layout)
