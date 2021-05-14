from PyQt5 import QtWidgets
import sys
import actions


class App:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        ui = actions.MainWindow()
        ui.show()
        sys.exit(app.exec_())
