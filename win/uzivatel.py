from PyQt6 import QtGui
from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from usApp import registrace

class Ui_Form(object):
    def setupUi(self, Form, email):
        Form.setObjectName("Form")
        Form.resize(500, 400)
        self.form = Form
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 1, 1, 1)
        self.jmeno = QtWidgets.QLabel(parent=Form)
        self.jmeno.setObjectName("jmeno")
        self.gridLayout.addWidget(self.jmeno, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 1, 1, 1)
        self.prijmeni = QtWidgets.QLabel(parent=Form)
        self.prijmeni.setObjectName("prijmeni")
        self.gridLayout.addWidget(self.prijmeni, 6, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.btnHome = QtWidgets.QPushButton(parent=Form)
        self.btnHome.setFlat(True)
        self.btnHome.setObjectName("btnHome")
        self.horizontalLayout.addWidget(self.btnHome)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem5, 9, 1, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem6, 4, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem7, 5, 1, 1, 2)
        self.usjmeno = QtWidgets.QLabel(parent=Form)
        self.usjmeno.setObjectName("usjmeno")
        self.gridLayout.addWidget(self.usjmeno, 2, 2, 1, 1)
        self.email = QtWidgets.QLabel(parent=Form)
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 8, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem8, 7, 1, 1, 2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem9, 3, 1, 1, 2)
        self.btnHome.clicked.connect(self.btnAkce)
        self.retranslateUi(Form, email)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def btnAkce(self):
        self.form.close()

    def retranslateUi(self, Form, email):
        _translate = QtCore.QCoreApplication.translate
        r = registrace.Registrace()
        listik = r.vyhledesjPodleEmailu(email)
        if len(listik) < 1:
            listik = [('error','error','error','error','error','error')]
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Jmeno: "))
        self.jmeno.setText(_translate("Form", str(listik[0][1])))
        self.label_4.setText(_translate("Form", "Prijmeni: "))
        self.prijmeni.setText(_translate("Form", str(listik[0][2])))
        self.label_8.setText(_translate("Form", "Uživatelské jméno:"))
        self.label_6.setText(_translate("Form", "email: "))
        self.label.setText(_translate("Form", "Uživatel"))
        self.btnHome.setIcon(QIcon('../OMEGA/src/img/home.png'))
        self.btnHome.setIconSize(QSize(30, 30))
        self.usjmeno.setText(_translate("Form", str(listik[0][3])))
        self.email.setText(_translate("Form", str(listik[0][4])))

def zobrazUzivatele(object : object, email):
    object.Form = QtWidgets.QWidget()
    object.ui = Ui_Form()
    object.ui.setupUi(object.Form, email)
    object.Form.show()




