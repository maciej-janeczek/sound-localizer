import pyaudio
import wave
import os
import threading
from .exceptions import *
from .utils import *
import glob
from ctypes import *
import platform
from contextlib import contextmanager

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

def py_error_handler(filename, line, function, err, fmt):
    pass

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

@contextmanager
def noalsaerr():
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)


class Synthesizer():

    def __init__(self, sounds_path, type="wav"):
        if platform.system() == "Linux":
            os.system("jack_control start")
        self.files_path = ""
        self.files_path = []
        self.files_names_list = []
        if not isinstance(sounds_path, str):
            raise SynthTypeError("not isinstance(sounds_path, str)", sounds_path + " : is not string")
        if not os.path.isdir(sounds_path):
            raise SynthNameError("not os.path.isdir(sounds_path)", sounds_path + " : path does not exist")

        self.files = glob.glob(os.path.join(sounds_path, "*." + type))
        if len(self.files) == 0:
            raise SynthPathError("len(this.files)", "No files of the type: "+type)
        for f in self.files:
            self.files_names_list.append(os.path.splitext(os.path.basename(f))[0])
        print(self.files_names_list)

    def play(self, sound_name, volume, pan):
        if not (sound_name in self.files_names_list):
            raise SynthNameError("not (file in this.files_names_list)", "No such file")
        files = [s for s in self.files if sound_name in s]
        if len(files) != 1:
            raise SynthNameError("len(files)", "Multiple files of that name")
            return
        note = Note(files[0], volume, pan)
        note.start()


class Note(threading.Thread):
    def __init__(self, sound_name, volume, pan):
        threading.Thread.__init__(self)
        self.sound_name = sound_name
        self.pan = pan
        self.volume = volume

    def run(self):
        self.play_sound()

    def play_sound(self):

        chunk = 1024
        f = wave.open(self.sound_name)
        with noalsaerr():
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                            channels=2,
                            rate=f.getframerate(),
                            output=True)

            #read data
            data = f.readframes(chunk)
            data = to_stereo(data, self.pan, self.volume)

            #play stream
            while len(data) != 0:
                stream.write(data)
                data = f.readframes(chunk)
                data = to_stereo(data, self.pan, self.volume)

            #stop stream
            stream.stop_stream()
            stream.close()

            #close PyAudio
            p.terminate()
