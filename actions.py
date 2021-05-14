from PyQt5 import QtCore, QtGui, QtWidgets
import trie
from GUI import Translator
from translate import translate_google_cloud_api
from google.api_core.exceptions import BadRequest
from google.auth.exceptions import TransportError
import data_base
import dill
import re


def error_message_box(message):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Error")
    msg.setWindowIcon(QtGui.QIcon("./icons/error.png"))
    msg.setText(message)
    msg.show()
    msg.exec_()


def info_message_box(message):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Information")
    msg.setWindowIcon(QtGui.QIcon("./icons/info.png"))
    msg.setText(message)
    msg.show()
    msg.exec_()


def warning_message_box(message):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Warning")
    msg.setWindowIcon(QtGui.QIcon("./icons/warn.png"))
    msg.setText(message)
    msg.show()
    msg.exec_()


class MainWindow(QtWidgets.QMainWindow, Translator):
    __db = data_base.DataBase()
    __language_dict = __db.get_languages()

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setup_ui(self)
        self.translate_button.clicked.connect(lambda: self.action_translate())
        self.save_button.clicked.connect(lambda: self.action_save())
        self.load_button.clicked.connect(lambda: self.action_load())
        self.swap_button.clicked.connect(lambda: self.action_swap())
        self.clear_button.clicked.connect(lambda: self.action_clear())
        self.languages_in.addItems(self.__language_dict.keys())
        self.languages_out.addItems(self.__language_dict.keys())
        self.text_in.installEventFilter(self)
        self.trie = dill.load(open("autocomplete/autofill.pickle", "rb"))

    # get data to call API
    def get_src_dest(self, src, dest):
        source = self.__language_dict[src]
        destination = self.__language_dict[dest]
        return source, destination

    # translate text from input and show it
    # add updating trie after pushing button
    def action_translate(self):
        src = self.languages_in.currentText()
        dest = self.languages_out.currentText()
        text = self.text_in.toPlainText()
        for word in self.text_in.toPlainText().split():
            trie.insert(self.trie, word)
        dill.dump(self.trie, open("autocomplete/autofill.pickle", "wb"))
        self.autocomplete.setText("To fill press Tab key:")
        self.suggestion = ""
        self.sugg_message = ""

        if text == "":
            pass
        elif src == dest:
            self.text_out.setText(text)
        else:
            src, dest = self.get_src_dest(src, dest)
            try:
                translation = translate_google_cloud_api(src, dest, text)
                self.text_out.setText(translation['translatedText'])
            # no internet connection
            except TransportError:
                error_message_box("No internet connection!")
            # except BadRequest:
            #     print("XD")

    # swap languages and set input text to the translated text then call action_translate
    def action_swap(self):
        src_lang = self.languages_in.currentIndex()
        dest_lang = self.languages_out.currentIndex()
        dest_text = self.text_out.toPlainText()

        self.languages_in.setCurrentIndex(dest_lang)
        self.languages_out.setCurrentIndex(src_lang)
        if dest_text != "":
            self.text_in.setText(dest_text)
            self.action_translate()

    def action_clear(self):
        self.text_in.setText("")
        self.text_out.setText("")

    def action_save(self):
        filename, filter_ = QtWidgets.QFileDialog.getSaveFileName(caption='Select output file',  directory='/Users',
                                                                  filter='*.txt')
        if filename:
            if self.text_in.toPlainText() != "":
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(
                        f"From: {self.languages_in.currentText()}\n{self.text_in.toPlainText()}\n" +
                        f"To: {self.languages_out.currentText()}\n{self.text_out.toPlainText()}")
                info_message_box("Translation has been saved!")
            else:
                error_message_box("Translation is empty!")
        else:
            error_message_box("Action canceled!")

    # make sure to add enough restrictions to loading data
    def action_load(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("File content")
        msg.setWindowIcon(QtGui.QIcon("./icons/info.png"))
        msg.setText("Make sure that txt file contains in first lane two languages(first source, second destination) "
                    "followed by text to transalte in next line.")
        msg.show()
        msg.exec_()
        filename, filter_ = QtWidgets.QFileDialog.getOpenFileName(caption='Save file', directory='/Users',
                                                                  filter='*.txt')
        print(filter_, filename)

        if filename:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.readlines()
                if len(content) != 2:
                    error_message_box("Wrong file content!")
                else:
                    src, dest = content[0].strip().split()
                    src_ind = list(self.__language_dict.keys()).index(src)
                    dest_ind = list(self.__language_dict.keys()).index(dest)
                    self.languages_in.setCurrentIndex(src_ind)
                    self.languages_out.setCurrentIndex(dest_ind)
                    self.text_in.setText(content[1].strip())
                    self.action_translate()

                    info_message_box("Text has been loaded!")
        else:
            error_message_box("Action canceled!")

    def action_autocomplete(self):
        tmp = self.text_in.toPlainText().split()[-1]
        print(tmp)
        sugg = trie.keys_with_prefix(self.trie, tmp)
        if len(tmp) >= 2 and not self.text_in.toPlainText().endswith(" "):
            self.sugg_message = max(sugg, key=lambda k: sugg[k])
            self.suggestion = self.sugg_message.replace(tmp, "")
            self.autocomplete.setText(f"To fill press Tab key: " + self.sugg_message)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.text_in:
            if event.key() == QtCore.Qt.Key_Tab:
                content = self.text_in.toPlainText() + self.suggestion
                self.text_in.setText(content)
                cursor = self.text_in.textCursor()
                cursor.movePosition(QtGui.QTextCursor.End)
                self.text_in.setTextCursor(cursor)
                self.autocomplete.setText("To fill press Tab key:")
                return True

        elif event.type() == QtCore.QEvent.KeyRelease and obj is self.text_in:
            if event.key() != QtCore.Qt.Key_Tab:
                self.action_autocomplete()

        return super(MainWindow, self).eventFilter(obj, event)
