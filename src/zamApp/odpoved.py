import datetime
import json
from src.conDB import connection, ochrana
from vendor.rp import resource_path

class ProblemOdpoved(Exception):
    def __init__(self, mes):
        self.mes = mes

class Odpoved:
    def __init__(self, objId=None, datum=None, casPred=None, cas=None, delka=None, poz=None):
        self.odjId = objId
        self.datum = datum
        self.casPred = casPred
        self.cas = cas
        self.delka = delka
        self.poz = poz

    @property
    def objId(self):
        return self._obj_id

    @objId.setter
    def objId(self, value):
        self._obj_id = value

    @property
    def datum(self):
        return self._datum

    @datum.setter
    def datum(self, value):
        self._datum = value

    @property
    def casPred(self):
        return self._casPred

    @casPred.setter
    def casPred(self, value):
        self._casPred = value

    @property
    def cas(self):
        return self._cas

    @cas.setter
    def cas(self, value):
        self._cas = value

    @property
    def delka(self):
        return self._delka

    @delka.setter
    def delka(self, value):
        self._delka = value

    @property
    def poz(self):
        return self._poz

    @poz.setter
    def poz(self, value):
        self._poz =value

    def vlozObj(self, con):
        cursor = con.cursor()
        sql = "insert into odpoved(obj_id, datum, casPred, cas, delka, poz) values (%s, %s, %s, %s, %s, %s);"
        val = [self.objId, self.datum, self.casPred, self.cas, self.delka, self.poz]
        cursor.execute(sql, val)
        con.commit()
        cursor.close()

    @staticmethod
    def vytvorOdpoved(globalID=None, obj_id=None, datum=None, casServisu=None, delka=None, poznamka=None):
        o = Odpoved()
        c = connection.Connection()
        con = c.con()
        o.objId = obj_id
        o.casPred = casServisu
        dny = {
            'Mon': 1,
            'Tue': 2,
            'Wed': 3,
            'Thu': 4,
            'Fri': 5,
            'Sat': 6,
            'Sun': 7
        }

        cas = dny[datum.strftime("%a")]
        f = open(resource_path('src/datasets/oteviraciDoba.json'))
        data = json.load(f)
        a = data.pop('date')

        for x,y in data.items():
            if x == globalID:
                for i,j in y.items():
                    if int(i) == int(cas):
                        if j[0] != None:
                            otevrenoOd = str(j[0]).split(':')
                            otevrenoDo = str(j[1]).split(':')
                        else:
                            raise ProblemOdpoved('Tento den neni otevreno')

        delkaDic = {
            0: datetime.timedelta(hours=1),
            1: datetime.timedelta(hours=2),
            2: datetime.timedelta(hours=3),
            3: datetime.timedelta(hours=int(otevrenoDo[0]), minutes=int(otevrenoDo[1]))
        }
        index = 0
        je = False
        for i in delka:
            if i:
                je = True
                indexDelka = index
            index += 1
        if je == False:
            raise ProblemOdpoved('Zadejte delku servisu')

        if indexDelka != 3:
            if casServisu < datetime.timedelta(hours=int(otevrenoOd[0]), minutes=int(otevrenoOd[1])) or casServisu > delkaDic[3]:
                raise ProblemOdpoved('Upravte čas servisu')
            casServisu = casServisu + delkaDic[indexDelka]
            if casServisu > delkaDic[3]:
                raise ProblemOdpoved('Upravte délku času servisu')
        else:
            if casServisu < datetime.timedelta(hours=int(otevrenoOd[0]), minutes=int(otevrenoOd[1])) or casServisu > delkaDic[3]:
                raise ProblemOdpoved('Upravte čas servisu')
            casServisu = delkaDic[indexDelka]

        if poznamka == '':
            poznamka = None
        else:
            if ochrana.sql_injection(poznamka):
                raise ProblemOdpoved('Tento input je zakazan')
            if len(poznamka) > 1000:
                raise ProblemOdpoved('Příliš dlouhá poznámka')

        if datum < datetime.datetime.now():
            raise ProblemOdpoved('Špatný datum servisu')

        o.datum = datum
        o.cas = casServisu
        o.delka = indexDelka
        o.poz = poznamka
        o.vlozObj(con)

        f.close()
        con.close()
