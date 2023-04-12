import hashlib
from conDB import connection, ochrana, metody
import re

class PrihlaseniError(Exception):
    def __init__(self, mes):
        self.mes = mes

class PrihlasZam:
    def __init__(self, autoservis=None, id=None, heslo=None):
        self.autoservis = autoservis
        self.id = id
        self.heslo = heslo

    @property
    def autoservis(self):
        return self._autoservis

    @autoservis.setter
    def autoservis(self, value):
        self._autoservis = value

    @property
    def heslo(self):
        return self._heslo

    @heslo.setter
    def heslo(self, value):
        self._heslo = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def hashPass(self):
        self.heslo = hashlib.sha256(self.heslo.encode()).hexdigest()

    def prehledZam(self):
        c = connection.Connection()
        con = c.con()
        cursor = con.cursor()
        sql = "select autoser_id, nazev,heslo from zam order by id"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        return myresult

    def pridejZam(self):
        c = connection.Connection()
        con = c.con()
        cursor = con.cursor()
        sql = "INSERT INTO zam (autoser_id, nazev, heslo) VALUES (%s, %s, %s)"
        val = (self.autoservis, self.id, self.heslo)
        cursor.execute(sql, val)
        c.commit()

    @staticmethod
    def prihlasitSe(autoser ,id, heslo):
        p = PrihlasZam()

        if ochrana.sql_injection(id) or ochrana.sql_injection(heslo):
            raise PrihlaseniError('Tento input je zakazan')
        if len(id) == 0:
            raise PrihlaseniError('Zadejte us jmeno')
        if len(heslo) == 0:
            raise PrihlaseniError('Zadejte heslo')
        if len(heslo) > 80:
            raise PrihlaseniError('Dlouhe heslo')
        p.autoservis = autoser
        p.id = id
        p.heslo = heslo
        p.hashPass()

        uzivatele = []
        for i in p.prehledZam():
            a = PrihlasZam(i[0], i[1], i[2])
            uzivatele.append(a)

        sautoservis = True
        sid = True
        sheslo = True
        for i in uzivatele:
            if i.autoservis == p.autoservis:
                sautoservis = False
                if i.id == p.id:
                    sid = False
                    if i.heslo == p.heslo:
                        sheslo = False
        if sid:
            raise PrihlaseniError('Špatné uživatelské jméno')
        if sheslo:
            raise PrihlaseniError('Špatné heslo')

    @staticmethod
    def registrace(autoS, jmeno, heslo, hesloP, con):
        p = PrihlasZam()
        usjmenoRE = r'^[a-zA-Z]{3,20}$'
        hesloRE = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{5,40}$'

        if not re.match(usjmenoRE, jmeno):
            raise PrihlaseniError('Uzivatelske jmeno nesplnuje podminky: delka 3 - 20 znaku | pouze pismena')
        if not re.match(hesloRE, heslo):
            raise PrihlaseniError('Heslo nesplnuje podminky: delka 5 - 40 | musi obsahovat cislice a pismena')
        if heslo == jmeno:
            raise PrihlaseniError('Heslo nesmí být stejné jako jméno')
        if heslo != hesloP:
            raise PrihlaseniError('Hesla nejsou stejna')
        if ochrana.sql_injection(jmeno) or ochrana.sql_injection(heslo) or ochrana.sql_injection(hesloP):
            raise PrihlaseniError('Tento input je zakazan')

        zamestanaci = metody.getZamJmeno(con, int(autoS))
        for i in zamestanaci:
            if i[0] == jmeno:
                raise PrihlaseniError('Toto usjmeno již existuje')

        p.autoservis = autoS
        p.id = jmeno
        p.heslo = heslo
        p.hashPass()
        p.pridejZam()
