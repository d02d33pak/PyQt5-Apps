#!usr/bin/env Python3

"""
Timer Application

Author: Deepak Talan
Github: @d02d33pak
"""

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

import sys


class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # main window position and dimensions
        # args = x_pos, y_pos, width, height
        self.setGeometry(400, 200, 400, 200)
        self.setWindowTitle('Timer')

        main_layout = qtw.QVBoxLayout()
        time_layout = qtw.QHBoxLayout()
        time_layout.setAlignment(qtc.Qt.AlignVCenter | qtc.Qt.AlignHCenter)
        btn_layout = qtw.QHBoxLayout()

        self.curr_time = qtc.QTime(00, 00, 00)

        # timer
        self.time_label = qtw.QLabel(self.curr_time.toString('hh:mm'))
        self.sec_label = qtw.QLabel(self.curr_time.toString('ss'))
        l_font = qtg.QFont('Arial', 40)
        s_font = qtg.QFont('Arial', 20)
        self.time_label.setFont(l_font)
        self.sec_label.setFont(s_font)

        self.timer = qtc.QTimer()
        self.timer.timeout.connect(self.update_time)

        # control buttons
        self.start_btn = qtw.QPushButton('Start')
        self.start_btn.clicked.connect(self.start_timer)
        self.stop_btn = qtw.QPushButton('Stop')
        self.stop_btn.setEnabled(False)
        self.stop_btn.clicked.connect(self.stop_timer)
        self.reset_btn = qtw.QPushButton('Reset')
        self.reset_btn.clicked.connect(self.reset_timer)

        time_layout.addWidget(self.time_label)
        time_layout.addWidget(self.sec_label)

        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)
        btn_layout.addWidget(self.reset_btn)

        main_layout.addLayout(time_layout)
        main_layout.addLayout(btn_layout)

        # main window central widget
        container = qtw.QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.show()

    def start_timer(self):
        self.timer.start(1000)
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)

    def stop_timer(self):
        self.timer.stop()
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)

    def reset_timer(self):
        self.stop_timer()
        self.curr_time = qtc.QTime(00, 00, 00)
        self.time_label.setText(self.curr_time.toString('hh:mm'))
        self.sec_label.setText(self.curr_time.toString('ss'))

    def update_time(self):
        self.curr_time = self.curr_time.addSecs(1)
        self.time_label.setText(self.curr_time.toString('hh:mm'))
        self.sec_label.setText(self.curr_time.toString('ss'))


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
