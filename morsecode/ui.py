"""
UI Class
"""

from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw


class MainUI:
    """ UI Components """

    def __init__(self):

        self.main_layout = qtw.QHBoxLayout()
        left_layout = qtw.QVBoxLayout()
        right_layout = qtw.QVBoxLayout()

        input_font = qtg.QFont("Sanserif", 12)
        output_font = qtg.QFont("Sanserif", 16)

        ### Convert Box Start ###
        self.convert_grp_box = qtw.QGroupBox("Converter")
        converter_layout = qtw.QVBoxLayout()

        radio_layout = qtw.QHBoxLayout()
        self.radio_to_morse = qtw.QRadioButton("Text to Morse")
        self.radio_to_morse.setChecked(True)
        self.radio_to_text = qtw.QRadioButton("Morse to Text")
        radio_layout.addWidget(self.radio_to_morse)
        radio_layout.addWidget(self.radio_to_text)

        h_line = qtw.QFrame()
        h_line.setFrameShape(qtw.QFrame.HLine)
        h_line.setFrameShadow(qtw.QFrame.Raised)

        self.input_label = qtw.QLabel("Input:")
        self.input_text = qtw.QLineEdit()
        self.input_text.setFont(input_font)

        self.btn_convert = qtw.QPushButton("Convert")

        self.output_label = qtw.QLabel("Output:")
        self.output_morse = qtw.QTextEdit()
        self.output_morse.setFont(output_font)
        self.output_morse.setReadOnly(True)

        converter_layout.addLayout(radio_layout)
        converter_layout.addWidget(h_line)
        converter_layout.addWidget(self.input_label)
        converter_layout.addWidget(self.input_text)
        converter_layout.addWidget(self.btn_convert)
        converter_layout.addWidget(self.output_label)
        converter_layout.addWidget(self.output_morse)

        self.convert_grp_box.setLayout(converter_layout)
        ### Convert Box End ###

        ### Sound Box Start ###
        self.sound_grp_box = qtw.QGroupBox("Play Morse Code")
        sound_layout = qtw.QHBoxLayout()

        self.btn_play_morse = qtw.QPushButton("")
        self.btn_play_morse.setIcon(qtg.QIcon("icons/play.png"))
        self.btn_stop_morse = qtw.QPushButton("")
        self.btn_stop_morse.setIcon(qtg.QIcon("icons/stop.png"))
        self.btn_stop_morse.setEnabled(False)

        sound_layout.addWidget(self.btn_play_morse)
        sound_layout.addWidget(self.btn_stop_morse)

        self.sound_grp_box.setLayout(sound_layout)
        ### Sound Box End ###

        ### Flash Box Start ###
        self.flash_grp_box = qtw.QGroupBox("Flash Morse Code")
        flash_layout = qtw.QVBoxLayout()
        flash_btn_layout = qtw.QHBoxLayout()  # contains red box in one line
        flash_color_layout = qtw.QHBoxLayout()  # and the buttons on another line

        self.flash_box = qtw.QLabel("")
        self.flash_box.setFixedSize(100, 100)
        self.flash_box.setStyleSheet(
            "background-color:white; border:2px solid black; border-radius:4px"
        )

        self.btn_start_flash = qtw.QPushButton("Start Flashing")
        self.btn_stop_flash = qtw.QPushButton("Stop Flashing")
        self.btn_stop_flash.setEnabled(False)

        flash_color_layout.addWidget(self.flash_box)
        flash_btn_layout.addWidget(self.btn_start_flash)
        flash_btn_layout.addWidget(self.btn_stop_flash)

        flash_layout.addLayout(flash_color_layout)
        flash_layout.addLayout(flash_btn_layout)

        self.flash_grp_box.setLayout(flash_layout)
        ### Flash Box End ###

        left_layout.addWidget(self.convert_grp_box)
        right_layout.addWidget(self.sound_grp_box)
        right_layout.addWidget(self.flash_grp_box)
        self.main_layout.addLayout(left_layout)
        self.main_layout.addLayout(right_layout)
