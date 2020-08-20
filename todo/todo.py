#!usr/bin/env Python3

"""
Todo App

Author: Deepak Talan
Github: @d02d33pak
"""

import json
import sys

from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

TICK = qtg.QImage("tick.png")


class TodoModel(qtc.QAbstractListModel):
    """ Subclassing from base List model """

    def __init__(self, *args, todos=None, **kwargs):
        super(TodoModel, self).__init__(*args, **kwargs)
        self.todos = todos or []

    def data(self, index, role):
        """
        Need to re-implement from Base class
        Returns data, in this case todos list
        """
        if role == qtc.Qt.DisplayRole:
            _, text = self.todos[index.row()]
            return text

        if role == qtc.Qt.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return TICK

        if role == qtc.Qt.SizeHintRole:
            return qtc.QSize(60, 30)

    def rowCount(self, index):
        """
        Need to re-implement from Base class
        Return no. of todos
        """
        return len(self.todos)


class MainWindow(qtw.QWidget):
    """ Main Window """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setGeometry(600, 200, 300, 360)
        self.setWindowTitle("Todo App")

        main_layout = qtw.QVBoxLayout()
        btn_layout = qtw.QHBoxLayout()

        self.input_box = qtw.QLineEdit()

        self.add_btn = qtw.QPushButton("Add")
        self.add_btn.setStyleSheet("background-color:#a6dcef")
        self.edit_btn = qtw.QPushButton("Edit")
        self.edit_btn.setStyleSheet("background-color:#f6ab6c")
        self.done_btn = qtw.QPushButton("Done")
        self.done_btn.setStyleSheet("background-color:#a8df65")
        self.delete_btn = qtw.QPushButton("Delete")
        self.delete_btn.setStyleSheet("background-color:#d92027")

        self.todo_list = qtw.QListView()
        self.todo_list.setAlternatingRowColors(True)
        self.todo_list.setStyleSheet("alternate-background-color: #ececec")

        self.model = TodoModel()
        # loading existing data from local db
        self.load()
        self.todo_list.setModel(self.model)

        # Connecting buttons with their respective fucntions
        self.add_btn.pressed.connect(self.add_item)
        self.done_btn.pressed.connect(self.complete_item)
        self.edit_btn.pressed.connect(self.edit_item)
        self.delete_btn.pressed.connect(self.delete_item)

        # Layout Management
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.edit_btn)
        btn_layout.addWidget(self.done_btn)
        btn_layout.addWidget(self.delete_btn)

        main_layout.addWidget(self.input_box)
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(self.todo_list)

        self.setLayout(main_layout)

        self.show()

    def add_item(self):
        """ Add ToDo item """
        text = self.input_box.text()
        if text:
            self.model.todos.append((False, text))
            self.model.layoutChanged.emit()
            self.input_box.setText("")
            self.save()

    def edit_item(self):
        """ Edit ToDo item """
        indexes = self.todo_list.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            _, text = self.model.todos[row]
            self.input_box.setText(text)
            del self.model.todos[row]
            self.model.layoutChanged.emit()
            self.todo_list.clearSelection()
            self.save()

    def complete_item(self):
        """ Mark ToDo item as completed """
        indexes = self.todo_list.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            _, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            self.model.dataChanged.emit(index, index)
            self.todo_list.clearSelection()
            self.save()

    def delete_item(self):
        """ Delete ToDo item """
        indexes = self.todo_list.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            del self.model.todos[row]
            self.model.layoutChanged.emit()
            self.todo_list.clearSelection()
            self.save()

    def load(self):
        """ To load todo data from local db """
        try:
            with open("data.db", "r") as file:
                self.model.todos = json.load(file)
        except Exception:
            pass

    def save(self):
        """ To save todo data to local file """
        with open("data.db", "w") as file:
            _ = json.dump(self.model.todos, file)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
