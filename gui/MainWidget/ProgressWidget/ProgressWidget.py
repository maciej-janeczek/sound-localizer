from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from core.user import User, Gender
from core.test import ProcedureType, Test
from gui.AddTestDialog import AddTestDialog
import synthesizer as synth


class ProgressWidget(QtWidgets.QGroupBox):
    start_test_signal = QtCore.pyqtSignal(Test)

    def __init__(self, parent):
        super().__init__("Progress")
        self.main_window = parent
        buttons_layout = QtWidgets.QHBoxLayout()

        self.b0 = QtWidgets.QPushButton("New test", self)
        self.b0.clicked.connect(self.new_test)
        self.b1 = QtWidgets.QPushButton("Start", self)
        self.b1.setDisabled(True)
        self.b1.clicked.connect(self.start_test)
        self.b2 = QtWidgets.QPushButton("Testing", self)
        self.b2.setDisabled(True)
        self.b5 = QtWidgets.QPushButton("Results", self)
        self.b5.setDisabled(True)
        buttons_layout.addWidget(self.b0)
        buttons_layout.addWidget(self.b1)
        buttons_layout.addWidget(self.b2)
        buttons_layout.addWidget(self.b5)
        self.setLayout(buttons_layout)
        self.synth = synth.Synthesizer("resources")

    def new_test(self):
        self.add_new = AddTestDialog()
        self.main_window.setDisabled(True)
        self.add_new.show()
        if self.add_new.exec_():
            self.user = User(self.add_new.name, self.add_new.age, self.add_new.gender)
            self.main_window.setDisabled(False)
            self.main_window.testing.setDisabled(False)
            self.main_window.testing.answer.setDisabled(True)
            self.main_window.testing.test_info.name.setText("     " + self.user.name)
            self.main_window.testing.test_info.age.setText("     " + str(self.user.age))
            self.main_window.testing.test_info.gender.setText("     " + str(self.user.gender.value))
            self.main_window.testing.test_info.procedure.setText("     " + str(self.add_new.procedure.value))
            if self.add_new.procedure == ProcedureType.BASIC:
                self.main_window.testing.test_info.iterations.setText("     " + str(self.add_new.iterations))
                self.main_window.testing.test_info.grid.setText("     5x5")
                self.main_window.testing.test_info.resH.setText("     45 degrees (H)")
                self.main_window.testing.test_info.resV.setText("     45 degrees (V)")
            self.b0.setDisabled(True)
            self.b1.setDisabled(False)

    def start_test(self):
        self.main_window.testing.answer.setDisabled(False)
        self.b1.setDisabled(True)
        self.b2.setDisabled(False)
        test = Test(self.user, self.synth)
        self.start_test_signal.emit(test)

