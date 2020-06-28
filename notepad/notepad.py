#!usr/bin/env Python3

"""
NotePad Clone Application

Author: Deepak Talan
Github: @d02d33pak
"""

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtPrintSupport as qtp

import os
import sys


class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # main window position and dimensions
        # args = x_pos, y_pos, width, height
        self.setGeometry(400, 200, 600, 400)

        layout = qtw.QVBoxLayout()
        self.editor = qtw.QPlainTextEdit()
        
        # path of the current file
        self.path = None

        layout.addWidget(self.editor)

        # main window central widget
        container = qtw.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # status bar at the bottom
        self.status = qtw.QStatusBar()
        self.status.showMessage('Ready')
        self.setStatusBar(self.status)

        # menu bar [alt + 'x']
        file_menu = self.menuBar().addMenu('&File')
        edit_menu = self.menuBar().addMenu('&Edit')
        view_menu = self.menuBar().addMenu('&View')

        # toolbar [clickable icons]
        file_toolbar = qtw.QToolBar('File')
        edit_toolbar = qtw.QToolBar('Edit')
        self.addToolBar(file_toolbar)
        self.addToolBar(edit_toolbar)


        open_file_action = qtw.QAction(qtg.QIcon(os.path.join('images', 'open.png')), 'Open', self)
        open_file_action.setStatusTip('Open File')
        open_file_action.setShortcut('Ctrl+O')
        open_file_action.triggered.connect(self.open_file)

        save_file_action = qtw.QAction(qtg.QIcon(os.path.join('images', 'save.png')), 'Save', self)
        save_file_action.setStatusTip('Save File')
        save_file_action.setShortcut('Ctrl+S')
        save_file_action.triggered.connect(self.save_file)

        save_as_file_action = qtw.QAction(qtg.QIcon(os.path.join('images', 'save.png')), 'Save as', self)
        save_as_file_action.setStatusTip('Save File as')
        save_as_file_action.setShortcut('Ctrl+J')
        save_as_file_action.triggered.connect(self.save_as)

        print_action = qtw.QAction(qtg.QIcon(os.path.join('images', 'print.png')), 'Print', self)
        print_action.setStatusTip('Print current file')
        print_action.setShortcut('Ctrl+P')
        print_action.triggered.connect(self.print_file)

        undo_action = qtw.QAction(qtg.QIcon(os.path.join('images', 'undo.png')), 'Undo', self)
        undo_action.setStatusTip('Undo last change')
        undo_action.setShortcut('Ctrl+U')
        undo_action.triggered.connect(self.editor.undo)

        redo_action = qtw.QAction(qtg.QIcon(os.path.join('images', 'redo.png')), 'Redo', self)
        redo_action.setStatusTip('Redo last change')
        redo_action.setShortcut('Ctrl+R')
        redo_action.triggered.connect(self.editor.redo)

        cut_action = qtw.QAction(qtg.QIcon(os.path.join('images', 'cut.png')), 'Cut', self)
        cut_action.setStatusTip('Cut selected text')
        cut_action.setShortcut('Ctrl+X')
        cut_action.triggered.connect(self.editor.cut)
        
        copy_action = qtw.QAction(qtg.QIcon(os.path.join('images', 'copy.png')), 'Copy', self)
        copy_action.setStatusTip('Copy selected text')
        copy_action.setShortcut('Ctrl+C')
        copy_action.triggered.connect(self.editor.copy)

        paste_action = qtw.QAction(qtg.QIcon(os.path.join('images', 'paste.png')), 'Paste', self)
        paste_action.setStatusTip('Paste from clipboard')
        paste_action.setShortcut('Ctrl+V')
        paste_action.triggered.connect(self.editor.paste)

        select_action = qtw.QAction(qtg.QIcon(os.path.join('images', 'select.png')), 'Select All', self)
        select_action.setStatusTip('Select all text')
        select_action.setShortcut('Ctrl+A')
        select_action.triggered.connect(self.editor.selectAll)

        # toggle action
        wrap_action = qtw.QAction('Wrap', self)
        wrap_action.setStatusTip('Wrap text to window')
        wrap_action.setCheckable(True)
        wrap_action.setChecked(True)
        wrap_action.setShortcut('Ctrl+W')
        wrap_action.triggered.connect(self.toggle_wrap)

        exit_action = qtw.QAction('E&xit', self)
        exit_action.setStatusTip('Exit Application')
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(qtw.qApp.quit)

        # adding actions to toolbar and menubar
        file_toolbar.addAction(open_file_action)
        file_toolbar.addAction(save_file_action)
        file_toolbar.addAction(save_as_file_action)
        file_toolbar.addAction(print_action)
        # ---
        file_menu.addAction(open_file_action)
        file_menu.addAction(save_file_action)
        file_menu.addAction(save_as_file_action)
        file_menu.addSeparator()
        file_menu.addAction(print_action)

        edit_toolbar.addAction(undo_action)
        edit_toolbar.addAction(redo_action)
        edit_toolbar.addAction(cut_action)
        edit_toolbar.addAction(copy_action)
        edit_toolbar.addAction(paste_action)
        edit_toolbar.addAction(select_action)
        # ---
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)
        edit_menu.addSeparator()
        edit_menu.addAction(cut_action)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)
        edit_menu.addAction(select_action)
        
        view_menu.addAction(wrap_action)

        self.menuBar().addAction(exit_action)

        self.update_title()
        self.show()

    def update_title(self):
        self.setWindowTitle(f'{(os.path.basename(self.path))} NotePad--' if self.path else 'Untitled - NotePad--')

    def show_dialog(self, error):
        dlg = qtw.QMessageBox(self)
        dlg.setText(error)
        dlg.setIcon(qtw.QMessageBox.Critical)
        dlg.show()

    def open_file(self):
        path, _ = qtw.QFileDialog.getOpenFileName(self, 'Open File', '', 'Text documents (*.txt); All file (*.*)')

        if path:
            try:
                with open(path, 'r') as file:
                    text = file.read()
            except Exception as err:
                self.show_dialog(str(err))
            else:
                self.path = path
                self.editor.setPlainText(text)
                self.update_title()

    def save_file(self):
        if self.path is None: # first time saving so use 'save as'
            return self.save_as()
        self.save() # otherwise just overwrite existing file

    def save_as(self):
        path, _ = qtw.QFileDialog.getSaveFileName(self, 'Save As', '', 'Text documents (*.txt);; All files (*.*)')
        
        if not path:
            return ''
        self.path = path
        self.save()

    def save(self):
        text = self.editor.toPlainText()
        try:
            with open(self.path, 'w') as file:
                file.write(text)
        except Exception as err:
            self.show_dialog(err)
        else:
            self.update_title()

    def print_file(self):
        dlg = qtp.QPrintDialog()
        if dlg.exec_():
            self.editor.print_(dlg.printer())

    def toggle_wrap(self):
        self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0)



if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    app.setApplicationName('NotePad--')
    window = MainWindow()
    sys.exit(app.exec_())
