from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from core.test import Answer


class AnswerWidget(QtWidgets.QGroupBox):
    answeredSignal = pyqtSignal(Answer)

    def __init__(self, xsize, ysize):
        super().__init__("")
        self.grid = QtWidgets.QGridLayout()
        self.lastX = 0
        self.lastY = 0

        for j in range(0, ysize):
            for i in range(0, xsize):
                btn = AnswerButton("H: " + str(45*(-i+(xsize-1)/2)) + "\n" + "V: " + str(45*(-j+(ysize-1)/2)),
                                   45*(-i+(xsize-1)/2), 45*(-j+(ysize-1)/2))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy(1), QtWidgets.QSizePolicy.Policy(1))
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(btn.sizePolicy().hasHeightForWidth())
                btn.setSizePolicy(sizePolicy)
                btn.clicked.connect(self.button_clicked)
                self.grid.addWidget(btn, j, i)

        self.setLayout(self.grid)

    def button_clicked(self):
        button = self.sender()
        answer = Answer(button.x, button.y)
        self.answeredSignal.emit(answer)


class AnswerButton(QtWidgets.QPushButton):
    def __init__(self, label, x, y):
        super(AnswerButton, self).__init__(label)
        self.x = x
        self.y = y
