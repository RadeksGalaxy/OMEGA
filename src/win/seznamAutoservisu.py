from PyQt6 import QtCore
from PyQt6 import QtGui
from PyQt6 import QtWidgets
from src.win import prihlaseni
from src.win import autoservisUs
from src.win import jednotliveAutoservis

class Ui_AtoservisyI(object):
    def setupUi(self, MainWindow, autoservisy, email):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 550)
        self.win = MainWindow
        self.email = email
        self.autoser = autoservisy
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 7, 1, 1, 1)
        self.comboAutoservis = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboAutoservis.setObjectName("comboAutoservis")
        for i in autoservisy:
            self.comboAutoservis.addItem("")
        self.gridLayout.addWidget(self.comboAutoservis, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btnHledat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnHledat.setObjectName("btnHledat")
        self.horizontalLayout.addWidget(self.btnHledat)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnZpet = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnZpet.setObjectName("btnZpet")
        self.horizontalLayout_2.addWidget(self.btnZpet)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.btnOdhlasitse = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnOdhlasitse.setObjectName("btnOdhlasitse")
        self.horizontalLayout_2.addWidget(self.btnOdhlasitse)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem5, 5, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem6, 5, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem7, 4, 1, 1, 1)
        self.chybHlaska = QtWidgets.QLabel(parent=self.centralwidget)
        self.chybHlaska.setText("")
        self.chybHlaska.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.chybHlaska.setObjectName("label_2")
        self.gridLayout.addWidget(self.chybHlaska, 6, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.btnOdhlasitse.clicked.connect(self.ui_prihlaseni)
        self.btnZpet.clicked.connect(self.zpetbtn)
        self.btnHledat.clicked.connect(self.hledatAkce)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow, autoservisy)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def zpetbtn(self):
        autoservisUs.zobrazHlavniMenu(self, self.email, self.autoser)
        self.win.close()

    def ui_prihlaseni(self):
        prihlaseni.zobrazUzivatele(self)
        self.win.close()

    def hledatAkce(self):
        try:
            jednotliveAutoservis.spustitOkenko(self, self.comboAutoservis.currentText())
        except Exception:
            self.chybHlaska.setText('Problém s připojením')

    def retranslateUi(self, MainWindow, autoservisy):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Autoservis"))
        for i in autoservisy:
            self.comboAutoservis.setItemText(autoservisy.index(i), _translate("autoservisUs", i))
        self.label.setText(_translate("MainWindow", "Seznam autoservisu"))
        self.btnHledat.setText(_translate("MainWindow", "Hledat"))
        self.btnZpet.setText(_translate("MainWindow", "zpět"))
        self.btnOdhlasitse.setText(_translate("MainWindow", "Odhlást se"))


def sezAutoser(object : object, au,email):
    object.MainWindow = QtWidgets.QMainWindow()
    object.ui = Ui_AtoservisyI()
    object.ui.setupUi(object.MainWindow, au, email)
    object.MainWindow.show()



