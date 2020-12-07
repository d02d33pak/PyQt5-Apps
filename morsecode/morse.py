#!usr/bin/evn Python3
"""
Morse Code App

Author: Deepak Talan
Github: @d02d33pak
"""

import sys
import time

from PyQt5 import QtCore as qtc
from PyQt5 import QtMultimedia as qtm
from PyQt5 import QtWidgets as qtw

from morse_dict import MORSE
from ui import MainUI

DIT = "sounds/dit.wav"
DAH = "sounds/dah.wav"


class SoundThread(qtc.QThread):
    """ Thread to play morse code """

    playDit = qtc.pyqtSignal()
    playDah = qtc.pyqtSignal()
    stopMorse = qtc.pyqtSignal()
    RUNNING = True

    def __init__(self, morse_code):
        super(SoundThread, self).__init__()
        self.morse_code = morse_code
        self.i = 0

    def run(self):
        """ RUN """
        while SoundThread.RUNNING:
            char = self.morse_code[self.i]
            if char == ".":
                self.playDit.emit()
                time.sleep(0.2)
            elif char == "-":
                self.playDah.emit()
                time.sleep(0.4)
            else:
                time.sleep(0.4)
            self.i += 1
            if self.i == len(self.morse_code):
                self.stopMorse.emit()
                SoundThread.RUNNING = False


class FlashThread(qtc.QThread):
    """ Thread to play morse code """

    flashRed = qtc.pyqtSignal()
    flashWhite = qtc.pyqtSignal()
    stopFlash = qtc.pyqtSignal()
    RUNNING = True

    def __init__(self, morse_code):
        super(FlashThread, self).__init__()
        self.morse_code = morse_code
        self.i = 0

    def run(self):
        """ RUN """
        while FlashThread.RUNNING:
            char = self.morse_code[self.i]
            if char == ".":
                self.flashRed.emit()
                time.sleep(0.3)
                self.flashWhite.emit()
                time.sleep(0.2)
            elif char == "-":
                self.flashRed.emit()
                time.sleep(0.6)
                self.flashWhite.emit()
                time.sleep(0.2)
            else:
                time.sleep(0.6)
            self.i += 1
            if self.i == len(self.morse_code):
                self.stopFlash.emit()
                FlashThread.RUNNING = False


class MainWindow(qtw.QWidget, MainUI):
    """ Main Window """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setGeometry(400, 200, 400, 200)
        self.setWindowTitle("Morse Code Converter")
        self.setLayout(self.main_layout)

        # connecting  with their respective functions
        if self.radio_to_morse.isChecked():
            self.btn_convert.pressed.connect(self.encrypt)
            self.input_text.returnPressed.connect(self.encrypt)
        elif self.radio_to_text.isChecked():
            self.btn_convert.pressed.connect(self.decrypt)
            self.input_text.returnPressed.connect(self.decrypt)

        self.btn_play_morse.pressed.connect(self.start_sound)
        self.btn_stop_morse.pressed.connect(self.stop_sound)

        self.btn_start_flash.pressed.connect(self.start_flash)
        self.btn_stop_flash.pressed.connect(self.stop_flash)

        self.show()

    def encrypt(self):
        """ Convert text to Morse Code """
        text = self.input_text.text().upper()
        cipher = [MORSE[ch] for ch in text if ch in MORSE.keys()]
        cipher = " ".join(cipher)
        self.output_morse.setText(cipher)

    def decrypt(self):
        """ Convert Morse Code to normal text """

    def start_sound(self):
        """ Play converted Morse Code """
        output_text = self.output_morse.toPlainText()
        if len(output_text) != 0:
            self.btn_play_morse.setEnabled(False)
            self.btn_stop_morse.setEnabled(True)
            ### Thread Part Start ###
            SoundThread.RUNNING = True
            self.play_thread = SoundThread(output_text)
            self.play_thread.playDit.connect(self.playDit)
            self.play_thread.playDah.connect(self.playDah)
            self.play_thread.stopMorse.connect(self.stop_sound)
            self.play_thread.start()
            ### Thread Part End ###

    def stop_sound(self):
        """ Stop converted Morse Code """
        self.btn_play_morse.setEnabled(True)
        self.btn_stop_morse.setEnabled(False)
        SoundThread.RUNNING = False

    def playDit(self):
        """ Play Dit sound for '.' """
        qtm.QSound.play(DIT)

    def playDah(self):
        """ Play Dah sound for '-' """
        qtm.QSound.play(DAH)

    def start_flash(self):
        """ Play converted Morse Code """
        output_text = self.output_morse.toPlainText()
        if len(output_text) != 0:
            self.btn_start_flash.setEnabled(False)
            self.btn_stop_flash.setEnabled(True)
            ### Thread Part Start ###
            FlashThread.RUNNING = True
            self.flash_thread = FlashThread(output_text)
            self.flash_thread.flashRed.connect(self.flashRed)
            self.flash_thread.flashWhite.connect(self.flashWhite)
            self.flash_thread.stopFlash.connect(self.stop_flash)
            self.flash_thread.start()
            ### Thread Part End ###

    def stop_flash(self):
        """ Stop converted Morse Code """
        self.btn_start_flash.setEnabled(True)
        self.btn_stop_flash.setEnabled(False)
        FlashThread.RUNNING = False

    def flashRed(self):
        """ Flash Red for Dit('.') and Dah('-') but for diff durations """
        self.flash_box.setStyleSheet(
            "background-color:red; border: 2px solid black; border-radius:4px"
        )

    def flashWhite(self):
        """ Bring back to white flash """
        self.flash_box.setStyleSheet(
            "background-color:white; border: 2px solid black; border-radius:4px"
        )


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
