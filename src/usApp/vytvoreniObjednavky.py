import datetime
from src.conDB import metody, ochrana
from src.usApp import metody as metodyCas


class ChybaText(Exception):
    def __init__(self, mes):
        self.mes = mes

class Objednavka:
    def __init__(self, autoservis=None, model=None, vyroba=None, km=None, typ=None, datum=None, poz=None):
        """
        trida pro vytvoreni objednavky uzivatelem
        :param autoservis: autoservis
        :param model: model auta
        :param vyroba: rok vyrobeni auta
        :param km: najete kilometry auta
        :param typ: typ servisu
        :param datum: datum vytvoreni objednavky
        :param poz: poznamka od uz
        """
        self.autoservis = autoservis
        self.model = model
        self.vyroba = vyroba
        self.km = km
        self.typ = typ
        self.datum = datum
        self.poz = poz

    @property
    def autoservis(self):
        return self._autoservis

    @autoservis.setter
    def autoservis(self, value):
        self._autoservis = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def vyroba(self):
        return self._vyroba

    @vyroba.setter
    def vyroba(self, value):
        self._vyroba = value

    @property
    def km(self):
        return self._km

    @km.setter
    def km(self, value):
        self._km = value

    @property
    def typ(self):
        return self._typ

    @typ.setter
    def typ(self, value):
        self._typ = value

    @property
    def datum(self):
        return self._datum

    @datum.setter
    def datum(self, value):
        self._datum = value

    @property
    def poz(self):
        return self._poz

    @poz.setter
    def poz(self, value):
        self._poz = value

    def vlozeni(self, con, email):
        """
        metoda pro vlozeni objednavky do db
        :param con: connection
        :param email: email pro ziskani id
        :return: vlozeni do db
        """
        idUs = metody.getIdUzivatele(email, con)
        cursor = con.cursor()
        sql = "insert into objednavky(autoservis_id, model_id, rok_vyroby, km, typ, datum, poz, us_id) values (%s, %s, %s, %s, %s, %s, %s, %s);"
        val = [self.autoservis, self.model, self.vyroba, self.km, self.typ, self.datum, self.poz, idUs]
        cursor.execute(sql, val)
        con.commit()
        cursor.close()

    @staticmethod
    def vytvorObjednavku(autoservis,model,vyroba,km,typSer,typOpr,typBour,rok,mesic,den,poznamka, con):
        """
        metoda pro vytvoreni objednavky
        :param autoservis: id autoservisu
        :param model: model auta
        :param vyroba: rok vyrobeni auta
        :param km: najeto km
        :param typSer: rbtn pokud je zapnuty je nastaven na true
        :param typOpr: rbtn pokud je zapnuty je nastaven na true
        :param typBour: rbtn pokud je zapnuty je nastaven na true
        :param rok: rok objednavky
        :param mesic: mesic objednavky
        :param den: den objednavky
        :param poznamka: poznamka od uz
        :param con: connection
        :return: vlozeni objednavky do db
        """
        modelID = metody.getIdModelu(model, con)
        autoservisID = metody.getIdAutoservisu(autoservis, con)

        ted = datetime.datetime.now()
        if vyroba > ted.year:
            raise ChybaText('Tento rok vyroby neni mozny')

        if km == 0:
            raise ChybaText('Doplnte najete kilometry auta')

        typ = 0
        if typSer:
            typ = 1
        elif typBour:
            typ = 2
        elif typOpr:
            typ = 3
        else:
            raise ChybaText('Nezadali jste typ objednavky')

        if metodyCas.datumValidator(rok, mesic, den) == False:
            raise ChybaText('Nevalidni datum')
        elif rok < ted.year:
            raise ChybaText('Nevalidni datum rok')
        elif rok == ted.year and mesic < ted.month:
            raise ChybaText('Nevalidni datum mesic')
        elif rok == ted.year and mesic == ted.month and den <= ted.day:
            raise ChybaText('Nevalidni datum den')

        if len(poznamka) > 1000:
            raise ChybaText('Prilis dlouha poznamka')

        poz = ''
        if len(poznamka) == 0:
            poz = None
        elif ochrana.sql_injection(poznamka):
            raise ChybaText('Tento input je zakazan')
        else:
            poz = poznamka

        datum_obj = f'{rok}-{mesic}-{den}'
        obj = Objednavka()
        obj.autoservis = autoservisID
        obj.model = modelID
        obj.vyroba = vyroba
        obj.km = km
        obj.typ = typ
        obj.datum = datum_obj
        obj.poz = poz
        return obj









