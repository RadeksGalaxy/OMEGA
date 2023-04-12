from PyQt6 import QtCore, QtGui, QtWidgets
from src.conDB import connection, metody
from vendor.tableModel import TableModel
import pandas as pd

class Ui_Form(object):
    def setupUi(self, Form, objID):
        Form.setObjectName("Form")
        Form.resize(768, 501)
        c = connection.Connection()
        con = c.con()
        self.form = Form
        self.objekt = metody.getOdpovedFinal(con, objID)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.chybHlaska = QtWidgets.QLabel(parent=Form)
        self.chybHlaska.setText("")
        self.chybHlaska.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.chybHlaska.setObjectName("chybHlaska")
        self.horizontalLayout_4.addWidget(self.chybHlaska)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_4, 6, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setMinimumSize(QtCore.QSize(80, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.tableOdpoved = QtWidgets.QTableView(parent=Form)
        self.tableOdpoved.setMaximumSize(QtCore.QSize(16777215, 75))
        self.tableOdpoved.setObjectName("tableOdpoved")
        self.horizontalLayout_2.addWidget(self.tableOdpoved)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.tableObjednavka = QtWidgets.QTableView(parent=Form)
        self.tableObjednavka.setMaximumSize(QtCore.QSize(16777215, 75))
        self.tableObjednavka.setObjectName("tableObjednavka")
        self.horizontalLayout.addWidget(self.tableObjednavka)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.poznamka = QtWidgets.QTextBrowser(parent=Form)
        self.poznamka.setMaximumSize(QtCore.QSize(16777215, 120))
        self.poznamka.setObjectName("poznamka")
        self.gridLayout.addWidget(self.poznamka, 5, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setMinimumSize(QtCore.QSize(80, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.tableAS = QtWidgets.QTableView(parent=Form)
        self.tableAS.setMaximumSize(QtCore.QSize(16777215, 75))
        self.tableAS.setObjectName("tableAS")
        self.horizontalLayout_5.addWidget(self.tableAS)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem2, 8, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btnPotvrdit = QtWidgets.QPushButton(parent=Form)
        self.btnPotvrdit.setObjectName("btnPotvrdit")
        self.horizontalLayout_3.addWidget(self.btnPotvrdit)
        self.btnZrusit = QtWidgets.QPushButton(parent=Form)
        self.btnZrusit.setObjectName("btnZrusit")
        self.horizontalLayout_3.addWidget(self.btnZrusit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 7, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)
        obj = pd.DataFrame(
            [self.objekt[0]]
            , columns=['objednavka_id', 'model', 'rok_vyroby', 'km', 'typ', 'datum'], index=[1])
        odpov = pd.DataFrame(
            [self.objekt[1]]
            , columns=['datum', 'cas_OD', 'delka', 'predpokladany_konec'], index=[1])
        AS = pd.DataFrame(
            [self.objekt[2]]
            , columns=['nazev', 'mesto', 'psc', 'ulice', 'prodej_aut', 'autorizovany_serivs'], index=[1])
        columnsASW = [220, 150, 100, 200, 100, 120]


        self.modelObj = TableModel(obj)
        self.tableObjednavka.setModel(self.modelObj)
        self.modelOd = TableModel(odpov)
        self.tableOdpoved.setModel(self.modelOd)
        self.modelAS = TableModel(AS)
        self.tableAS.setModel(self.modelAS)
        self.tableOdpoved.setColumnWidth(3, 160)
        for i in range(0, len(self.objekt[2])):
            self.tableAS.setColumnWidth(i, columnsASW[i])

        self.btnZrusit.clicked.connect(self.zrusitAkce)
        self.btnPotvrdit.clicked.connect(self.potvrditAkce)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        c.commit()

    def zrusitAkce(self):
        try:
            c = connection.Connection()
            con = c.con()
            metody.obnovaOdpovedi(con, 2, self.objekt[0][0])
            c.commit()
            self.form.close()
        except Exception as e:
            self.chybHlaska.setText(str(e))

    def potvrditAkce(self):
        try:
            c = connection.Connection()
            con = c.con()
            metody.obnovaOdpovedi(con, 1, self.objekt[0][0])
            c.commit()
            self.form.close()
        except Exception as e:
            self.chybHlaska.setText(str(e))


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "AS"))
        self.label.setText(_translate("Form", "Servis"))
        self.label_3.setText(_translate("Form", "Odpověď"))
        self.label_2.setText(_translate("Form", "Objednávka"))
        self.label_5.setText(_translate("Form", "info AS"))
        self.btnPotvrdit.setText(_translate("Form", "✅Potvrdit"))
        self.btnZrusit.setText(_translate("Form", "❌Zrušit"))
        self.poznamka.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "hr { height: 1px; border-width: 0; }\n"
    "li.unchecked::marker { content: \"\\2610\"; }\n"
    "li.checked::marker { content: \"\\2612\"; }\n"
    "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+self.objekt[3][0]+"</p></body></html>"))

def zobrazOdpovedId(object: object, objID):
    object.Form = QtWidgets.QWidget()
    object.ui = Ui_Form()
    object.ui.setupUi(object.Form , objID)
    object.Form.show()

