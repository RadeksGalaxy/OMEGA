import json
import mysql.connector

'''
trida pro pripojeni do DB podle architektury singleton
'''
class Connection:
    def __init__(self):
        with open("../config/confDB.json", "r") as f:
            conf = json.load(f)
        if len(conf["host"]) == 0 or len(conf["user"]) == 0 or len(conf["password"]) == 0 or len(conf["database"]) == 0:
            raise Exception("wrong data input in conf file")
        self.connection = mysql.connector.connect(
            host=conf["host"],
            user=conf["user"],
            password=conf["password"],
            database=conf["database"],
            port=conf['port'],
        )
    '''
    metodat pro vytvoreni pripojeni do DB
    '''
    def con(self):
        return self.connection

