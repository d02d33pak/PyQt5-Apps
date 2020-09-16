#!usr/bin/env Python3

"""
Custom Widgets
"""

from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw


class CustomHeader(qtw.QLabel):
    """ Custom Header Label """

    def __init__(self, *args, **kwargs):
        super(CustomHeader, self).__init__(*args, **kwargs)

        my_font = qtg.QFont()
        my_font.setBold(True)
        my_font.setWeight(60)
        my_font.setPointSize(12)

        self.setAlignment(qtc.Qt.AlignCenter)
        self.setFont(my_font)


class CustomLabel(qtw.QLabel):
    """ Custom Body Label """

    def __init__(self, *args, **kwargs):
        super(CustomLabel, self).__init__(*args, **kwargs)

        my_font = qtg.QFont()
        my_font.setWeight(30)
        my_font.setPointSize(14)

        self.setAlignment(qtc.Qt.AlignCenter)
        self.setFont(my_font)
