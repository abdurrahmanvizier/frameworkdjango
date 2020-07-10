from .fileengine import Get as FileEngine
from .mysqlengine import Get as MySQLEngine
# import cosmosengine as CosmosEngine
from .sqlserverengine import Get as SQLServerEngine

class Desc:
    def __init__(self, **keydict):
        print("Process Generate Object Columns")
        self.keydict = keydict

    def FileDesc(self):
        engine_get = FileEngine(createdby = self.keydict['createdby'])
        try:
            df = engine_get.ObjectDesc(servername = self.keydict['server_name'], 
                                    serverhostname = self.keydict['server_hostname'], 
                                    serverusername = self.keydict['server_user'], 
                                    serverpassword = self.keydict['server_password'], 
                                    filename = self.keydict['file_name'], 
                                    filepath = self.keydict['file_path'], 
                                    filedelimiter = self.keydict['file_delimiter'], 
                                    fileformat = self.keydict['format_type'], 
                                    objecthashkey = self.keydict['objecthashkey'])
            return df
        except:
            print("Ingest ObjectDesc Manualy")

    def MySQLDesc(self):
        
        engine_get = MySQLEngine(hostname = self.keydict['database_hostname'], 
                                databasename = self.keydict['database_name'], 
                                tablename = self.keydict['object_name'], 
                                username = self.keydict['database_user'], 
                                password = self.keydict['database_password'], 
                                port = self.keydict['database_port'],
                                createdby = self.keydict['createdby'])
        df = engine_get.ObjectDesc(self.keydict['objecthashkey'])
        print(df)
        return df

    def SQLServerDesc(self):
        engine_get = SQLServerEngine(hostname = self.keydict['database_hostname'], 
                                    databasename = self.keydict['database_name'], 
                                    tablename = self.keydict['object_name'], 
                                    username = self.keydict['database_user'], 
                                    password = self.keydict['database_password'], 
                                    port = self.keydict['database_port'],
                                    createdby = self.keydict['createdby'])
        df = engine_get.ObjectDesc(self.keydict['objecthashkey'])
        print(df)
        return df

    def CosmosDesc(self):
        from pymongo import MongoClient
        from datetime import datetime
        from bson import json_util
        
        servertunnel_name = self.keydict['servertunnel_name']
        servertunnel_hostname = self.keydict['servertunnel_hostname']
        servertunnel_port = self.keydict['servertunnel_port']
        servertunnel_user = self.keydict['servertunnel_user']
        servertunnel_password = self.keydict['servertunnel_password']
        servertunnel_pk_user = self.keydict['servertunnel_pk_user']
        servertunnel_pk_password = self.keydict['servertunnel_pk_password']

        database_application = self.keydict['database_application']
        database_name = self.keydict['database_name']
        database_hostname = self.keydict['database_hostname']
        database_port = self.keydict['database_port']
        database_user = self.keydict['database_user']
        database_password = self.keydict['database_password']

        all_data = {
                    "hostname" : servertunnel_hostname,
                    "port" : int(servertunnel_port),
                    "user" : servertunnel_user,
                    "pk_user" : servertunnel_pk_user,
                    "pk_password" : servertunnel_pk_password,
                    "site" : database_hostname.split('||')[0],
                    "site_port" : database_port,
                    "localport" : database_hostname.split('||')[1]
        }
        tunneling = Connect(**all_data)

        client = database_application
        databasename = database_name
        database_hostname = database_hostname.split('||')[0]

        tunneling.start()
        if database_application == 'seva-accounts':
            connection = MongoClient("mongodb://{}:{}@{}:{}/?ssl=true".format(database_user, database_password, database_hostname, database_port))
        else:
            connection = MongoClient("mongodb://{}:{}@{}:{}".format(database_user, database_password, database_hostname, database_port))
        engine_get = CosmosEngine.Get(connection = connection, client = client, databasename = databasename)
        df = engine_get.ObjectDesc(objecthashkey)
        df = df.replace("\r\n", "<CRLF>", regex=True).replace("\n\r", "<LFCR>", regex=True).replace("\n", "<CR>", regex=True).replace("\r", "<LF>", regex=True)
        connection.close()
        if all(x==True for x in tunneling.status().values()) == True:
            print(tunneling.status())
            tunneling.stop()
        else:
            print(tunneling.status())
        return df
