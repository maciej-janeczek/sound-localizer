from core.user import User
import os
from PyQt5 import QtCore
from enum import Enum
import synthesizer as synth
import random
from decimal import Decimal
from core.user import *


class ProcedureType(Enum):
    BASIC = "Basic"


class ProcedureBasic(QtCore.QThread):

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.timer = QtCore.QTimer()
        self.iteration = -1
        self.answered = True
        self.dir_v_list = [-90, -45, 0, 45, 90]
        self.picked_v_list = []
        self.answers = []
        self.synth = synth.Synthesizer("resources")

        #self.dir_h_list = [-90, -45, 0, 45, 90]

    def run(self):
        self.thread_func()
        self.exec_()

    def thread_func(self):
        self.timer.timeout.connect(self.timer_func)
        self.timer.start(5000)

    def timer_func(self):
        if self.answered and self.iteration < 20:
            self.answered = False
            self.picked_v_list.append(random.choice(self.dir_v_list))
            self.iteration += 1

        self.synth.play("string", 0.2, self.picked_v_list[self.iteration]/90.0)

    def check_success(self, answer):
        if not self.answered:
            self.answers.append([answer.x, answer.y])
            print(len(self.answers), len(self.picked_v_list), self.iteration)
            self.answered = True
            #return self.picked_v_list[self.iteration] == self.answers[self.iteration]
            print("Generated was ", self.picked_v_list[self.iteration], "You picked ", int(self.answers[self.iteration][0]))


class Test(object):
    answered_test_signal = QtCore.pyqtSignal(int)

    def __init__(self, user):
        self.user = user
        self.procedure = ProcedureBasic()


    def save(self, path):
        pass

    def start_test(self):
        self.procedure.run()

    def stop_test(self):
        if self.procedure.isRunning():
            if self.procedure.timer.isActive():
                self.procedure.timer.stop()

    def answered(self, answer):
        self.procedure.check_success(answer)


class Answer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
