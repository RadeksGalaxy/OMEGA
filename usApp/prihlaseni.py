import hashlib
import re
from conDB import connection
from usApp import ochrana

class SpatnePrihlaseniError(Exception):
    def __init__(self, mes):
        self.mes = mes

class PrihlasSe:
    def __init__(self, email=None, heslo=None):
        self.email = email
        self.heslo = heslo

    @property
    def heslo(self):
        return self._heslo

    @heslo.setter
    def heslo(self, value):
        self._heslo = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    def hashPass(self):
        self.heslo = hashlib.sha256(self.heslo.encode()).hexdigest()

    def prehledUzivatelu(self):
        c = connection.Connection()
        con = c.con()
        cursor = con.cursor()
        sql = "select email,heslo from user order by id;"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        return myresult

    @staticmethod
    def prihlasitSe(email, heslo):
        l = PrihlasSe()
        emailRE = r'^[a-zA-Z0-9._%+-]{1,50}@[a-zA-Z0-9.-]{1,20}\.[a-zA-Z]{2,10}$'
        hesloRE = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,40}$'

        if not re.match(emailRE, email):
            raise SpatnePrihlaseniError('Spatny email')
        if not re.match(hesloRE, heslo):
            raise SpatnePrihlaseniError('Heslo nesplnuje podminky: delka 8 - 40 | musi obsahovat cislice a pismena')
        if ochrana.sql_injection(email) or ochrana.sql_injection(heslo):
            raise SpatnePrihlaseniError('Tento input je zakazan')
        l.heslo = heslo
        l.email = email
        l.hashPass()

        uzivatele = []
        for i in l.prehledUzivatelu():
            p = PrihlasSe()
            p.email = i[0]
            p.heslo = i[1]
            uzivatele.append(p)
        semail = True
        sheslo = True
        for i in uzivatele:
            if i.email == email:
                semail = False
                if i.heslo == l.heslo:
                    sheslo = False

        if semail:
            raise SpatnePrihlaseniError('Tento účet neexistuje')
        if sheslo:
            raise SpatnePrihlaseniError('Spatné heslo')
