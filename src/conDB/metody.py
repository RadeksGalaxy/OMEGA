from src.conDB import connection


class ProblemDB(Exception):
    def __init__(self, mes):
        self.mes = mes

'''
soubor pro metody pro propojeni s databazi s pomocnymi objekty
metody jsou pojmenovane podle toho co se od nich ceka
'''
typ = {
    1: 'servis',
    2: 'bouračka',
    3: 'oprava'
}
stav = {
    1: '✅',
    2: '❌'
}
delka = {
    0: '1H',
    1: '2H',
    2: '3H',
    3: 'Cely den'
}
odpoved = {
    None: '⏳',
    1: '✅',
    2: '❌'
}


def nacteniAut():
    '''
    metoda pro nacteni vsech autoservisu
    :return: autoservis s mestem
    '''
    try:
        c = connection.Connection()
        con = c.con()
        cursor = con.cursor()
        sql = "select * from auto order by id;"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        lis = []
        for i in myresult:
            lis.append(i[1])
        return lis
    except Exception as e:
        raise ProblemDB('Error DB')

def metoda1(ob : object, ob2 : object):
    '''
    metoda pro pridani itemu do okna
    :param ob: objekt nazvu
    :param ob2: objekt v pyqt
    :return: pridani itemu
    '''
    for i in ob:
        ob2.addItem("")

def getIdModelu(model, con):
    '''
    metoda na ziskani id modelu auta
    :param model: nazev modelu
    :param con: conection
    :return: id modelu
    '''
    try:
        cursor = con.cursor()
        sql = "select id from auto where model = '"+model+"';"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        lis = []
        for i in myresult:
            lis.append(i[0])
        return lis[0]
    except Exception:
        raise ProblemDB('Problem s DB')

def getIdAutoservisu(autoservis, con):
    '''
    metoda pro ziskani id autoservisu
    :param autoservis: nazev autoservisu
    :param con: connection
    :return: id daneho autoservisu
    '''
    try:
        cursor = con.cursor()
        sql = "select id from autoservisy where concat(nazev,' ',mesto) = '"+autoservis+"';"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        lis = []
        for i in myresult:
            lis.append(i[0])
        return lis[0]
    except Exception:
        raise ProblemDB('Problem s DB')

def getGlobalIdAutoservisu(autoservis, con):
    '''
    metoda pro ziskani globalID autoservisu
    :param autoservis: nazev autoservis
    :param con: connection
    :return: vrati globalID daneho autoservisu
    '''
    try:
        cursor = con.cursor()
        sql = "select global_id from autoservisy where concat(nazev,' ',mesto) = '"+autoservis+"';"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        lis = []
        for i in myresult:
            lis.append(i[0])
        return lis[0]
    except Exception:
        raise ProblemDB('Problem s DB')

def getIdUzivatele(email, con):
    '''
    metoda pro ziskani id uzivatele
    :param email: email
    :param con: connnection
    :return: id daneho uzivatele s emailem
    '''
    try:
        cursor = con.cursor()
        sql = "select id from user where email = '"+email+"';"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        lis = []
        for i in myresult:
            lis.append(i[0])
        return lis[0]
    except Exception:
        raise ProblemDB('Problem s DB')

def getNazevAutoser(con):
    '''
    metoda pro ziskani nazvu autoservisu
    :param con: connection
    :return: autoservisy
    '''
    try:
        cursor = con.cursor()
        sql = "select distinct nazev from autoservisy order by nazev;"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        return myresult
    except Exception as e:
        raise ProblemDB('Error DB')

def getModely(con):
    '''
    metoda pro ziskani modelu z db
    :param con: connection
    :return: ziskani modelu
    '''
    try:
        cursor = con.cursor()
        sql = "select model from auto;"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        lis = []
        for i in myresult:
            lis.append(i[0])
        return lis
    except Exception as e:
        raise ProblemDB('Error DB')

def getObjednavky(con, autoserId, typ=None, model=None):
    '''
    metoda na ziskani objednavek pro autoservis
    :param con: connection
    :param autoserId: id autoservisu
    :param typ: typ servisu
    :param model: id modelu
    :return: vsechny objednavky splnujici hodnoty
    '''
    try:
        cursor = con.cursor()
        if typ == None and model == None:
            sql = f"select objednavky.id,a.model,rok_vyroby,km,typ,datum,u.email from objednavky inner join auto a on objednavky.model_id = a.id inner join user u on objednavky.us_id = u.id where autoservis_id={autoserId} and datum>=sysdate() order by datum;"
        elif typ != None and model == None:
            sql = f"select objednavky.id,a.model,rok_vyroby,km,typ,datum,u.email from objednavky inner join auto a on objednavky.model_id = a.id inner join user u on objednavky.us_id = u.id where autoservis_id={autoserId} and datum>=sysdate() and typ={typ} order by datum;"
        elif typ == None and model != None:
            sql = f"select objednavky.id,a.model,rok_vyroby,km,typ,datum,u.email from objednavky inner join auto a on objednavky.model_id = a.id inner join user u on objednavky.us_id = u.id where autoservis_id={autoserId} and datum>=sysdate() and model_id={model} order by datum;"
        else:
            sql = f"select objednavky.id,a.model,rok_vyroby,km,typ,datum,u.email from objednavky inner join auto a on objednavky.model_id = a.id inner join user u on objednavky.us_id = u.id where autoservis_id={autoserId} and datum>=sysdate() and typ={typ} and model_id={model} order by datum;"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        return myresult
    except Exception as e:
        raise ProblemDB('Error DB')

def getAutoservis(con):
    '''
    metoda pro ziskani nazvu autoservisu
    :param con: connection
    :return: autoservisy
    '''
    try:
        cursor = con.cursor()
        sql = "select concat(nazev,' ',mesto) as jmeno from autoservisy order by jmeno;"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        listik = []
        for i in myresult:
            listik.append(i[0])
        return listik
    except Exception as e:
        raise ProblemDB('Error DB')


def getObjednavkyPoz(con, id):
    '''
    metoda pro ziskani poznamku objednavky
    :param con: connection
    :param id: id vyhledavane
    :return: poznamka dle id
    '''
    try:
        cursor = con.cursor()
        sql = f'select poz from objednavky where id = {id};'
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        return myresult
    except Exception as e:
        raise ProblemDB('Error DB')

def getUziv(con, id):
    '''
    metoda pro vraceni uzivatele podle id
    :param con: connection
    :param id: vyhledavane id
    :return: uzivatel
    '''
    try:
        cursor = con.cursor()
        sql = f'select * from user where id = {id};'
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        return myresult
    except Exception as e:
        raise ProblemDB('Error DB')

def getOdpovedi(con):
    '''
    metoda pro vraceni odpovedi z db
    :param con: conection
    :return: odpovedi z db
    '''
    try:
        cursor = con.cursor()
        sql = f'select * from odpoved order by id;'
        cursor.execute(sql)
        myresult = cursor.fetchall()
        cursor.close()
        return myresult
    except Exception as e:
        raise ProblemDB('Error DB')


def getOdpovediUpravene(con, uz):
    '''
    vraceni odpovedi z db pro jednotliveho uzivatele
    :param con: connection
    :param uz: email uzivatele
    :return: vsechny odpovedi
    '''
    try:
        cursor = con.cursor()
        sql = f'select od.obj_id, o.typ, od.datum, od.casPred, od.cas, od.delka, od.odpoved ' \
              f'from odpoved od inner join objednavky o on od.obj_id = o.id inner join user u on o.us_id = u.id ' \
              f'where od.datum >= sysdate() and u.email = %s ' \
              f'order by od.datum;'
        val = [uz]
        cursor.execute(sql, val)
        myresult = cursor.fetchall()
        cursor.close()
        lis = []
        for i in myresult:
            lis.append(list(i))

        for i in lis:
            for j,k in typ.items():
                if i[1] == j:
                    i[1] = k
            for j,k in delka.items():
                if i[5] == str(j):
                    i[5] = k
            for j,k in odpoved.items():
                if i[6] == j:
                    i[6] = k
            i[3] = str(i[3])
            i[4] = str(i[4])


        return lis
    except Exception as e:
        raise ProblemDB('Error DB')

def getOdpovedFinal(con, objID):
    '''
    metoda pro vypsani konecne odpovedi z db podle id objednavky
    :param con: connection
    :param objID: id objednavky
    :return: vrati objednavku z db podle id
    '''
    try:
        cursor = con.cursor()
        sql = f'select autoservis_id from objednavky where id = {objID};'
        cursor.execute(sql)
        myresult = cursor.fetchall()

        sql1 = f'select o.id, auto.model, o.rok_vyroby, o.km, o.typ, o.datum from objednavky as o inner join auto on o.model_id=auto.id where o.id = {objID};'
        sql2 = f'select nazev, mesto, psc, ulice, prodejAut, servisAut from autoservisy where id = {myresult[0][0]};'
        sql3 = f'select datum, caspred, delka, cas from odpoved where obj_id = {objID};'
        sql4 = f'select poz from odpoved where obj_id = {objID};'

        cursor.execute(sql1)
        myresult1 = cursor.fetchall()
        myresult1 = list(myresult1[0])
        cursor.execute(sql3)
        myresult2 = cursor.fetchall()
        myresult2 = list(myresult2[0])
        cursor.execute(sql2)
        myresult3 = cursor.fetchall()
        myresult3 = list(myresult3[0])
        cursor.execute(sql4)
        myresult4 = cursor.fetchall()
        myresult4 = list(myresult4[0])

        for j,k in typ.items():
            if myresult1[4] == j:
                myresult1[4] = k
        for j,k in stav.items():
            if myresult3[4] == j:
                myresult3[4] = k
            if myresult3[5] == j:
                myresult3[5] = k
        for j,k in delka.items():
            if myresult2[2] == str(j):
                myresult2[2] = k
        myresult2[1] = str(myresult2[1])
        myresult2[3] = str(myresult2[3])
        myresult4[0] = str(myresult4[0]).replace('\n' , '<br>')

        return [myresult1, myresult2, myresult3, myresult4]
    except Exception as e:
        raise ProblemDB('Error DB')

def obnovaOdpovedi(con, val, id):
    '''
    metodda pro obnova odpovedi z db
    :param con: connection
    :param val: nova hodnota
    :param id: id odpovedi ktertou chceme zmenit
    :return: vrati zmenu v db
    '''
    try:
        cursor = con.cursor()
        sql = "update odpoved set odpoved= %s where obj_id= %s;"
        val = (val, id)
        cursor.execute(sql, val)
        cursor.close()
    except Exception as e:
        raise ProblemDB('Error DB')

def getOdpovediKalendar(con, datum, globalID):
    '''
    metoda pro vraceni odpovedi pro jednotlivy datum
    :param con: connection
    :param datum: datum ktery hledamu
    :param globalID: globalni id autoservisu
    :return: vsechny odpovedi z datumu
    '''
    try:
        cursor = con.cursor()
        sql = f'select o.obj_id, o.casPred, o.cas, o.delka, o.odpoved from odpoved as o inner join objednavky o2 on o.obj_id = o2.id where o.odpoved is not null and o.datum = %s and o2.autoservis_id = (select id from autoservisy where global_id = %s) order by o.id;'
        val = [datum, str(globalID)]
        cursor.execute(sql, val)
        myresult = cursor.fetchall()
        cursor.close()

        lis = []
        for i in myresult:
            lis.append(list(i))

        for i in lis:
            i[1] = str(i[1])
            i[2] = str(i[2])
            for j,k in delka.items():
                if i[3] == str(j):
                    i[3] = k
            for j,k in stav.items():
                if i[4] == j:
                    i[4] = k

        return lis
    except Exception as e:
        raise ProblemDB('Error DB')

def getZamJmeno(con, id):
    '''
    metoda pro nazev zamestnance
    :param con: connection
    :param id: id autoservisu
    :return: nazvy zamestnancu v jednotlivem autoservisu
    '''
    try:
        cursor = con.cursor()
        sql = f'select nazev from zam where autoser_id = %s;'
        val = [id]
        cursor.execute(sql, val)
        myresult = cursor.fetchall()
        cursor.close()

        lis = []
        for i in myresult:
            lis.append(list(i))

        return lis
    except Exception as e:
        raise ProblemDB('Error DB')

def getOdpovediJe(id):
    '''
    metoda na zjisteni cetnosti odpovedi
    :param id: id
    :return: je nebo neni odpoved v db
    '''
    c = connection.Connection()
    con = c.con()
    cursor = con.cursor()
    sql = f'select obj_id from odpoved where obj_id = %s;'
    val = [id]
    cursor.execute(sql, val)
    myresult = cursor.fetchall()
    cursor.close()
    if len(myresult) == 0:
        return True
    else:
        return False
