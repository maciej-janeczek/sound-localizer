import sys
import PyQt5.QtWidgets as qt
import gui


if __name__ == '__main__':
    app = qt.QApplication(sys.argv)
    w = gui.SoundLocalizerWindow()
    sys.exit(app.exec_())
