#!usr/bin/env Python3

"""
Pomodoro App 

Author: Deepak Talan
Github: @d02d33pak

> Used 25 seconds Focus Time and 5 seconds Break Time for simplicity
instead of 25 mins and 5 mins respectively
"""

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

import sys
import time

POMO_TIME = 25 # 60sec*25 is focus time
BREAK_TIME = 5  # 60sec*5 is break time


class CounterThread(qtc.QThread):
    """
    Runs a counter thread
    """
    # countChanged = qtc.pyqtSignal(int)
    countChanged = qtc.pyqtSignal(int, str)
    pomoComplete = qtc.pyqtSignal()
    running = True

    def run(self):
        on_focus, on_break = True, False
        session_time = 0
        while CounterThread.running:
            if on_focus and session_time <= POMO_TIME:
                prg_perc = int((session_time / POMO_TIME ) * 100)
                prg_str = str(POMO_TIME - session_time) + ':00'
                self.countChanged.emit(prg_perc, prg_str)
                session_time+=1
                time.sleep(1)
            elif on_break and session_time <= BREAK_TIME:
                prg_perc = int((session_time / BREAK_TIME ) * 100)
                prg_str = str(BREAK_TIME - session_time) + ':00'
                self.countChanged.emit(prg_perc, prg_str)
                session_time+=1
                time.sleep(1)
            else:
                if on_focus: self.pomoComplete.emit()
                on_focus, on_break = not on_focus, not on_break
                session_time = 0
        return


class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, *kwargs)

        self.setGeometry(600, 200, 300, 100)
        self.setWindowTitle('Pomodoro App')

        layout = qtw.QVBoxLayout()
        btn_layout = qtw.QHBoxLayout()
        
        self.pomos = 0
        self.pomo_label = qtw.QLabel('Pomodoro Completed')
        self.pomo_label.setAlignment(qtc.Qt.AlignCenter)
        self.pomo_count = qtw.QLabel(str(self.pomos))
        self.pomo_count.setAlignment(qtc.Qt.AlignCenter)
        font = qtg.QFont('Arial', 44)
        self.pomo_count.setFont(font)

        self.progress = qtw.QProgressBar()
        self.update_progress(0, '25:00')

        self.start_btn = qtw.QPushButton('Start')
        # green bg color for start btn
        self.start_btn.setStyleSheet('background-color:#a8df65')
        self.start_btn.clicked.connect(self.start_pomo)
        self.stop_btn = qtw.QPushButton('Stop')
        self.stop_btn.setEnabled(False)
        self.stop_btn.clicked.connect(self.stop_pomo)

        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)

        layout.addWidget(self.pomo_label)
        layout.addWidget(self.pomo_count)
        layout.addWidget(self.progress)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

        self.show()

    def start_pomo(self):
        CounterThread.running = True
        self.counter = CounterThread()
        self.counter.countChanged.connect(self.update_progress)
        self.counter.pomoComplete.connect(self.update_pomo)
        self.counter.start()
        # toggling enable state and color of btns
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.start_btn.setStyleSheet('')
        self.stop_btn.setStyleSheet('background-color:#d92027; color:white')

    def update_progress(self, value, time):
        self.progress.setValue(value)
        self.progress.setFormat(time) # for text on the progress bar

    def update_pomo(self):
        self.pomos+=1
        self.pomo_count.setText(str(self.pomos))

    def stop_pomo(self):
        CounterThread.running = False
        self.update_progress(0, '25:00')
        # toggling enable state and color of btns
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.start_btn.setStyleSheet('background-color:#a8df65')
        self.stop_btn.setStyleSheet('')


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
