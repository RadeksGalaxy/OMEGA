import json
import mysql.connector

class Connection:
    def __init__(self):
        '''
        trida pro pripojeni do DB podle architektury singleton
        '''
        with open("../OMEGA/config/confDB.json", "r") as f:
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

    def con(self):
        '''
        metodat pro vytvoreni pripojeni do DB
        '''
        return self.connection

    def commit(self):
        self.connection.commit()

