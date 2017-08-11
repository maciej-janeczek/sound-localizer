from PyQt5 import QtWidgets
from .ProgressWidget import ProgressWidget
from .TestingWidget import TestingWidget


class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(0, 0, parent.size().width(), parent.size().height())
        mainLayout = QtWidgets.QVBoxLayout()
        self.progress = ProgressWidget(self)
        mainLayout.addWidget(self.progress, 1)
        self.testing = TestingWidget()
        self.progress.start_test_signal.connect(self.testing.start_test)
        mainLayout.addWidget(self.testing, 10)
        self.testing.setDisabled(True)
        self.setLayout(mainLayout)
