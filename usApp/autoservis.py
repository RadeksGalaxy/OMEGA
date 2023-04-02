import json
from conDB import connection

class Autoservisy:
    def __init__(self, globalId=None,nazev=None,mesto=None,ulice=None,psc=None,prodejAut=None,servisAut=None,email=None,url=None,logo=None):
        self.globalId = globalId
        self.nazev = nazev
        self.mesto = mesto
        self.ulice = ulice
        self.psc = psc
        self.prodejAut = prodejAut
        self.servisAut = servisAut
        self.email = email
        self.url = url
        self.logo = logo

    @property
    def globalId(self):
        return self._globalId

    @globalId.setter
    def globalId(self, value):
        self._globalId = value

    @property
    def nazev(self):
        return self._nazev

    @nazev.setter
    def nazev(self, value):
        self._nazev = value

    @property
    def mesto(self):
        return self._mesto

    @mesto.setter
    def mesto(self, value):
        self._mesto = value

    @property
    def ulice(self):
        return self._ulice

    @ulice.setter
    def ulice(self, value):
        self._ulice = value

    @property
    def psc(self):
        return self._psc

    @psc.setter
    def psc(self, value):
        self._psc = value

    @property
    def prodejAut(self):
        return self._prodejAut

    @prodejAut.setter
    def prodejAut(self, value):
        self._prodejAut = value

    @property
    def servisAut(self):
        return self._servisAut

    @servisAut.setter
    def servisAut(self, value):
        self._servisAut = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value

    def toString(self):
        return f'{self.nazev}  adresa:{self.mesto} {self.ulice} {self.psc}  prodej:{self.prodejAut}  servis:{self.servisAut}'

    @staticmethod
    def importAutoservisy():
        celkem = []
        with open('../src/datasets/czAutoservisySkoda.json', 'r') as f:
            data = json.load(f)

        for i in data['Items']:
            a = Autoservisy()
            a.globalId = i['GlobalId']
            a.nazev = i['Name']
            a.mesto = i['Address']['City']
            a.ulice = i['Address']['Street']
            a.psc = i['Address']['ZIP']
            a.logo = i['LogoUrl']
            a.prodejAut = 1
            if i['HasSales'] == False:
                a.prodejAut = 0
            a.servisAut = 1
            if i['HasServices'] == False:
                a.servisAut = 0
            celkem.append(a)
        c = connection.Connection()
        con = c.con()
        cursor = con.cursor()
        for i in celkem:
            sql = "insert into autoservisy(global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) values (%s, %s, %s, %s, %s, %s, %s, %s);"
            val = [i.globalId, i.nazev, i.mesto, i.ulice, i.psc, i.logo, i.prodejAut, i.servisAut]
            cursor.execute(sql, val)
        con.commit()
        cursor.close()

    @staticmethod
    def vypisAutoservis():
        c = connection.Connection()
        con = c.con()
        cursor = con.cursor()
        sql = "select concat(nazev,' ',mesto) as jmeno from autoservisy order by jmeno;"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        listik = []
        for i in myresult:
            listik.append(i[0])
        return listik
