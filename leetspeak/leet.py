#!usr/bin/env Python3

"""
Leet Speak Convertor App

Author: Deepak Talan
Github: @d02d33pak
"""

import sys

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg

REPLACEMENTS = {
    "a": "4",
    "A": "4",
    "e": "3",
    "E": "3",
    "g": "6",
    "G": "6",
    "i": "1",
    "I": "1",
    "o": "0",
    "O": "0",
    "s": "5",
    "S": "5",
    "t": "7",
    "T": "7",
}


class MainWindow(qtw.QMainWindow):
    """ Main Window """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setGeometry(600, 200, 440, 440)
        self.setWindowTitle("Leet Speak Generator")

        self.toggle_state = False

        # Main Container Widget
        container = qtw.QWidget()

        main_vert_layout = qtw.QVBoxLayout()
        top_horz_layout = qtw.QHBoxLayout()
        cntr_horz_layout = qtw.QHBoxLayout()
        bttm_horz_layout = qtw.QHBoxLayout()

        # Status Bar
        self.status_bar = qtw.QStatusBar()
        self.status_bar.showMessage(" L37'5 60...")
        self.status_bar.setStyleSheet("padding-bottom:8px;")
        self.setStatusBar(self.status_bar)

        self.input_lbl = qtw.QLabel("Input:")
        self.input_box = qtw.QPlainTextEdit()
        self.input_box.setLineWrapMode(1)
        self.input_box.zoomIn(4)

        self.live_trnsltn_btn = qtw.QCheckBox("Live Translation")
        self.live_trnsltn_btn.setStatusTip("Translate as you type")
        self.leet_radio = qtw.QRadioButton("Leet Speak")
        self.leet_radio.setChecked(True)
        self.leet_radio.setEnabled(False)
        self.human_radio = qtw.QRadioButton("Human Speak")
        self.human_radio.setEnabled(False)

        self.encode_btn = qtw.QPushButton("Generate Leet Speak")
        self.encode_btn.setStatusTip(" Convert Human Speak to Leet Speak")
        self.decode_btn = qtw.QPushButton("Generate Human Speak")
        self.decode_btn.setStatusTip(" Convert Leet Speak to Human Speak")

        self.output_lbl = qtw.QLabel("Output:")
        self.output_box = qtw.QPlainTextEdit()
        self.output_box.setLineWrapMode(1)
        self.output_box.zoomIn(4)
        self.output_box.setReadOnly(True)

        self.copy_btn = qtw.QPushButton("Copy Output Speak")
        self.copy_btn.setStatusTip(" Copy the generated speak")
        self.clear_inp_btn = qtw.QPushButton("Clear Input")
        self.clear_inp_btn.setStatusTip(" Clear all text from input box")
        self.clear_out_btn = qtw.QPushButton("Clear Output")
        self.clear_out_btn.setStatusTip(" Clear all text from output box")

        # Connecting all buttons to their respective functions
        self.live_trnsltn_btn.stateChanged.connect(self.toggle_live_trnsltn)
        self.leet_radio.toggled.connect(self.toggle_speak)
        self.human_radio.toggled.connect(self.toggle_speak)

        self.encode_btn.clicked.connect(lambda: self.encode_leet(True))
        self.decode_btn.clicked.connect(self.decode_leet)

        self.copy_btn.clicked.connect(self.copy_output)
        self.clear_inp_btn.clicked.connect(lambda: self.clear_box(0))
        self.clear_out_btn.clicked.connect(lambda: self.clear_box(1))

        # Layout Management
        top_horz_layout.addWidget(self.live_trnsltn_btn)
        top_horz_layout.addWidget(self.leet_radio)
        top_horz_layout.addWidget(self.human_radio)

        cntr_horz_layout.addWidget(self.encode_btn)
        cntr_horz_layout.addWidget(self.decode_btn)

        bttm_horz_layout.addWidget(self.copy_btn)
        bttm_horz_layout.addWidget(self.clear_inp_btn)
        bttm_horz_layout.addWidget(self.clear_out_btn)

        main_vert_layout.addWidget(self.input_lbl)
        main_vert_layout.addWidget(self.input_box)
        main_vert_layout.addLayout(top_horz_layout)
        main_vert_layout.addLayout(cntr_horz_layout)
        main_vert_layout.addWidget(self.output_lbl)
        main_vert_layout.addWidget(self.output_box)
        main_vert_layout.addLayout(bttm_horz_layout)

        container.setLayout(main_vert_layout)
        self.setCentralWidget(container)

        self.show()

    def encode_leet(self, is_encoding):
        """ Encode Human to Leet """
        input_text = self.input_box.toPlainText()
        if is_encoding:
            for key, val in REPLACEMENTS.items():
                input_text = input_text.replace(key, val)
        else:
            for key, val in REPLACEMENTS.items():
                input_text = input_text.replace(val, key)
        self.output_box.setPlainText(input_text)

    def decode_leet(self):
        """ Decode Leet to Human """
        self.encode_leet(False)

    def toggle_live_trnsltn(self):
        """ Enable Live Translation options """
        self.toggle_state = not self.toggle_state
        # enable/disable both radio buttons
        self.human_radio.setEnabled(not self.human_radio.isEnabled())
        self.leet_radio.setEnabled(not self.leet_radio.isEnabled())
        if self.toggle_state:
            self.toggle_speak()
        else:
            self.input_box.disconnect()

    def toggle_speak(self):
        """ Toggle Live Translation Speak """
        if self.leet_radio.isChecked():
            self.input_box.textChanged.connect(lambda: self.encode_leet(True))
        elif self.human_radio.isChecked():
            self.input_box.textChanged.connect(self.decode_leet)

    def copy_output(self):
        """ Copy Output Speak """
        self.output_box.selectAll()
        self.output_box.copy()
        self.output_box.moveCursor(qtg.QTextCursor.End)

    def clear_box(self, box_id):
        """ Clear Input/Output Box """
        if box_id == 0:
            self.input_box.clear()
        else:
            self.output_box.clear()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
