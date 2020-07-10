# -*- coding: utf-8 -*-

"""
framework engine

@author: Dul 20190718

""" 

from os import environ
from datetime import datetime

from sqlalchemy import create_engine
import pandas as pd

class Get:
    def __init__(self, spark = None, hostname = None, databasename = None, 
                 tablename = None, username = None, password = None, port = None,
                 createdby = None):
        print("SQLServer Get Function")
        self.spark = spark
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
        engine = create_engine("""mssql+pyodbc://{}:{}@{}:{}/{}?
                                  driver=ODBC+Driver+17+for+SQL+Server""".format(self.username, 
                                                                                 self.password, 
                                                                                 self.hostname, 
                                                                                 self.port,
                                                                                 self.databasename))
        df = pd.read_sql("{}".format(query), engine)
        return df

    def ObjectDesc(self, objecthashkey):
        tablename = self.tablename.split(".")
        query1 = "SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE FROM information_schema.columns WHERE table_name = '{}' and TABLE_SCHEMA = '{}'".format(tablename[1], tablename[0])
        query2 = "SELECT COLUMN_NAME FROM information_schema.CONSTRAINT_COLUMN_USAGE where table_name = '{}' and TABLE_SCHEMA = '{}' and CONSTRAINT_NAME like 'PK%'".format(tablename[1], tablename[0])
        #
        df1 = self.ReadTable(query = query1)
        df2 = self.ReadTable(query = query2)
        #
        key = ''
        if len(df2) == 0:
            key = 'null'
        else:
            key = df2['COLUMN_NAME'].to_list()

        ## Old Funtion Pimary Key
        # df1 = df1.withColumn('COLUMN_KEY', when((col("COLUMN_NAME") == key), '1').otherwise('0'))
        df1['COLUMN_KEY'] = df1['COLUMN_KEY'].apply(lambda x: '1' if x in key else '0')
        df1['IS_NULLABLE'] = df1['IS_NULLABLE'].apply(lambda x: '1' if x == 'YES' else '0')
        df1['objecthashkey_id'] = str(objecthashkey)
        df1.rename(columns = {"COLUMN_NAME": "deschashkey", "DATA_TYPE": "datatype", 
                             "CHARACTER_MAXIMUM_LENGTH": "length", "IS_NULLABLE": "nullable", 
                             "COLUMN_KEY": "primary"}, inplace=True)
        df1["objectdeschashkey"] = df1['objecthashkey_id'].map(str) + df1['deschashkey'].map(str)
        df1['sourcesystemcreatedby'] = str(self.sourcesystemcreatedby)
        df1['sourcesystemcreatedtime'] = self.sourcesystemcreatedtime
        return df1
     
        
