import requests
from src.conDB import connection
import json
import datetime
from vendor.rp import resource_path

def aktualizaceSouboruOtevreni():
    """
    metoda pro aktualizovani oteviraci doby v souboru
    :return: zmena souboru
    """
    datum1 = f'{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day} {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}'
    c = connection.Connection()
    con = c.con()
    cursor = con.cursor()
    sql = "select global_id from autoservisy order by id;"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    cursor.close()
    lis = []
    for i in myresult:
        lis.append(i[0])
    cas = datetime.datetime.now()
    datum = f'{cas.year}-{cas.month}-{cas.day}'
    cass = f'{cas.hour}:{cas.hour}:{cas.second}'
    seznamOtevreni = {}
    seznamOtevreni['date'] = datum1
    for j in lis:
        id = j
        response = requests.get(
            f'https://retailers.skoda-auto.com/api/260/cs-CZ/Dealers/GetDealer?id={j}&clientDate={datum}%20{cass}')
        if response.status_code == 200:
            data = response.json()
            seznamTypu = []
            je = False
            for i in data['Service']['Items']:
                seznamTypu.append(i['Name'])
                nazev = i['Name']
                if nazev == 'Autorizovaný servis':
                    dni = {}
                    for j in i['OpeningHours']:
                        dni[j['WeekDay']] = j['Interval1From'], j['Interval1To']
                    seznamOtevreni[id] = dni
            for i in seznamTypu:
                if i == 'Autorizovaný servis':
                    je = True

            if je == True:
                pass
            else:
                raise Exception('error')
        else:
            raise Exception('error')

    json_object = json.dumps(seznamOtevreni, indent=2)
    with open(resource_path("src/datasets/oteviraciDoba.json"), "w") as outfile:
        outfile.write(json_object)


#aktualizaceSouboruOtevreni()