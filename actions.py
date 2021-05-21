import os
import dill
import re
import regex
from PyQt5 import QtCore, QtGui, QtWidgets
from google.auth.exceptions import TransportError
import data_base
import trie
from GUI import Translator
from translate import translate_google_cloud_api


def error_message_box(message):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Error!")
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
    msg.setWindowTitle("Warning!")
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
        self.setWindowIcon(QtGui.QIcon("./icons/trans.png"))
        self.translate_button.clicked.connect(lambda: self.action_translate())
        self.save_button.clicked.connect(lambda: self.action_save())
        self.load_button.clicked.connect(lambda: self.action_load())
        self.swap_button.clicked.connect(lambda: self.action_swap())
        self.clear_button.clicked.connect(lambda: self.action_clear())
        self.languages_in.addItems(self.__language_dict.keys())
        self.languages_out.addItems(self.__language_dict.keys())
        self.text_in.installEventFilter(self)
        self.languages_in.currentTextChanged.connect(lambda: self.autocomplete_load_node())
        self.actual_lang = self.languages_in.currentText().lower()
        self.node = dill.load(open(f"autocomplete/{self.actual_lang}.pickle", "rb"))
        self.suggestion = ""

    def autocomplete_load_node(self):
        tmp = self.languages_in.currentText().lower()
        dill.dump(self.node, open(f"autocomplete/{self.actual_lang}.pickle", "wb"))
        self.actual_lang = tmp
        if os.path.isfile(f"./autocomplete/{self.actual_lang}.pickle"):
            self.node = dill.load(open(f"autocomplete/{self.actual_lang}.pickle", "rb"))
        else:
            node = trie.Node()
            dill.dump(node, open(f"autocomplete/{self.actual_lang}.pickle", "wb"))
            self.node = node

    def translate_update_trie(self):
        # this regex ignores special language characters
        words_save = regex.sub('[^\p{L} ]+', "", regex.sub('[\s]+', " ", self.text_in.toPlainText().lower())).split()
        for word in words_save:
            trie.insert(self.node, word)
        file_name = self.languages_in.currentText().lower()
        dill.dump(self.node, open(f"autocomplete/{file_name}.pickle", "wb"))
        self.autocomplete.setText("Press Tab to complete:")
        self.suggestion, self.sugg_message = "", ""

    # translate text from input and show it
    def action_translate(self, update_trie=True):
        src = self.languages_in.currentText()
        dest = self.languages_out.currentText()
        text = self.text_in.toPlainText()

        if text == "":
            return
        elif src == dest:
            self.text_out.setText(text)
        else:
            src = self.__language_dict[src]
            dest = self.__language_dict[dest]
            try:
                translation = translate_google_cloud_api(src, dest, text)
                self.text_out.setText(translation['translatedText'])
            # no internet connection
            except TransportError:
                error_message_box("No internet connection!")

        if update_trie:
            self.translate_update_trie()

    # swap languages and texts if not empty, then call translate on new input
    def action_swap(self):
        src_lang = self.languages_in.currentIndex()
        dest_lang = self.languages_out.currentIndex()
        dest_text = self.text_out.toPlainText()

        self.languages_in.setCurrentIndex(dest_lang)
        self.languages_out.setCurrentIndex(src_lang)
        if dest_text != "":
            self.text_in.setText(dest_text)
            self.action_translate(update_trie=False)

    def action_clear(self):
        self.text_in.setText("")
        self.text_out.setText("")

    def action_save(self):
        filename, filter_ = QtWidgets.QFileDialog.getSaveFileName(caption='Select output file', directory='/Users',
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
        warning_message_box("Make sure that .txt file contains in first lane: two languages(first source, "
                            "second destination) followed by text to translate in next line.")
        filename, filter_ = QtWidgets.QFileDialog.getOpenFileName(caption='Save file', directory='/Users',
                                                                  filter='*.txt')

        if filename:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.readlines()
                if len(content) != 2:
                    error_message_box("Wrong file content!")
                else:
                    src, dest = content[0].strip().split()
                    src, dest = src.lower().capitalize(), dest.lower().capitalize()

                    list_lang = list(self.__language_dict.keys())
                    if src not in list_lang and dest not in list_lang:
                        error_message_box("Source and destination languages are wrong or not followed!")
                        return
                    elif src not in list_lang:
                        error_message_box("Source language is wrong or not followed!")
                        return
                    elif dest not in list_lang:
                        error_message_box("Destination language is wrong or not followed!")
                        return

                    src_ind, dest_ind = list_lang.index(src), list_lang.index(dest)
                    self.languages_in.setCurrentIndex(src_ind)
                    self.languages_out.setCurrentIndex(dest_ind)
                    self.text_in.setText(content[1].strip())
                    self.action_translate(update_trie=False)
                    info_message_box("Text has been loaded!")
        else:
            error_message_box("Action canceled!")

    def action_autocomplete(self):
        if self.text_in.toPlainText() == "":
            return
        tmp = self.text_in.toPlainText().split()[-1]
        # replace punctuation marks and convert to lower letters
        tmp = re.sub('[?.!]', "", tmp).lower()
        suggs = trie.keys_with_prefix(self.node, tmp)

        # when no action is taken: tmp length less than 2, space at the end of the word or no suggestion to prefix word
        if len(tmp) >= 2 and not self.text_in.toPlainText().endswith(" ") and suggs:
            self.sugg_message = max(suggs, key=lambda k: suggs[k])
            self.suggestion = self.sugg_message.replace(tmp, "")
            self.autocomplete.setText(f"Press Tab to complete: " + self.sugg_message)
        else:
            self.autocomplete.setText(f"Press Tab to complete:")

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.text_in:
            if event.key() == QtCore.Qt.Key_Tab:
                content = self.text_in.toPlainText() + self.suggestion
                self.text_in.setText(content)
                cursor = self.text_in.textCursor()
                cursor.movePosition(QtGui.QTextCursor.End)
                self.text_in.setTextCursor(cursor)
                self.autocomplete.setText("Press Tab to complete:")
                self.suggestion = ""
                return True

        elif event.type() == QtCore.QEvent.KeyRelease and obj is self.text_in:
            if event.key() != QtCore.Qt.Key_Tab:
                self.action_autocomplete()

        if self.text_in.toPlainText() != "":
            self.clear_button.setVisible(True)
        else:
            self.clear_button.setVisible(False)

        return super(MainWindow, self).eventFilter(obj, event)
