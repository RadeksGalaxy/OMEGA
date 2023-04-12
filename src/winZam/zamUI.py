from PyQt6 import QtCore
from PyQt6 import QtGui
from PyQt6 import QtWidgets
from src.conDB import connection, metody
from src.winZam import kalendar, odpovedObj, prihlaseniZam


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, auser, globalID):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 725)
        c = connection.Connection()
        con = c.con()
        self.okno = MainWindow
        self.autoservisId = auser
        self.globalId = globalID
        self.typy = ['','servis', 'bouračka', 'oprava']
        self.colmn = ['id','model', 'rok_vyroby', 'km', 'typ', 'datum', 'email', 'odpoved']
        self.colmnS = [90, 110, 120, 150, 100, 140, 200, 70]
        self.obj = []
        c = connection.Connection()
        self.con = c.con()
        for i in metody.getObjednavky(self.con, self.autoservisId, None, None):
            a = list(i)
            self.obj.append(a)

        for j in metody.getOdpovedi(self.con):
            for i in self.obj:
                if i[0] == j[1]:
                    i.append('✅')

        for i in self.obj:
            if len(i) == 7:
                i.append('❌')

        self.modely = metody.getModely(con)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.spinId = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinId.setMinimumSize(QtCore.QSize(80, 0))
        self.spinId.setObjectName("spinId")
        self.spinId.setMaximum(9999)
        self.horizontalLayout_6.addWidget(self.spinId)
        self.btnHledat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnHledat.setObjectName("btnHledat")
        self.horizontalLayout_6.addWidget(self.btnHledat)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.btnkalendar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnkalendar.setMaximumSize(QtCore.QSize(125, 16777215))
        self.btnkalendar.setObjectName("btnkalendar")
        self.horizontalLayout_3.addWidget(self.btnkalendar)
        self.btnOdhlasitse = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnOdhlasitse.setMaximumSize(QtCore.QSize(125, 16777215))
        self.btnOdhlasitse.setObjectName("btnOdhlasitse")
        self.horizontalLayout_3.addWidget(self.btnOdhlasitse)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.chybHlaska = QtWidgets.QLabel(parent=self.centralwidget)
        self.chybHlaska.setText("")
        self.chybHlaska.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.chybHlaska)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_7, 4, 0, 1, 1)
        self.tabulka = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tabulka.setObjectName("tabulka")
        if len(self.obj) != 0:
            self.tabulka.setColumnCount(len(self.obj[0]))
            for i in range(0 , len(self.obj[0])):
                item = QtWidgets.QTableWidgetItem()
                self.tabulka.setHorizontalHeaderItem(i, item)
            self.tabulka.setRowCount(0)
        else:
            self.tabulka.setColumnCount(0)
        self.obnovit()
        self.gridLayout.addWidget(self.tabulka, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboMode = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboMode.setObjectName("comboMode")
        self.comboMode.addItem("")
        for i in self.modely:
            self.comboMode.addItem("")
        self.horizontalLayout_2.addWidget(self.comboMode)
        self.comboTyp = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboTyp.setObjectName("comboTyp")
        #self.comboTyp.addItem("")
        for i in self.typy:
            self.comboTyp.addItem("")
        self.horizontalLayout_2.addWidget(self.comboTyp)
        self.comboOdpoved = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboOdpoved.setObjectName("comboOdpoved")
        self.comboOdpoved.addItem("")
        self.comboOdpoved.addItem("")
        self.comboOdpoved.addItem("")
        self.horizontalLayout_2.addWidget(self.comboOdpoved)
        self.btnRefresh = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnRefresh.setFont(font)
        self.btnRefresh.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/refresh.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnRefresh.setIcon(icon)
        self.btnRefresh.setIconSize(QtCore.QSize(22, 22))
        self.btnRefresh.setDefault(False)
        self.btnRefresh.setFlat(True)
        self.btnRefresh.setObjectName("btnRefresh")
        self.horizontalLayout_2.addWidget(self.btnRefresh)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem5, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1094, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btnOdhlasitse.clicked.connect(self.odhlasitSe)
        self.btnRefresh.clicked.connect(self.getCombo)
        self.btnRefresh.clicked.connect(self.obnovit)
        self.btnHledat.clicked.connect(self.hledatAkce)
        self.btnkalendar.clicked.connect(self.kalenndarAkce)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def odhlasitSe(self):
        prihlaseniZam.zobrazPrilaseni(self)
        self.okno.close()

    def kalenndarAkce(self):
        try:
            self.chybHlaska.setText('')
            kalendar.zobrazKalendar(self, self.globalId)
        except Exception as e:
            self.chybHlaska.setText(str(e))

    def hledatAkce(self):
        je = False
        for i in self.obj:
            if i[0] == self.spinId.value():
                je = True
                ob = i
        if je:
            try:
                self.chybHlaska.setText('')
                self.Form = QtWidgets.QWidget()
                self.ui = odpovedObj.Ui_Form()
                self.ui.setupUi(self.Form, ob, self.globalId)
                self.Form.show()
                self.getCombo()
                self.obnovit()
            except Exception as e:
                self.chybHlaska.setText(str(e))
        else:
            self.chybHlaska.setText('objednavka neni v seznamu')

    def getCombo(self):
        if self.comboMode.currentText() == '':
            model = None
        else:
            model = metody.getIdModelu(self.comboMode.currentText(), self.con)
        if self.comboTyp.currentText() == '':
            typ = None
        else:
            typ = self.comboTyp.currentIndex()
        self.obj = []
        for i in metody.getObjednavky(self.con, autoserId=self.autoservisId, model=model, typ=typ):
            a = list(i)
            self.obj.append(a)

        cc = connection.Connection()
        con = cc.con()
        for j in metody.getOdpovedi(con):
            for i in self.obj:
                if i[0] == j[1]:
                    i.append('✅')
        con.close()
        for i in self.obj:
            if len(i) == 7:
                i.append('❌')
        if self.comboOdpoved.currentText() == '':
            od = None
        else:
            od = self.comboOdpoved.currentText()
        lis = []
        if od != None:
            for i in self.obj:
                if i[7] == od:
                    lis.append(i)
        else:
            lis = self.obj
        self.obj = lis

    def obnovit(self):
        if len(self.obj) != 0:
            for i in range(0,len(self.obj[0])):
                self.tabulka.setColumnWidth(int(i),self.colmnS[i])
            for i in self.obj:
                i[4] = str(self.typy[i[4]])

            self.tabulka.setRowCount(0)
            for x,y in enumerate(self.obj):
                self.tabulka.insertRow(x)
                for j,k in enumerate(y):
                    self.tabulka.setItem(x, j, QtWidgets.QTableWidgetItem(str(k)))
        else:
            self.tabulka.setRowCount(0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Autoservis"))
        self.label_3.setText(_translate("MainWindow", "Otevřít ID"))
        self.btnHledat.setText(_translate("MainWindow", "Hledat"))
        self.label.setText(_translate("MainWindow", "Objdenávky"))
        self.btnOdhlasitse.setText(_translate("MainWindow", "Odhlásit se"))
        self.btnkalendar.setText(_translate("MainWindow", "Kalendář"))
        self.label_2.setText(_translate("MainWindow", "Filtr"))
        self.comboMode.setItemText(0, _translate("MainWindow", ""))
        for i in self.modely:
            self.comboMode.setItemText(self.modely.index(i)+1, _translate("MainWindow", str(i)))
        for i in self.typy:
            self.comboTyp.setItemText(self.typy.index(i), _translate("MainWindow", str(i)))
        self.comboOdpoved.setItemText(0, _translate("MainWindow", ''))
        self.comboOdpoved.setItemText(1, _translate("MainWindow", '✅'))
        self.comboOdpoved.setItemText(2, _translate("MainWindow", '❌'))
        if len(self.obj) != 0:
            for i in self.colmn:
                item = self.tabulka.horizontalHeaderItem(self.colmn.index(i))
                item.setText(_translate("MainWindow", str(i)))
        else:
            pass

def zobrazHlavniMenu(object=object, auservis=None, globalID=None):
    object.MainWindow = QtWidgets.QMainWindow()
    object.ui = Ui_MainWindow()
    object.ui.setupUi(object.MainWindow, auservis, globalID)
    object.MainWindow.show()

