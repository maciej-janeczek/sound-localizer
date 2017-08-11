import PyQt5.QtWidgets as qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp

from core.user import User, Gender
from gui.AddTestDialog import AddTestDialog
from .MainWidget import MainWidget


class SoundLocalizerWindow(qt.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        screen_size = qt.QDesktopWidget().screenGeometry(-1)
        super().setWindowTitle("Sound Localizer")
        super().resize(int(screen_size.width()*0.8), int(screen_size.height()*0.8))
        super().move(int(screen_size.width()*0.1), int(screen_size.height()*0.1))

        self.init_menu()

        self.main_widget = MainWidget(self)
        size = self.size()
        self.show()

    def init_menu(self):
        self.menubar = self.menuBar()

        file_menu = self.menubar.addMenu('&File')
        new_user_action = QAction(QIcon('new.png'), '&New Test', self)
        new_user_action.triggered.connect(self.new_test)
        file_menu.addAction(new_user_action)

        save_action = QAction(QIcon('save.png'), '&Save', self)
        save_action.triggered.connect(self.save)
        file_menu.addAction(save_action)

        load_action = QAction(QIcon('load.png'), '&Load', self)
        load_action.triggered.connect(self.load)
        file_menu.addAction(load_action)

        exit_action = QAction(QIcon('exit.png'), '&Exit', self)
        exit_action.triggered.connect(qApp.quit)
        file_menu.addAction(exit_action)

        settings_menu = self.menubar.addMenu('&Settings')
        audio_device_action = QAction(QIcon('settings.png'), '&Audio Device', self)
        audio_device_action.triggered.connect(self.audio_device_settings)
        settings_menu.addAction(audio_device_action)

        control_device_action = QAction(QIcon('settings.png'), '&Control Device', self)
        control_device_action.triggered.connect(self.control_device_settings)
        settings_menu.addAction(control_device_action)

        helpMenu = self.menubar.addMenu('&Help')


    def new_test(self):
        self.add_new = AddTestDialog()
        self.main_widget.setDisabled(True)
        self.add_new.show()
        if self.add_new.exec_():
            user = User(self.add_new.name, self.add_new.age, self.add_new.gender)
            self.main_widget.setDisabled(False)
            self.main_widget.testing.test_info.name.setText("     " + user.name)
            self.main_widget.testing.test_info.age.setText("     " + str(user.age))
            self.main_widget.testing.test_info.gender.setText("     " + str(user.gender.value))
            self.main_widget.testing.test_info.procedure.setText("     " + str(self.add_new.procedure.value))
            self.main_widget.testing.test_info.iterations.setText("     " + str(self.add_new.iterations))

    def save(self):
        pass

    def load(self):
        pass

    def select_sound(self):
        pass

    def audio_device_settings(self):
        pass

    def control_device_settings(self):
        pass





