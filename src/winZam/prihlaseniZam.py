from PyQt6 import QtCore, QtGui, QtWidgets
from src.conDB import connection, metody
from src.zamApp import prihlaseni
from src.winZam import zamUI


class Ui_PrihlaseniZam(object):
    def setupUi(self, MainWindow):
        """
        metooda pro nastaveni okna pro prihlaseni okna
        :param MainWindow: objekt
        :return: nastaveni okna
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 560)
        self.okno = MainWindow
        c = connection.Connection()
        self.con = c.con()
        self.autoservisy = metody.getAutoservis(self.con)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 2)
        self.lineID = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineID.setObjectName("lineID")
        self.gridLayout.addWidget(self.lineID, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 3, 1, 1)
        self.chybHlaska = QtWidgets.QLabel(parent=self.centralwidget)
        self.chybHlaska.setText("")
        self.chybHlaska.setObjectName("chybHlaska")
        self.chybHlaska.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.chybHlaska, 6, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.lineHeslo = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineHeslo.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineHeslo.setObjectName("lineHeslo")
        self.gridLayout.addWidget(self.lineHeslo, 5, 2, 1, 1)
        self.comboAutoservis = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboAutoservis.setObjectName("comboAutoservis")
        for i in self.autoservisy:
            self.comboAutoservis.addItem('')
        self.gridLayout.addWidget(self.comboAutoservis, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btnPrihlasitse = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnPrihlasitse.setObjectName("btnPrihlasitse")
        self.horizontalLayout.addWidget(self.btnPrihlasitse)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 1, 1, 2)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem4, 8, 1, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem5, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1028, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btnPrihlasitse.clicked.connect(self.prihlasitSe)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def prihlasitSe(self):
        """
        metoda pro prihlaseni a pro tlacitko prihlaseni zamestnance
        :return: prihlaseni se do aplikace
        """
        try:
            prihlaseni.PrihlasZam.prihlasitSe(self.comboAutoservis.currentIndex() + 1, self.lineID.text(), self.lineHeslo.text())
            zamUI.zobrazHlavniMenu(self, metody.getIdAutoservisu(self.comboAutoservis.currentText(), self.con), metody.getGlobalIdAutoservisu(self.comboAutoservis.currentText(), self.con))
            self.okno.close()
        except prihlaseni.PrihlaseniError as e:
            self.chybHlaska.setText(str(e))
        except Exception as e:
            pass

    def retranslateUi(self, MainWindow):
        """
        metoda pro nasteveni textu v okne
        :param MainWindow: objekt
        :return: nastaveni textu
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Autoservis"))
        self.label_2.setText(_translate("MainWindow", "Autoservis"))
        self.label_4.setText(_translate("MainWindow", "Heslo"))
        self.btnPrihlasitse.setText(_translate("MainWindow", "Přihlásit se"))
        self.label.setText(_translate("MainWindow", "Přihlásit se"))
        self.label_3.setText(_translate("MainWindow", "ID"))
        for i in self.autoservisy:
            self.comboAutoservis.setItemText(self.autoservisy.index(i), _translate("MainWindow", i))

def zobrazPrilaseni(object=object):
    """
    metoda pro zobrazeni okna prihlseni
    :param object: objekt
    :return: zobrazeni okna
    """
    object.MainWindow = QtWidgets.QMainWindow()
    object.ui = Ui_PrihlaseniZam()
    object.ui.setupUi(object.MainWindow)
    object.MainWindow.show()

