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

    def __init__(self, synthesizer):
        QtCore.QThread.__init__(self)
        self.timer = QtCore.QTimer()
        self.iteration = -1
        self.answered = True
        self.dir_v_list = [-90.0, -45.0, 0.0, 45.0, 90.0]
        self.dir_h_list = [-45.0, 0.0, 45.0, 90.0]
        self.picked_list = []
        self.answers = []
        self.synth = synthesizer

    def run(self):
        self.thread_func()
        self.exec_()

    def thread_func(self):
        self.timer.timeout.connect(self.timer_func)
        self.timer.start(2000)

    def timer_func(self):
        if self.answered and self.iteration < 5:
            self.answered = False
            self.picked_list.append([random.choice(self.dir_v_list), random.choice(self.dir_h_list)])
            self.iteration += 1
            self.synth.play(0.2, self.picked_list[self.iteration])
        else:
            self.timer.stop()
            # Signal to end should be send and swith to next stage ( " Results ")
            print("END ! :)")

    def check_success(self, answer):
        if not self.answered:
            self.answers.append([answer.x, answer.y])
            self.answered = True
            print("Generated was x:{gen_x}, y:{gen_y} -- You picked  x:{pick_x}, y:{pick_y}".format(
                                        gen_x=self.picked_list[self.iteration][0],  
                                        gen_y=self.picked_list[self.iteration][1], 
                                        pick_x=self.answers[self.iteration][0],
                                        pick_y=self.answers[self.iteration][1]))


class Test(object):
    answered_test_signal = QtCore.pyqtSignal(int)

    def __init__(self, user, synthesizer):
        self.user = user
        self.procedure = ProcedureBasic(synthesizer)

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
