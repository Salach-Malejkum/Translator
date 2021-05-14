from PyQt5 import QtCore, QtGui, QtWidgets


class Translator(object):

    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.setWindowIcon(QtGui.QIcon('icons/trans.png'))
        main_window.resize(871, 444)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(size_policy)
        main_window.setMinimumSize(QtCore.QSize(871, 444))
        main_window.setMaximumSize(QtCore.QSize(871, 444))
        main_window.setStyleSheet("background-color: rgb(103, 103, 103);")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")

        self.translate_button = QtWidgets.QPushButton(self.centralwidget)
        self.translate_button.setGeometry(QtCore.QRect(290, 270, 71, 23))
        self.translate_button.setStyleSheet("QPushButton{\n"
                                            "background-color:#00a82d;\n"
                                            "    border-radius:10px;\n"
                                            "    border:1px solid #18ab29;\n"
                                            "    display:inline-block;\n"
                                            "    cursor:pointer;\n"
                                            "    color:#ffffff;\n"
                                            "    font-family:Arial;\n"
                                            "    font-size:11px;\n"
                                            "    text-decoration:none;\n"
                                            "    text-shadow:0px 1px 0px #2f6627;\n"
                                            "    font-weight: bold;\n"
                                            "}\n"
                                            "QPushButton::hover{\n"
                                            "    background-color: #00b12d;\n"
                                            "}\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color:#15d648;\n"
                                            "}")
        self.translate_button.setObjectName("translate_button")

        self.languages_in = QtWidgets.QComboBox(self.centralwidget)
        self.languages_in.setGeometry(QtCore.QRect(70, 100, 131, 22))
        self.languages_in.setStyleSheet("QComboBox{\n"
                                        "    border:1px solid #18ab29;\n"
                                        "    border-radius: 10px;\n"
                                        "    background: #007509;\n"
                                        "    display:inline-block;\n"
                                        "    cursor:pointer;\n"
                                        "    color:#ffffff;\n"
                                        "    font-family:Arial;\n"
                                        "    font-size:11px;\n"
                                        "    text-decoration:none;\n"
                                        "    text-shadow:0px 1px 0px #2f6627;\n"
                                        "    font-weight: bold;\n"
                                        "}\n"
                                        "\n"
                                        "QComboBox::drop-down {\n"
                                        "    border-left-width: 1px;\n"
                                        "    border-left-color:#18ab29;\n"
                                        "    border-left-style: solid; /* just a single line */\n"
                                        "    border-top-right-radius: 10px; /* same radius as the QComboBox */\n"
                                        "    border-bottom-right-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QComboBox::on {\n"
                                        "    background-color:#00a82d;\n"
                                        "    display:inline-block;\n"
                                        "    cursor:pointer;\n"
                                        "    color:#ffffff;\n"
                                        "    font-family:Arial;\n"
                                        "    font-size:11px;\n"
                                        "    text-decoration:none;\n"
                                        "    text-shadow:0px 1px 0px #2f6627;\n"
                                        "}\n"
                                        "QComboBox::down-arrow{\n"
                                        "    image:url(./icons/blackarrow.png);\n"
                                        "    width: 14px;\n"
                                        "    height: 14px;\n"
                                        "}\n"
                                        "QComboBox::down-arrow:on{\n"
                                        "    image:url(./icons/whitearrow.png);\n"
                                        "    width: 14px;\n"
                                        "    height: 14px;\n"
                                        "}\n"
                                        "QComboBox QAbstractItemView {\n"
                                        "    selection-background-color:#00a82d;\n"
                                        "    border:1px solid #18ab29;\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "QListView {\n"
                                        "    background: #007509;\n"
                                        "    color: #ffffff\n"
                                        "}")
        self.languages_in.setObjectName("languages_in")

        self.languages_out = QtWidgets.QComboBox(self.centralwidget)
        self.languages_out.setGeometry(QtCore.QRect(510, 100, 131, 22))
        self.languages_out.setStyleSheet("QComboBox{\n"
                                         "    border:1px solid #18ab29;\n"
                                         "    border-radius: 10px;\n"
                                         "    background: #007509;\n"
                                         "    display:inline-block;\n"
                                         "    cursor:pointer;\n"
                                         "    color:#ffffff;\n"
                                         "    font-family:Arial;\n"
                                         "    font-size:11px;\n"
                                         "    text-decoration:none;\n"
                                         "    text-shadow:0px 1px 0px #2f6627;\n"
                                         "    font-weight: bold;\n"
                                         "}\n"
                                         "\n"
                                         "QComboBox::drop-down {\n"
                                         "    border-left-width: 1px;\n"
                                         "    border-left-color:#18ab29;\n"
                                         "    border-left-style: solid; /* just a single line */\n"
                                         "    border-top-right-radius: 10px; /* same radius as the QComboBox */\n"
                                         "    border-bottom-right-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QComboBox::on {\n"
                                         "    background-color:#00a82d;\n"
                                         "    display:inline-block;\n"
                                         "    cursor:pointer;\n"
                                         "    color:#ffffff;\n"
                                         "    font-family:Arial;\n"
                                         "    font-size:11px;\n"
                                         "    text-decoration:none;\n"
                                         "    text-shadow:0px 1px 0px #2f6627;\n"
                                         "}\n"
                                         "QComboBox::down-arrow{\n"
                                         "    image:url(./icons/blackarrow.png);\n"
                                         "    width: 14px;\n"
                                         "    height: 14px;\n"
                                         "}\n"
                                         "QComboBox::down-arrow:on{\n"
                                         "    image:url(./icons/whitearrow.png);\n"
                                         "    width: 14px;\n"
                                         "    height: 14px;\n"
                                         "}\n"
                                         "QComboBox QAbstractItemView {\n"
                                         "    selection-background-color:#00a82d;\n"
                                         "    border:1px solid #18ab29;\n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "QListView {\n"
                                         "    background: #007509;\n"
                                         "    color: #ffffff\n"
                                         "}")
        self.languages_out.setObjectName("languages_out")

        self.text_in = QtWidgets.QTextEdit(self.centralwidget)
        self.text_in.setGeometry(QtCore.QRect(70, 130, 291, 131))
        self.text_in.setStyleSheet("    border-radius:10px;\n"
                                   "    border:1px solid #18ab29;\n"
                                   "    display:inline-block;\n"
                                   "    cursor:pointer;\n"
                                   "    color:#ffffff;\n"
                                   "    font-family:Arial;\n"
                                   "    font-size:11px;\n"
                                   "    text-decoration:none;\n"
                                   "    text-shadow:0px 1px 0px #2f6627;\n"
                                   "    font-weight: bold;\n"
                                   "background-color: rgb(165, 165, 165);")
        self.text_in.setObjectName("text_in")

        self.text_out = QtWidgets.QTextEdit(self.centralwidget)
        self.text_out.setEnabled(False)
        self.text_out.setGeometry(QtCore.QRect(510, 130, 291, 131))
        self.text_out.setStyleSheet("    border-radius:10px;\n"
                                    "    border:1px solid #18ab29;\n"
                                    "    display:inline-block;\n"
                                    "    cursor:pointer;\n"
                                    "    color:#ffffff;\n"
                                    "    font-family:Arial;\n"
                                    "    font-size:11px;\n"
                                    "    text-decoration:none;\n"
                                    "    text-shadow:0px 1px 0px #2f6627;\n"
                                    "    font-weight: bold;\n"
                                    "background-color: rgb(145, 145, 145);")
        self.text_out.setObjectName("text_out")

        self.autocomplete = QtWidgets.QLabel(self.centralwidget)
        self.autocomplete.setGeometry(QtCore.QRect(70, 270, 211, 20))
        self.autocomplete.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                        "    border-radius:10px;\n"
                                        "    border:1px solid #18ab29;\n"
                                        "    display:inline-block;\n"
                                        "    cursor:pointer;\n"
                                        "    color:#ffffff;\n"
                                        "    font-family:Arial;\n"
                                        "    font-size:11px;\n"
                                        "    font-weight: bold;\n"
                                        "    text-decoration:none;\n"
                                        "    text-shadow:0px 1px 0px #2f6627;")
        self.autocomplete.setObjectName("label")

        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(400, 160, 75, 23))
        self.save_button.setStyleSheet("QPushButton{\n"
                                       "background-color:#00a82d;\n"
                                       "    border-radius:10px;\n"
                                       "    border:1px solid #18ab29;\n"
                                       "    display:inline-block;\n"
                                       "    cursor:pointer;\n"
                                       "    color:#ffffff;\n"
                                       "    font-family:Arial;\n"
                                       "    font-size:11px;\n"
                                       "    text-decoration:none;\n"
                                       "    text-shadow:0px 1px 0px #2f6627;\n"
                                       "    font-weight: bold;\n"
                                       "}\n"
                                       "QPushButton::hover{\n"
                                       "    background-color: #00b12d;\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color:#15d648;\n"
                                       "}")
        self.save_button.setObjectName("save_button")

        self.load_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_button.setGeometry(QtCore.QRect(400, 210, 75, 23))
        self.load_button.setStyleSheet("QPushButton{\n"
                                       "background-color:#00a82d;\n"
                                       "    border-radius:10px;\n"
                                       "    border:1px solid #18ab29;\n"
                                       "    display:inline-block;\n"
                                       "    cursor:pointer;\n"
                                       "    color:#ffffff;\n"
                                       "    font-family:Arial;\n"
                                       "    font-size:11px;\n"
                                       "    text-decoration:none;\n"
                                       "    text-shadow:0px 1px 0px #2f6627;\n"
                                       "    font-weight: bold;\n"
                                       "}\n"
                                       "QPushButton::hover{\n"
                                       "    background-color: #00b12d;\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color:#15d648;\n"
                                       "}")
        self.load_button.setObjectName("load_button")

        self.swap_button = QtWidgets.QPushButton(self.centralwidget)
        self.swap_button.setGeometry(QtCore.QRect(400, 100, 75, 21))
        self.swap_button.setStyleSheet("QPushButton{\n"
                                       "    icon: url(./icons/swap.png);\n"
                                       "    background-color:#00a82d;\n"
                                       "    border-radius:10px;\n"
                                       "    border:1px solid #18ab29;\n"
                                       "    display:inline-block;\n"
                                       "    cursor:pointer;\n"
                                       "}\n"
                                       "QPushButton::hover{\n"
                                       "    background-color: #00b12d;\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color:#15d648;\n"
                                       "}\n"
                                       "    ")
        self.swap_button.setText("")

        icon = QtGui.QIcon.fromTheme("swap.png")
        self.swap_button.setIcon(icon)
        self.swap_button.setObjectName("swap_button")

        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(330, 140, 21, 23))
        self.clear_button.setStyleSheet("QPushButton {\n"
                                        "    border-radius:10px;\n"
                                        "    background-color: rgb(165, 165, 165);\n"
                                        "    icon: url(./icons/clear.png);\n"
                                        "    display:inline-block;\n"
                                        "    cursor:pointer;\n"
                                        "}\n"
                                        "QPushButton::hover{\n"
                                        "    background-color: rgb(175, 175, 175);\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: rgb(185, 185, 185);\n"
                                        "}")
        self.clear_button.setText("")
        self.clear_button.setObjectName("clear_button")
        self.clear_button.setVisible(False)

        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Translator"))
        self.translate_button.setText(_translate("MainWindow", "Translate"))
        self.autocomplete.setText(_translate("MainWindow", "Press Tab to complete:"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.load_button.setText(_translate("MainWindow", "Load"))
