import re
import hashlib
from src.conDB import connection, ochrana


class SpatnaRegistrError(Exception):
    def __init__(self, mes):
        self.mes = mes

class Registrace:
    def __init__(self, usjmeno=None, jmeno=None, prijmeni=None, heslo=None, email=None):
        self.usjmeno = usjmeno
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.heslo = heslo
        self.email = email
        c = connection.Connection()
        self.con = c.con()

    @property
    def usjmeno(self):
        return self._usjmeno

    @usjmeno.setter
    def usjmeno(self, value):
        self._usjmeno = value

    @property
    def jmeno(self):
        return self._jmeno

    @jmeno.setter
    def jmeno(self, value):
        self._jmeno = value

    @property
    def prijmeni(self):
        return self._prijmeni

    @prijmeni.setter
    def prijmeni(self, value):
        self._prijmeni = value

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
        cursor = self.con.cursor()
        sql = "select * from user order by id;"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        return myresult

    def pridaniUz(self):
        cursor = self.con.cursor()
        sql = "insert into user(jmeno, prijmeni, usjmeno, email, heslo) values  (%s, %s, %s, %s, %s);"
        val = [self.jmeno, self.prijmeni, self.usjmeno, self.email, self.heslo]
        cursor.execute(sql, val)
        self.con.commit()
        cursor.close()

    def vyhledesjPodleEmailu(self, email):
        cursor = self.con.cursor()
        sql = "select * from user where email='"+email+"' order by id;"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        return myresult

    def uyToString(self):
        return f'{self.jmeno}  {self.prijmeni}  {self.usjmeno}  {self.email}  {self.heslo}'

    @staticmethod
    def registrovatSe(jmeno, prijmeni, usjmeno, email, heslo):
        r = Registrace()

        usjmenoRE = r'^[a-zA-Z0-9_-]{5,20}$'
        jmenoRE = r'^[A-Z][a-z]{2,20}$'
        emailRE = r'^[a-zA-Z0-9._%+-]{1,50}@[a-zA-Z0-9.-]{1,20}\.[a-zA-Z]{2,10}$'
        hesloRE = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,40}$'

        if not re.match(usjmenoRE, usjmeno):
            raise SpatnaRegistrError('Uzivatelske jmeno nesplnuje podminky: delka 5 - 20 znaku | pouze pismena, cislice, \'_\' nebo \'-\'')
        if not re.match(jmenoRE, jmeno):
            raise SpatnaRegistrError('Jmeno nesplnuje podminky: delka 3 - 20 znaku | pouze pismena a prvni velke')
        if not re.match(jmenoRE, prijmeni):
            raise SpatnaRegistrError('Prijmeni nesplnuje podminky: delka 3 - 20 znaku | pouze pismena a prvni velke')
        if not re.match(hesloRE, heslo):
            raise SpatnaRegistrError('Heslo nesplnuje podminky: delka 8 - 40 | musi obsahovat cislice a pismena')
        if not re.match(emailRE, email):
            raise SpatnaRegistrError('Spatny email')
        if heslo == jmeno:
            raise SpatnaRegistrError('Heslo nesmí být stejné jako jméno')
        if ochrana.sql_injection(jmeno) or ochrana.sql_injection(prijmeni) or ochrana.sql_injection(usjmeno) or ochrana.sql_injection(email) or ochrana.sql_injection(heslo):
            raise SpatnaRegistrError('Tento input je zakazan')


        uzivatele = []
        for i in r.prehledUzivatelu():
            r2 = Registrace()
            r2.email = i[4]
            r2.heslo = i[5]
            r2.jmeno = i[1]
            r2.prijmeni = i[2]
            r2.usjmeno = i[3]
            uzivatele.append(r2)

        for i in uzivatele:
            if i.email == email:
                raise SpatnaRegistrError('Tento účet již existuje')


        r.email = email
        r.heslo = heslo
        r.jmeno = jmeno
        r.prijmeni = prijmeni
        r.usjmeno = usjmeno
        r.hashPass()
        r.pridaniUz()
