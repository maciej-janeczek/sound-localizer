from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class TestInfoWidget(QtWidgets.QGroupBox):
    def __init__(self):
        super().__init__("Test Info")
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(QtWidgets.QLabel("Name:"), 1, Qt.AlignTop)
        self.name = QtWidgets.QLabel("")
        self.layout.addWidget(self.name, 1, Qt.AlignTop)

        self.layout.addWidget(QtWidgets.QLabel("Age:"), 1, Qt.AlignTop)
        self.age = QtWidgets.QLabel("")
        self.layout.addWidget(self.age, 1, Qt.AlignTop)

        self.layout.addWidget(QtWidgets.QLabel("Gender:"), 1, Qt.AlignTop)
        self.gender = QtWidgets.QLabel("")
        self.layout.addWidget(self.gender, 1, Qt.AlignTop)

        self.layout.addWidget(QtWidgets.QLabel("Testing procedure:"), 1, Qt.AlignTop)
        self.procedure = QtWidgets.QLabel("")
        self.layout.addWidget(self.procedure, 1, Qt.AlignTop)

        self.layout.addWidget(QtWidgets.QLabel("Iterations:"), 1, Qt.AlignTop)
        self.iterations = QtWidgets.QLabel("")
        self.layout.addWidget(self.iterations, 1, Qt.AlignTop)

        self.layout.addWidget(QtWidgets.QLabel("Grid:"), 1, Qt.AlignTop)
        self.grid = QtWidgets.QLabel("")
        self.layout.addWidget(self.grid, 1, Qt.AlignTop)

        self.layout.addWidget(QtWidgets.QLabel("Resolution:"), 1, Qt.AlignTop)
        self.resH = QtWidgets.QLabel("")
        self.layout.addWidget(self.resH, 1, Qt.AlignTop)
        self.resV = QtWidgets.QLabel("")
        self.layout.addWidget(self.resV, 1, Qt.AlignTop)

        self.layout.addWidget(QtWidgets.QLabel(""), 10, Qt.AlignTop)

        self.setLayout(self.layout)
