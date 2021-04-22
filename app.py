from PyQt5 import QtWidgets
import sys
import data_base
import GUI


class App:

    __db = data_base.DataBase()
    __language_dict = __db.get_languages()

    def __init__(self):

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = GUI.Translator()
        ui.setupUi(MainWindow, list(self.__language_dict.keys()))
        MainWindow.show()
        sys.exit(app.exec_())

    @classmethod
    def get_src_dst(cls, src, dest):
        source = cls.__language_dict[src]
        destination = cls.__language_dict[dest]
        return source, destination
