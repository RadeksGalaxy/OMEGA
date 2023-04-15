from PyQt6 import QtCore


class Ui_JedAutoserII:
    def hledatHledat(self):
        '''
        metoda pro tlacitko hledat jednotlive sekce AS
        :return: zmena kontaktu
        '''
        self.label_21.hide()
        self.lEmail.hide()
        self.label_17.hide()
        self.lTel1.hide()
        self.label_18.hide()
        self.lTel2.hide()
        self.label_19.hide()
        self.lTel3.hide()
        self.label_20.hide()
        self.lTel4.hide()
        index = 0
        index2 = 0
        for x in self.autoservis.seznamTypu:
            #print(x)
            if x == self.comboTypy.currentText():
                index2 = index
            index += 1
        kontakt = list(self.autoservis.seznamKontaktu.items())[index2][1]
        vyplnKontakt(kontakt['Email'], self.label_21, self.lEmail)
        vyplnKontakt(kontakt['Telephone'], self.label_17, self.lTel1)
        vyplnKontakt(kontakt['Telephone2'], self.label_18, self.lTel2)
        vyplnKontakt(kontakt['Mobile'], self.label_19, self.lTel3)
        vyplnKontakt(kontakt['Mobile2'], self.label_20, self.lTel4)
        otevreni = list(self.autoservis.seznamOtevreni.items())[index2][1]
        vyplnOtevreni(otevreni[1], self.lPondeli)
        vyplnOtevreni(otevreni[2], self.lUtery)
        vyplnOtevreni(otevreni[3], self.lStreda)
        vyplnOtevreni(otevreni[4], self.lCtvrtek)
        vyplnOtevreni(otevreni[5], self.lPatek)
        vyplnOtevreni(otevreni[6], self.lSobota)
        vyplnOtevreni(otevreni[7], self.lNedele)

    def retranslateUi(self, Form):
        '''
        metoda pro vzhled formu pro autoservis
        :param Form: form
        :return: nastaveni textu
        '''
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Autoservis"))
        self.lAutoservis.setText(_translate("Form", "Autoservis"))
        self.lOtevrenoZavreno.setText(_translate("Form", "Otevreno"))
        self.label_7.setText(_translate("Form", "Otevírací doba"))
        self.label_8.setText(_translate("Form", "Po"))
        self.lPondeli.setText(_translate("Form", "TextLabel"))
        self.label_9.setText(_translate("Form", "Út"))
        self.lUtery.setText(_translate("Form", "TextLabel"))
        self.label_10.setText(_translate("Form", "St"))
        self.lStreda.setText(_translate("Form", "TextLabel"))
        self.label_12.setText(_translate("Form", "Čt"))
        self.lCtvrtek.setText(_translate("Form", "TextLabel"))
        self.label_14.setText(_translate("Form", "Pá"))
        self.lPatek.setText(_translate("Form", "TextLabel"))
        self.label_15.setText(_translate("Form", "So"))
        self.lSobota.setText(_translate("Form", "TextLabel"))
        self.label_16.setText(_translate("Form", "Ne"))
        self.lNedele.setText(_translate("Form", "TextLabel"))
        self.label_13.setText(_translate("Form", "Kontakty"))
        self.lTel1.setText(_translate("Form", "TextLabel"))
        self.lTel2.setText(_translate("Form", "TextLabel"))
        self.lTel3.setText(_translate("Form", "TextLabel"))
        self.lTel4.setText(_translate("Form", "TextLabel"))
        self.lEmail.setText(_translate("Form", "TextLabel"))
        self.btnHledat.setText(_translate("Form", "Hledat"))
        self.lURLadresa.setText(_translate("Form", "URL"))
        self.lUlice.setText(_translate("Form", "Ulice"))
        self.lPSC.setText(_translate("Form", "PSC"))
        self.lMesto.setText(_translate("Form", "Mesto"))
        self.label_21.hide()
        self.lEmail.hide()
        self.label_17.hide()
        self.lTel1.hide()
        self.label_18.hide()
        self.lTel2.hide()
        self.label_19.hide()
        self.lTel3.hide()
        self.label_20.hide()
        self.lTel4.hide()
        self.lAutoservis.setText(self.autoservis.nazev)
        self.lMesto.setText(self.autoservis.mesto)
        self.lUlice.setText(self.autoservis.ulice)
        self.lPSC.setText(self.autoservis.psc)
        self.lURLadresa.setText(self.autoservis.url)
        index = 0
        for x in self.autoservis.seznamTypu:
            self.comboTypy.setItemText(index, _translate("Form", x))
            index += 1
        kontakt = list(self.autoservis.seznamKontaktu.items())[0][1]
        vyplnKontakt(kontakt['Email'], self.label_21, self.lEmail)
        vyplnKontakt(kontakt['Telephone'], self.label_17, self.lTel1)
        vyplnKontakt(kontakt['Telephone2'], self.label_18, self.lTel2)
        vyplnKontakt(kontakt['Mobile'], self.label_19, self.lTel3)
        vyplnKontakt(kontakt['Mobile2'], self.label_20, self.lTel4)
        otevreni = list(self.autoservis.seznamOtevreni.items())[0][1]
        vyplnOtevreni(otevreni[1], self.lPondeli)
        vyplnOtevreni(otevreni[2], self.lUtery)
        vyplnOtevreni(otevreni[3], self.lStreda)
        vyplnOtevreni(otevreni[4], self.lCtvrtek)
        vyplnOtevreni(otevreni[5], self.lPatek)
        vyplnOtevreni(otevreni[6], self.lSobota)
        vyplnOtevreni(otevreni[7], self.lNedele)
        if self.autoservis.stav == 1:
            self.lOtevrenoZavreno.setStyleSheet("QLabel { color : green; }")
            self.lOtevrenoZavreno.setText('Otevřeno')
        else:
            self.lOtevrenoZavreno.setStyleSheet("QLabel { color : red; }")
            self.lOtevrenoZavreno.setText('Zavřeno')

def vyplnKontakt(text, limg, ltext):
    '''
    metoda na vyplneni kontaktu
    :param text: text vlozeni
    :param limg: cesta obrazku
    :param ltext: cesta objektu
    :return: nastaveni textu
    '''
    if text != None:
        ltext.setText(text)
        limg.show()
        ltext.show()

def vyplnOtevreni(listik, lable):
    '''
    metoda pro zmenu otevreni doby
    :param listik: list otevreni
    :param lable: objekt
    :return: nastaveni textu otevreni
    '''
    if listik[0] != None or listik[1] != None:
        cas = f"{listik[0]} - {listik[1]}"
    else:
        cas = 'Zavřeno - Zavřeno'
    lable.setText(cas)