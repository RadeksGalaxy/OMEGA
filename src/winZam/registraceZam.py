from PyQt6 import QtCore, QtGui, QtWidgets
from src.conDB import connection, metody
from src.zamApp import prihlaseni


class Ui_RegistraceZam(object):
    def setupUi(self, MainWindow):
        """
        metoda pro nastaveni okna registrace
        :param MainWindow: objekt
        :return: nasteveni okna registrace
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 460)
        self.c = connection.Connection()
        self.con = self.c.con()
        self.autoservisy = metody.getAutoservis(self.con)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.chybHlaska = QtWidgets.QLabel(parent=self.centralwidget)
        self.chybHlaska.setText("")
        self.chybHlaska.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.chybHlaska.setObjectName("chybHlaska")
        self.gridLayout.addWidget(self.chybHlaska, 7, 1, 1, 3)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(45, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 9, 1, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 3)
        self.comboAutoservis = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboAutoservis.setObjectName("comboAutoservis")
        for i in self.autoservisy:
            self.comboAutoservis.addItem('')
        self.gridLayout.addWidget(self.comboAutoservis, 3, 2, 1, 2)
        self.jmeno = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.jmeno.setMinimumSize(QtCore.QSize(150, 0))
        self.jmeno.setObjectName("jmeno")
        self.gridLayout.addWidget(self.jmeno, 4, 3, 1, 1)
        self.heslo = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.heslo.setMinimumSize(QtCore.QSize(150, 0))
        self.heslo.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.heslo.setObjectName("heslo")
        self.gridLayout.addWidget(self.heslo, 5, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(45, 0))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(45, 0))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.btnRegistr = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnRegistr.setObjectName("btnRegistr")
        self.horizontalLayout.addWidget(self.btnRegistr)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 1, 1, 3)
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 1, 1, 1)
        self.hesloPotvrd = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.hesloPotvrd.setMinimumSize(QtCore.QSize(150, 0))
        self.hesloPotvrd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.hesloPotvrd.setObjectName("hesloPotvrd")
        self.gridLayout.addWidget(self.hesloPotvrd, 6, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btnRegistr.clicked.connect(self.regAkce)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def regAkce(self):
        """
        metoda pro registraci pro tlacitrko registrovat a vytvotreni uzivatele
        :return: vlozeni uzivatele do db
        """
        try:
            self.chybHlaska.setText('')
            c = connection.Connection()
            con = c.con()
            prihlaseni.PrihlasZam.registrace(metody.getIdAutoservisu(self.comboAutoservis.currentText(), con), self.jmeno.text(), self.heslo.text(), self.hesloPotvrd.text(), con)
            self.chybHlaska.setText('Zaregistrovano')
        except Exception as e:
            self.chybHlaska.setText(str(e))


    def retranslateUi(self, MainWindow):
        """
        metoda pro nastaveni textu v okne registrace
        :param MainWindow: objekt
        :return: nastaveni textu
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Registrace AS"))
        self.label_3.setText(_translate("MainWindow", "heslo"))
        self.label_2.setText(_translate("MainWindow", "jmeno"))
        self.label_4.setText(_translate("MainWindow", "AS"))
        self.label.setText(_translate("MainWindow", "Registrace"))
        self.btnRegistr.setText(_translate("MainWindow", "Registrovat se"))
        self.label_5.setText(_translate("MainWindow", "potvrz h."))
        for i in self.autoservisy:
            self.comboAutoservis.setItemText(self.autoservisy.index(i), _translate("MainWindow", i))

