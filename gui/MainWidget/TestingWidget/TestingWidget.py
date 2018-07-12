from PyQt5 import QtWidgets
from .TestInfoWidget import TestInfoWidget
from .AnswerWidget import AnswerWidget
from .ResultsWidget import ResultsWidget
from core.test import Test
from core.user import User, Gender


class TestingWidget(QtWidgets.QGroupBox):


    def __init__(self):
        super().__init__("Test Procedure 1")
        self.testing_layout = QtWidgets.QHBoxLayout()
        self.test_info = TestInfoWidget()
        self.testing_layout.addWidget(self.test_info, 1)
        self.answer = AnswerWidget(5, 5)
        self.testing_layout.addWidget(self.answer, 5)
        self.setLayout(self.testing_layout)
        self.results = ResultsWidget()
        self.testing_layout.addWidget(self.results, 2)
        self.answer.answeredSignal.connect(self.answered)

    def start_test(self, test):
        print ("Test started")
        self.test = test
        print(self.test.user.name)
        test.start_test()

    def answered(self, answer):
        self.test.answered(answer)





