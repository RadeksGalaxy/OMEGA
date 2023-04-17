import datetime

import pandas as pd
from PyQt6 import QtCore, QtGui, QtWidgets
from src.conDB import connection, metody
from vendor.tableModel import TableModel


class Ui_Kalendar(object):
    def setupUi(self, Form, globalID):
        """
        metoda pro nastaveni okna kalendare zamestnancum
        :param Form: form
        :param globalID: globalnni id autoservisu
        :return: nastaveni okna
        """
        Form.setObjectName("Form")
        Form.resize(730, 535)
        self.globalId = globalID
        self.colmW = [90, 80, 80, 100, 40]
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 20, -1, 20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.kalendar = QtWidgets.QCalendarWidget(parent=Form)
        self.kalendar.setMaximumSize(QtCore.QSize(250, 250))
        self.kalendar.setObjectName("kalendar")
        self.horizontalLayout.addWidget(self.kalendar)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.chybHlaska = QtWidgets.QLabel(parent=Form)
        self.chybHlaska.setText("")
        self.chybHlaska.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.chybHlaska.setObjectName("chybHlaska")
        self.verticalLayout_3.addWidget(self.chybHlaska)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.btnHledat = QtWidgets.QPushButton(parent=Form)
        self.btnHledat.setObjectName("btnHledat")
        self.horizontalLayout_4.addWidget(self.btnHledat)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 3, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 3, 1, 1)
        self.tabulka = QtWidgets.QTableView(parent=Form)
        self.tabulka.setEnabled(True)
        self.tabulka.setMinimumSize(QtCore.QSize(0, 0))
        self.tabulka.setTabletTracking(False)
        self.tabulka.setAcceptDrops(False)
        self.tabulka.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tabulka.setAutoFillBackground(False)
        self.tabulka.setObjectName("tabulka")
        self.gridLayout.addWidget(self.tabulka, 4, 1, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem6, 5, 1, 1, 1)

        self.btnHledat.clicked.connect(self.obnovaAkce)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def obnovaAkce(self):
        """
        metoda na obnovu tebulky objednavek
        :return: obnova
        """
        try:
            datum = datetime.date(self.kalendar.selectedDate().year(), self.kalendar.selectedDate().month(), self.kalendar.selectedDate().day())
            c = connection.Connection()
            con = c.con()
            lis = metody.getOdpovediKalendar(con, datum, self.globalId)
            index = []
            for i in range(0, len(lis)):
                index.append(i+1)
            od = pd.DataFrame(
                lis
            , columns=['id_obj', 'cas_OD', 'cas_DO', 'delka', 'stav'], index=index)
            self.model = TableModel(od)
            self.tabulka.setModel(self.model)
            for i in range(0,len(self.colmW)):
                self.tabulka.setColumnWidth(i, self.colmW[i])
            self.chybHlaska.setText('datum: '+str(datum.year)+'-'+str(datum.month)+'-'+str(datum.day))
        except Exception as e:
            self.chybHlaska.setText(str(e))


    def retranslateUi(self, Form):
        """
        metoda na nastaveni textu okna
        :param Form: form
        :return: nastaveni textu
        """
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kalendář"))
        self.label.setText(_translate("Form", "Kalendář"))
        self.btnHledat.setText(_translate("Form", "Obnovit"))

def zobrazKalendar(object:object, globalID):
    """
    metoda pro zobrazeni okna kalendare
    :param object: objekt
    :param globalID: globalni id autoservisu
    :return: zobrazeni okna
    """
    object.Form = QtWidgets.QWidget()
    object.ui = Ui_Kalendar()
    object.ui.setupUi(object.Form, globalID)
    object.Form.show()

