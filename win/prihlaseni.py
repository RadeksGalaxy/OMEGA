import mysql
from PyQt6 import QtCore
from PyQt6 import QtWidgets
from PyQt6 import QtGui
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QLineEdit

from win import registrForm
from usApp import prihlaseni as prihlasse
from win import autoservisUs

class Ui_prihlaseni(object):
    def ui_rozhrani(self, email):
        self.autoservisUs = QtWidgets.QMainWindow()
        self.ui = autoservisUs.Ui_autoservisUs()
        self.ui.setupUi(self.autoservisUs, email, [])
        self.autoservisUs.show()

    def setupUi(self, prihlaseni):
        prihlaseni.setObjectName("prihlaseni")
        prihlaseni.resize(960, 540)
        self.prihl = prihlaseni
        self.centralwidget = QtWidgets.QWidget(parent=prihlaseni)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.usname = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.usname.setMinimumSize(QtCore.QSize(250, 0))
        self.usname.setObjectName("usname")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.usname)
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.passwd = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.passwd.setMinimumSize(QtCore.QSize(250, 0))
        self.passwd.setObjectName("passwd")
        self.passwd.setEchoMode(QLineEdit.EchoMode.Password)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.passwd)
        self.chybHlaska = QtWidgets.QLabel(parent=self.centralwidget)
        self.chybHlaska.setText("")
        self.chybHlaska.setObjectName("chybHlaska")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.chybHlaska)
        self.loginBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.loginBtn.setObjectName("loginBtn")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.loginBtn)
        self.registrBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.registrBtn.setObjectName("registrBtn")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.registrBtn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.ItemRole.SpanningRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Fixed)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.ItemRole.SpanningRole, spacerItem3)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.formLayout)
        prihlaseni.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=prihlaseni)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 24))
        self.menubar.setObjectName("menubar")
        prihlaseni.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=prihlaseni)
        self.statusbar.setObjectName("statusbar")
        prihlaseni.setStatusBar(self.statusbar)
        self.registrBtn.clicked.connect(self.registrBtnAkce)
        self.loginBtn.clicked.connect(self.prihlasitBtnAkce)

        self.retranslateUi(prihlaseni)
        QtCore.QMetaObject.connectSlotsByName(prihlaseni)

    def registrBtnAkce(self):
        self.Form = QtWidgets.QWidget()
        self.ui = registrForm.Ui_RegistrForm()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def prihlasitBtnAkce(self):
        spravne = False
        try:
            email = self.usname.text()
            heslo = self.passwd.text()
            if len(str(email)) != 0 and len(str(heslo)) != 0:
                prihlasse.PrihlasSe.prihlasitSe(str(email), str(heslo))
                self.chybHlaska.setText('')
                spravne = True

            else:
                self.chybHlaska.setText('Vložte email a heslo')
        except prihlasse.SpatnePrihlaseniError as e:
            self.chybHlaska.setText(str(e))
        except mysql.connector.errors.DatabaseError as e:
            self.chybHlaska.setText(str('database error'))
        except Exception as e:
            self.chybHlaska.setText('error')

        if spravne:
            self.prihl.close()
            self.ui_rozhrani(self.usname.text())

    def retranslateUi(self, prihlaseni):
        _translate = QtCore.QCoreApplication.translate
        prihlaseni.setWindowTitle(_translate("autoservis", "autoservis"))
        prihlaseni.setWindowIcon(QIcon('../src/img/user.png'))
        self.label_2.setText(_translate("prihlaseni", "Přihlásit se"))
        self.label_4.setText(_translate("prihlaseni", "email"))
        self.label_5.setText(_translate("prihlaseni", "heslo"))
        self.loginBtn.setText(_translate("prihlaseni", "Přihlásit se"))
        self.registrBtn.setText(_translate("prihlaseni", "Registrace"))

def zobrazUzivatele(object : object):
    object.prihlaseni = QtWidgets.QMainWindow()
    object.ui = Ui_prihlaseni()
    object.ui.setupUi(object.prihlaseni)
    object.prihlaseni.show()
