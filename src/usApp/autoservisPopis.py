from src.usApp import autoservis
from src.conDB import connection, metody
import requests
import datetime


class AutoservisPopis (autoservis.Autoservisy):
    def __init__(self, globalId=None, nazev=None,mesto=None,ulice=None,psc=None,prodejAut=None, servisAut=None,email=None,url=None,logo=None, seznamTypu=list, seznamOtevreni=dict,seznamKontaktu=dict, stav=None):
        '''
        rozsirujici trida pro autoservisu, ktera je pouzita pro prehled autoservisu pro uzivatele
        :param globalId: globalni ID pro CZ
        :param nazev: nazev AS
        :param mesto: mesto sidliciho servisu
        :param ulice: ulice AS
        :param psc: postovni smerovaci cislo AS
        :param prodejAut: 1=pobocka prodava auta 0=neprodava
        :param servisAut: 1=pobocka ma autorizovany servis 0=nema
        :param email: email na AS
        :param url: url adresa na web AS
        :param logo: url adresa loga AS
        :param seznamTypu: seznam vsech moznych pobocek na adrese
        :param seznamOtevreni: seznam oteviraci doby dle pobocky
        :param seznamKontaktu: seznam kontaktu pro urcite pobocky
        :param stav: stav zda v ten moment je AS otevren nebo ma zavreno
        '''
        super().__init__(globalId,nazev,mesto,ulice,psc,prodejAut,servisAut,email,url,logo)
        self.seznamTypu = seznamTypu
        self.seznamOtevreni = seznamOtevreni
        self.seznamKontaktu = seznamKontaktu
        self.stav = stav
    
    @property
    def seznamTypu(self):
        return self._seznamTypu
    
    @seznamTypu.setter
    def seznamTypu(self, value):
        self._seznamTypu = value
    
    @property
    def seznamOtevreni(self):
        return self._seznamOtevreni
    
    @seznamOtevreni.setter
    def seznamOtevreni(self, value):
        self._seznamOtevreni = value
        
    @property
    def seznamKontaktu(self):
        return self._seznamKontaktu
    
    @seznamKontaktu.setter
    def seznamKontaktu(self, value):
        self._seznamKontaktu = value
    
    @property
    def stav(self):
        return self._stav
    
    @stav.setter
    def stav(self, value):
        self._stav = value

    def pridejTyp(self, value):
        '''
        metoda pro pridani typu AS
        :param value: typ AS
        :return: pridani do listu
        '''
        a = self.seznamTypu
        b = []
        if type(a) == list:
            for i in a:
                b.append(i)
            b.append(value)
            self.seznamTypu = b


    @staticmethod
    def vytvorPrehled(autoservis):
        a = AutoservisPopis()
        c = connection.Connection()
        con = c.con()
        cas = datetime.datetime.now()
        globalId = metody.getGlobalIdAutoservisu(autoservis, con)
        datum = f'{cas.year}-{cas.month}-{cas.day}'
        cass = f'{cas.hour}:{cas.hour}:{cas.second}'
        seznamTypu = []
        seznamKontaktu = {}
        seznamOtevreni = {}
        response = requests.get(
            f'https://retailers.skoda-auto.com/api/260/cs-CZ/Dealers/GetDealer?id={globalId}&clientDate={datum}%20{cass}')
        if response.status_code == 200:
            data = response.json()
            a.globalId = data['GlobalId']
            a.nazev = data['Name']
            a.mesto = data['Address']['City']
            a.psc = data['Address']['ZIP']
            a.ulice = data['Address']['Street']
            a.logo = data['LogoUrl']
            a.prodejAut = 1
            if data['HasSales'] == False:
                a.prodejAut = 0
            a.servisAut = 1
            if data['HasServices'] == False:
                a.servisAut = 0
            a.email = data['Contact']['Email']
            a.url = data['Contact']['WebUrl']
            a.stav = 1
            if data['IsOpenNow'] == False:
                a.stav = 0


            for i in data['Service']['Items']:
                seznamTypu.append(i['Name'])
                seznamKontaktu[i['Name']] = i['Contact']
                nazev = i['Name']
                dni = {}
                for j in i['OpeningHours']:
                    dni[j['WeekDay']] = j['Interval1From'], j['Interval1To']
                seznamOtevreni[nazev] = dni

            for i in data['Sale']['Items']:
                seznamTypu.append(i['Name'])
                seznamKontaktu[i['Name']] = i['Contact']
                nazev = i['Name']
                dni = {}
                for j in i['OpeningHours']:
                    dni[j['WeekDay']] = j['Interval1From'],j['Interval1To']
                seznamOtevreni[nazev] = dni
        else:
            seznamKontaktu = {'error': {'WebUrl': None, 'Email': None, 'Telephone': None, 'Telephone2': None, 'Mobile': None, 'Mobile2': None, 'WhatsApp': None}}
            seznamOtevreni = {'error': {1: (None, None), 2: (None, None), 3: (None, None), 4: (None, None), 5: (None, None), 6: (None, None), 7: (None, None)}}
        a.seznamTypu = seznamTypu
        a.seznamOtevreni = seznamOtevreni
        a.seznamKontaktu = seznamKontaktu
        web = 'WebUrl'
        what = 'WhatsApp'
        for i,x in a.seznamKontaktu.items():
            del x[web]
            del x[what]
        return a
