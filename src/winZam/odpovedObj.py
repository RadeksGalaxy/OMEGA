import datetime

from PyQt6 import QtCore, QtGui, QtWidgets
from src.conDB import connection, metody
import pandas as pd
from vendor.tableModel import TableModel
from src.zamApp import odpoved


class Ui_OdpovedForm(object):
    def setupUi(self, Form, ob, globalID):
        '''
        metoda pro nastaveni okna odpovedi
        :param Form: form
        :param ob: ojednavka
        :param globalID: globalni id autoservisu
        :return: nastaveni okna
        '''
        Form.setObjectName("Form")
        Form.resize(860, 570)
        self.form = Form
        self.objed = ob
        self.globalId = globalID
        c = connection.Connection()
        self.con = c.con()
        self.us = metody.getUziv(self.con, metody.getIdUzivatele('student@spsejecna.cz', self.con))
        self.us = list(self.us[0])
        self.us.pop(0)
        self.us.pop(4)
        self.objed.pop(6)
        try:
            self.poz = metody.getObjednavkyPoz(self.con, self.objed[0])[0][0]

            self.poz = str(self.poz).replace('\n', '<br>')
        except Exception:
            self.poz = 'None'

        self.colmnW = [100, 120, 150, 250]
        self.objed.pop(6)

        obj = pd.DataFrame([
            self.objed,
        ], columns=['id','model', 'najeto', 'km', 'typ', 'rok_vyroby'], index=['Hodnota'])
        uz = pd.DataFrame([
            self.us,
        ], columns=['jmeno', 'prijmeni', 'usJmeno', 'email'], index=['Hodnota'])
        self.datum = datetime.date.today()
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.casEdit = QtWidgets.QTimeEdit(parent=Form)
        self.casEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.casEdit.setObjectName("casEdit")
        self.horizontalLayout_2.addWidget(self.casEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem3, 9, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.chybHlaska = QtWidgets.QLabel(parent=Form)
        self.chybHlaska.setText("")
        self.chybHlaska.setObjectName("chybHlaska")
        self.horizontalLayout_3.addWidget(self.chybHlaska)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_3, 11, 0, 1, 2)
        self.poznamkaVypis = QtWidgets.QTextBrowser(parent=Form)
        self.poznamkaVypis.setMaximumSize(QtCore.QSize(16777215, 120))
        self.poznamkaVypis.setObjectName("poznamkaVypis")
        self.gridLayout.addWidget(self.poznamkaVypis, 5, 0, 1, 2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.rbtn1 = QtWidgets.QRadioButton(parent=Form)
        self.rbtn1.setMinimumSize(QtCore.QSize(80, 0))
        self.rbtn1.setObjectName("rbtn30")
        self.horizontalLayout_8.addWidget(self.rbtn1)
        self.rbtn2 = QtWidgets.QRadioButton(parent=Form)
        self.rbtn2.setMinimumSize(QtCore.QSize(80, 0))
        self.rbtn2.setObjectName("rbtn1")
        self.horizontalLayout_8.addWidget(self.rbtn2)
        self.rbtn3 = QtWidgets.QRadioButton(parent=Form)
        self.rbtn3.setMinimumSize(QtCore.QSize(80, 0))
        self.rbtn3.setObjectName("rbtn2")
        self.horizontalLayout_8.addWidget(self.rbtn3)
        self.rbtnDele = QtWidgets.QRadioButton(parent=Form)
        self.rbtnDele.setMinimumSize(QtCore.QSize(80, 0))
        self.rbtnDele.setObjectName("rbtnDele")
        self.horizontalLayout_8.addWidget(self.rbtnDele)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_8, 8, 0, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem8, 6, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.btnOdpoved = QtWidgets.QPushButton(parent=Form)
        self.btnOdpoved.setObjectName("btnOdpoved")
        self.horizontalLayout.addWidget(self.btnOdpoved)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.gridLayout.addLayout(self.horizontalLayout, 13, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setMinimumSize(QtCore.QSize(80, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.poznamka = QtWidgets.QTextEdit(parent=Form)
        self.poznamka.setMaximumSize(QtCore.QSize(16777215, 120))
        self.poznamka.setObjectName("poznamka")
        self.horizontalLayout_5.addWidget(self.poznamka)
        self.gridLayout.addLayout(self.horizontalLayout_5, 10, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.datumEdit = QtWidgets.QDateEdit(parent=Form)
        self.datumEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.datumEdit.setObjectName("datumEdit")
        self.horizontalLayout_4.addWidget(self.datumEdit)
        spacerItem12 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.gridLayout.addLayout(self.horizontalLayout_4, 7, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem13, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setMinimumSize(QtCore.QSize(80, 0))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.tabulkaUz = QtWidgets.QTableView(parent=Form)
        self.tabulkaUz.setMaximumSize(QtCore.QSize(16777215, 55))
        self.tabulkaUz.setObjectName("tabulkaUz")
        self.horizontalLayout_7.addWidget(self.tabulkaUz)
        self.gridLayout.addLayout(self.horizontalLayout_7, 4, 0, 1, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setMinimumSize(QtCore.QSize(80, 0))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.tabulkaObj = QtWidgets.QTableView(parent=Form)
        self.tabulkaObj.setMaximumSize(QtCore.QSize(16777215, 55))
        self.tabulkaObj.setObjectName("tabulkaObj")
        self.horizontalLayout_6.addWidget(self.tabulkaObj)
        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 0, 1, 2)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem14, 14, 0, 1, 2)

        self.model = TableModel(uz)
        self.tabulkaUz.setModel(self.model)
        self.modelObj = TableModel(obj)
        self.tabulkaObj.setModel(self.modelObj)
        for i in self.colmnW:
            self.tabulkaUz.setColumnWidth(self.colmnW.index(i), i)
        self.datumEdit.setDate(QtCore.QDate(self.objed[5].year, self.objed[5].month, self.objed[5].day))
        self.btnOdpoved.clicked.connect(self.odeslat)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def odeslat(self):
        '''
        metoda pro tlacitko a opdeslani odpovedi uzivateli
        :return: odeslaniodpovedi do db
        '''
        cas = datetime.timedelta(hours=self.casEdit.time().hour(), minutes=self.casEdit.time().minute())
        datum = datetime.datetime(self.datumEdit.date().year(), self.datumEdit.date().month(), self.datumEdit.date().day())
        try:
            self.chybHlaska.setText('')
            odpoved.Odpoved.vytvorOdpoved(self.globalId, self.objed[0], datum, cas, [self.rbtn1.isChecked(), self.rbtn2.isChecked(), self.rbtn3.isChecked(), self.rbtnDele.isChecked()], self.poznamka.toPlainText())
            self.form.close()
        except odpoved.ProblemOdpoved as e:
            self.chybHlaska.setText(str(e))



    def retranslateUi(self, Form):
        '''
        metoda pro nastaveni textu v okne
        :param Form: form
        :return: nastaveni textu v okne
        '''
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Odpoved"))
        self.label_3.setText(_translate("Form", "Čas OD"))
        if self.poz != 'None':
            self.poznamkaVypis.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "hr { height: 1px; border-width: 0; }\n"
    "li.unchecked::marker { content: \"\\2610\"; }\n"
    "li.checked::marker { content: \"\\2612\"; }\n"
    "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+self.poz+"</p></body></html>"))
        else:
            self.poznamkaVypis.hide()
        self.rbtn1.setText(_translate("Form", "1 h"))
        self.rbtn2.setText(_translate("Form", "2 h"))
        self.rbtn3.setText(_translate("Form", "3 h"))
        self.rbtnDele.setText(_translate("Form", "celý den"))
        self.btnOdpoved.setText(_translate("Form", "Odpovědět"))
        self.label_5.setText(_translate("Form", "Poznámka"))
        self.label_2.setText(_translate("Form", "Datum"))
        self.label.setText(_translate("Form", "Odpověď"))
        self.label_7.setText(_translate("Form", "Uzivatel"))
        self.label_6.setText(_translate("Form", "Objednavka"))
