# -*- coding: utf-8 -*-

"""
framework engine

@author: Dul 20190718

"""
from os import environ
from datetime import datetime

import mysql.connector
import pandas as pd

class Get:
    def __init__(self, hostname = None, databasename = None, 
                 tablename = None, username = None, password = None, port = None,
                 createdby = None):
        print("MySQL Get Function")
        self.hostname = hostname
        self.databasename = databasename
        self.tablename = tablename
        self.username = username
        self.password = password
        self.port = port
        now = datetime.now()
        if createdby:
            self.sourcesystemcreatedby = createdby
        else:
            self.sourcesystemcreatedby = environ.get('USER')
        self.sourcesystemcreatedtime = (now.strftime("%Y-%m-%d %H:%M:%S"))


    def ReadTable(self, query = None):
        conn = mysql.connector.connect(user= self.username, password= self.password,
                                        host= self.hostname,database= self.databasename)
        df = pd.read_sql("{}".format(query), conn)
        return df

    def ReadTableAsia(self, query = None):
        conn = mysql.connector.connect(user= self.username, password= self.password,
                                        host= self.hostname,database= self.databasename,
                                        time_zone= "Asia/Jakarta")
        df = pd.read_sql("{}".format(query), conn)
        return df

    def ObjectDesc(self, objecthashkey):
        query = "SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE, COLUMN_KEY FROM information_schema.columns WHERE table_name = '{}'".format(self.tablename)
        #
        try:
            df = self.ReadTable(query = query)
        except:
            df = self.ReadTableAsia(query = query)
        #
        df['COLUMN_KEY'] = df['COLUMN_KEY'].apply(lambda x: '1' if x == 'PRI' else '0')
        df['IS_NULLABLE'] = df['IS_NULLABLE'].apply(lambda x: '1' if x == 'YES' else '0')
        df['objecthashkey_id'] = str(objecthashkey)
        df.rename(columns = {"COLUMN_NAME": "deschashkey", "DATA_TYPE": "datatype", 
                             "CHARACTER_MAXIMUM_LENGTH": "length", "IS_NULLABLE": "nullable", 
                             "COLUMN_KEY": "primary"}, inplace=True)
        df['length'] = df['length'].fillna(0).astype(int)

        df["objectdeschashkey"] = df['objecthashkey_id'].map(str) + df['deschashkey'].map(str)
        df['sourcesystemcreatedby'] = str(self.sourcesystemcreatedby)
        df['sourcesystemcreatedtime'] = self.sourcesystemcreatedtime
        return df