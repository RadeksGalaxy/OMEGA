from conDB import connection

class ProblemDB(Exception):
    def __init__(self, mes):
        self.mes = mes

def nacteniAut():
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

def metoda1(ob : object, ob2 : object):
    for i in ob:
        ob2.addItem("")

def getIdModelu(model, con):
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
    cursor = con.cursor()
    sql = "select distinct nazev from autoservisy order by nazev;"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    cursor.close()
    return myresult

def getModely(con):
    cursor = con.cursor()
    sql = "select model from auto;"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    cursor.close()
    lis = []
    for i in myresult:
        lis.append(i[0])
    return lis

def getObjednavky(con, autoserId, typ=None, model=None):
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

def getAutoservis(con):
    cursor = con.cursor()
    sql = "select concat(nazev,' ',mesto) as jmeno from autoservisy order by jmeno;"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    cursor.close()
    listik = []
    for i in myresult:
        listik.append(i[0])
    return listik


def getAAA():
    c = connection.Connection()
    con = c.con()
    cursor = con.cursor()
    sql = "select poz from objednavky where length(poz) > 0;"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    cursor.close()
    return myresult[0][0].replace('\n','<br>')
