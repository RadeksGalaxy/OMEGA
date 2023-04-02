import mysql
from PyQt6 import QtCore
from PyQt6 import QtWidgets
from PyQt6 import QtGui
from PyQt6.QtWidgets import QMessageBox, QLineEdit
from usApp import registrace

class Ui_RegistrForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 440)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, spacerItem1)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Fixed)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, spacerItem2)
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.usname = QtWidgets.QLineEdit(parent=Form)
        self.usname.setMinimumSize(QtCore.QSize(250, 0))
        self.usname.setObjectName("usname")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.usname)
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.jmeno = QtWidgets.QLineEdit(parent=Form)
        self.jmeno.setMinimumSize(QtCore.QSize(250, 0))
        self.jmeno.setObjectName("jmeno")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.jmeno)
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.prijmeni = QtWidgets.QLineEdit(parent=Form)
        self.prijmeni.setMinimumSize(QtCore.QSize(250, 0))
        self.prijmeni.setObjectName("prijmeni")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.prijmeni)
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.passwd = QtWidgets.QLineEdit(parent=Form)
        self.passwd.setMinimumSize(QtCore.QSize(250, 0))
        self.passwd.setObjectName("passwd")
        self.passwd.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.passwd)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.pswdPotvrzeni = QtWidgets.QLineEdit(parent=Form)
        self.pswdPotvrzeni.setMinimumSize(QtCore.QSize(250, 0))
        self.pswdPotvrzeni.setObjectName("pswdPotvrzeni")
        self.pswdPotvrzeni.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pswdPotvrzeni)
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.email = QtWidgets.QLineEdit(parent=Form)
        self.email.setMinimumSize(QtCore.QSize(250, 0))
        self.email.setObjectName("email")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.email)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Fixed)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.ItemRole.SpanningRole, spacerItem3)
        self.chybHlaska = QtWidgets.QLabel(parent=Form)
        self.chybHlaska.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.chybHlaska.setText("")
        self.chybHlaska.setObjectName("chybHlaska")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.chybHlaska)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Fixed)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.ItemRole.SpanningRole, spacerItem4)
        self.registrBtn = QtWidgets.QPushButton(parent=Form)
        self.registrBtn.setObjectName("registrBtn")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.registrBtn)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout.setItem(13, QtWidgets.QFormLayout.ItemRole.SpanningRole, spacerItem5)
        self.gridLayout.addLayout(self.formLayout, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 2, 1, 1)
        self.registrBtn.clicked.connect(lambda: self.registrBtnAkce(Form))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def registrBtnAkce(self, Form):
        spravne = False
        try:
            if self.passwd.text() != self.pswdPotvrzeni.text():
                raise registrace.SpatnaRegistrError('Heslo je zapsáno špatně')
            jmeno = self.jmeno.text()
            prijmeni = self.prijmeni.text()
            usjmeno = self.usname.text()
            email = self.email.text()
            heslo = self.passwd.text()
            registrace.Registrace.registrovatSe(str(jmeno), str(prijmeni), str(usjmeno), str(email), str(heslo))
            self.chybHlaska.setText('')
            spravne = True
        except registrace.SpatnaRegistrError as e:
            self.chybHlaska.setText(str(e))
        except mysql.connector.errors.DatabaseError as e:
            self.chybHlaska.setText(str('database error'))

        if spravne:
            dlg = QMessageBox(Form)
            dlg.setWindowTitle("Poznamka")
            dlg.setText("Ucet je uspesne zaregistrovany")
            button = dlg.exec()
            if button == QMessageBox.StandardButton.Ok:
                print("ucet vytvoren")
            Form.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("registrace", "registrace"))
        self.label_2.setText(_translate("Form", "Registrace"))
        self.label_4.setText(_translate("Form", "uživatelske jm."))
        self.label_6.setText(_translate("Form", "jméno"))
        self.label_7.setText(_translate("Form", "přijmení"))
        self.label_5.setText(_translate("Form", "heslo"))
        self.label.setText(_translate("Form", "potvrzení hesla"))
        self.label_8.setText(_translate("Form", "email"))
        self.registrBtn.setText(_translate("Form", "Registrovat se"))
