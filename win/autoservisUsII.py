from PyQt6.QtWidgets import QMessageBox
from PyQt6.uic.properties import QtCore
from PyQt6 import QtCore
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon

from usApp import vytvoreniObjednavky
from win import prihlaseni
from win import uzivatel
from conDB import connection
from win import seznamAutoservisu
from conDB import metody as metodyDB

class Ui_pomoc:
    def retranslateUi(self, autoservisUs, jmeno):
        _translate = QtCore.QCoreApplication.translate
        autoservisUs.setWindowTitle(_translate("autoservisUs", "autoservisUs"))
        self.label_3.setText(_translate("autoservisUs", "Model"))
        self.rbtnServis.setText(_translate("autoservisUs", "Servis"))
        self.rbtnBouracka.setText(_translate("autoservisUs", "Bouračka"))
        self.rbtnOprava.setText(_translate("autoservisUs", "Oprava"))
        self.label_11.setText(_translate("autoservisUs", "Rok výroby"))
        self.label_12.setText(_translate("autoservisUs", "Najeté kilometry"))
        self.label.setText(_translate("autoservisUs", "Objednávka"))
        self.label_10.setText(_translate("autoservisUs", "Typ"))
        self.label_2.setText(_translate("autoservisUs", "Požadovaný datum"))
        self.btnOdeslat.setText(_translate("autoservisUs", "Odeslat"))
        self.label_5.setText(_translate("autoservisUs", "den"))
        self.label_6.setText(_translate("autoservisUs", "měsíc"))
        self.label_7.setText(_translate("autoservisUs", "rok"))
        for i in self.auta:
            self.comboModel.setItemText(self.auta.index(i), _translate("autoservisUs", i))
        for i in self.autoservis:
            self.comboAutoservis.setItemText(self.autoservis.index(i), _translate("autoservisUs", str(i)))
        self.label_9.setText(_translate("autoservisUs", "Autoservis"))
        self.label_4.setText(_translate("autoservisUs", "Poznámka"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("autoservisUs", "Vytvořit objednávku"))
        self.label_13.setText(_translate("autoservisUs", "Vyhledat: ID"))
        self.btnVyhledat.setText(_translate("autoservisUs", "Vyhledat"))
        self.label_8.setText(_translate("autoservisUs", "Odpovědi"))
        self.btnRefresh.setIcon(QIcon('../OMEGA/src/img/refresh.png'))
        self.btnRefresh.setIconSize(QSize(30, 30))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("autoservisUs", "Odpovědi"))
        self.btnOdhlasitse.setText(_translate("autoservisUs", "Odhlásit se"))
        self.btnUs.setIcon(QIcon('../OMEGA/src/img/user.png'))
        self.btnUs.setIconSize(QSize(22, 22))
        self.usjmeno.setText(_translate("autoservisUs", jmeno))
        self.btnAutoservisy.setText(_translate("autoservisUs", "Autoservisy"))

    def ui_prihlaseni(self):
        prihlaseni.zobrazUzivatele(self)
        self.autoservisUS.close()

    def ui_uzivatel(self, email):
        uzivatel.zobrazUzivatele(self, email)

    def zobrazAutoser(self):
        seznamAutoservisu.sezAutoser(self, self.autoservis, self.email)
        self.autoservisUS.close()

    def akceOdeslani(self):
        try:
            self.chybHlaska.setText('')
            c = connection.Connection()
            con = c.con()
            obj = vytvoreniObjednavky.Objednavka.vytvorObjednavku(self.comboAutoservis.currentText(),
                                                                  self.comboModel.currentText(),
                                                                  self.rokVyroby.value(),
                                                                  self.najeteKm.value(),
                                                                  self.rbtnServis.isChecked(),
                                                                  self.rbtnOprava.isChecked(),
                                                                  self.rbtnBouracka.isChecked(),
                                                                  self.rok.value(),
                                                                  self.mesic.value(),
                                                                  self.den.value(),
                                                                  self.poznamka.toPlainText(),
                                                                  con)

            dialog = QMessageBox(self.autoservisUS)
            dialog.setWindowTitle("Info")
            dialog.setText('Opravdu chcete odeslat objenávku?')
            yesbtn = QMessageBox.StandardButton.Yes
            nobtn = QMessageBox.StandardButton.No
            dialog.setStandardButtons(yesbtn | nobtn)
            dialog.setIcon(QMessageBox.Icon.Question)
            btn = dialog.exec()
            if btn == yesbtn:
                try:
                    obj.vlozeni(con,self.email)
                    self.chybHlaska.setText('Odesláno')
                except metodyDB.ProblemDB as e:
                    self.chybHlaska.setText(str(e))
                except Exception:
                    pass
            else:
                pass
        except metodyDB.ProblemDB as e:
            self.chybHlaska.setText(str(e))
        except vytvoreniObjednavky.ChybaText as e:
            self.chybHlaska.setText(str(e))
        except Exception:
            pass