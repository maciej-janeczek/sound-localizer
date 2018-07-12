# import pyaudio
import wave
import os
from .exceptions import *
from .utils import *
import glob
import libs.ctcsound as cs


class Synthesizer():

    def __init__(self, sounds_path, type="wav"):
        self.csound = cs.Csound()
        self.scorePath = "resources/BarImpact.csd"
        self.csound.compileCsd(self.scorePath)
        self.csound.start()
        self.csThread = cs.CsoundPerformanceThread(self.csound.csound())
        self.csThread.play()

        # self.files_path = ""
        # self.files_path = []
        # self.files_names_list = []
        # if not isinstance(sounds_path, str):
        #     raise SynthTypeError("not isinstance(sounds_path, str)", sounds_path + " : is not string")
        # if not os.path.isdir(sounds_path):
        #     raise SynthNameError("not os.path.isdir(sounds_path)", sounds_path + " : path does not exist")

        # self.files = glob.glob(os.path.join(sounds_path, "*." + type))
        # if len(self.files) == 0:
        #     raise SynthPathError("len(this.files)", "No files of the type: "+type)
        # for f in self.files:
        #     self.files_names_list.append(os.path.splitext(os.path.basename(f))[0])
        # print(self.files_names_list)

    def play(self, volume, pan):

        self.csound.setControlChannel("vol1", volume)
        self.csound.setControlChannel("azimuth1", -pan[0])
        self.csound.setControlChannel("elev1", -pan[1])
        self.csound.setControlChannel("tremAmp1", 0.0)
        self.csound.setControlChannel("tremFreq", 5.0)
        self.csound.setControlChannel("d360_1", 0.0)
        self.csound.setControlChannel("elev1", 0.0)
        self.csound.setControlChannel("mute1", 0.0)
        self.csThread.inputMessage("i1 0 0.5 1 1 1 400 .2 .01 50 10600 0.5 0.16 0 0")
