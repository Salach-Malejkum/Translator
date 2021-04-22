from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from translate import translate_google_cloud_api
import app


class Translator(object):
    def setupUi(self, MainWindow, lang_list):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 489)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.button_trans = QPushButton(self.centralwidget)
        self.button_trans.setGeometry(QtCore.QRect(290, 270, 75, 23))
        self.button_trans.setObjectName("translate_button")
        self.button_trans.clicked.connect(lambda: self.action_translate())

        self.languages_in = QComboBox(self.centralwidget)
        self.languages_in.setGeometry(QtCore.QRect(70, 100, 131, 22))
        self.languages_in.setObjectName("languages_in")
        self.languages_in.addItems(lang_list)

        self.languages_out = QComboBox(self.centralwidget)
        self.languages_out.setGeometry(QtCore.QRect(510, 100, 131, 22))
        self.languages_out.setObjectName("languages_out")
        self.languages_out.addItems(lang_list)

        self.text_in = QTextEdit(self.centralwidget)
        self.text_in.setGeometry(QtCore.QRect(70, 130, 291, 131))
        self.text_in.setObjectName("text_in")

        self.text_out = QTextEdit(self.centralwidget)
        self.text_out.setEnabled(False)
        self.text_out.setGeometry(QtCore.QRect(510, 130, 291, 131))
        self.text_out.setObjectName("text_out")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_trans.setText(_translate("MainWindow", "Translate"))

    def action_translate(self):
        src = self.languages_in.currentText()
        dest = self.languages_out.currentText()
        text = self.text_in.toPlainText()
        if src == dest:
            self.text_out.setText(text)
        else:
            src, dest = app.App.get_src_dst(src, dest)
            translation = translate_google_cloud_api(src, dest, text)
            self.text_out.setText(translation['translatedText'])
