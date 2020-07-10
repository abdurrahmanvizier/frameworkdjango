from framework.models import *
from django.conf import settings
from django_pandas.io import read_frame

from .process_object_desc import Desc

from sqlalchemy import create_engine
from datetime import datetime

import pandas as pd

class ManualDesc:
    def __init__(self, request = None, object1 = None, object2 = None, dataframe_source = None):
        self.object1 = object1
        self.object2 = object2
        self.request = request
        self.dataframe_source = dataframe_source
        self.sourcesystemcreatedtime = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    def checkEngine(self, objectcheck):
        engine = ObjectStorageEngine.objects.values_list('storageenginehashkey', flat=True).get(objecthashkey=objectcheck)
        return engine

    def hiveColumnDesc(self, dataframe):
        type_match = {"bit": "int", "tinyint": "int", "smallint": "int", "mediumint": "int", "int": "int",
                      "bigint": "int", "float": "float", "double": "double", "decimal": "string", "date": "string",
                      "datetime": "timestamp", "timestamp": "timestamp", "time": "string", "year": "int",
                      "char": "string", "varchar": "string", "blob": "string", "text": "string", "tinyblob": "string",
                      "tinytext": "string", "mediumblob": "string", "mediumtext": "string", "longblob": "string",
                      "longtext": "string", "enum": "string", "set": "string", "binary": "string", "boolean": "boolean",
                      "string": "string", "geometry": "string", "nchar": "string", "nvarchar": "string",
                      "ntext": "string", "varbinary": "string", "image": "string", "numeric": "string",
                      "smallmoney": "string", "money": "string", "real": "string", "datetime2": "timestamp",
                      "smalldatetime": "timestamp", "datetimeoffset": "string", "point":"string", "json":"string",
                      "TimeStatus":"string", "timestatus":"string"}
        dataframe['datatype'] = dataframe['datatype'].map(type_match)

        return dataframe

    def generateDesc(self, objecthashkey, datainit = None):
        engine = self.checkEngine(objecthashkey)
        
        if engine == 'mysql':
            databasehashkey = ObjectDatabase.objects.values_list('databasehashkey', flat=True).get(objecthashkey=objecthashkey)
            data_database = Database.objects.filter(databasehashkey=databasehashkey).values()[0]
            data_dict = {
                "database_application":data_database['applicationname'], "database_name":data_database['databasename'],
                "database_hostname":data_database['hostname'], "database_port":data_database['port'], 
                "database_user":data_database['username'], "database_password":data_database['password'],
                "objecthashkey":objecthashkey, "object_name":objecthashkey[11:],
                "createdby":self.request.user.username
            }
            dataframe = Desc(**data_dict).MySQLDesc()
        
        elif engine == 'sqlserver':
            databasehashkey = ObjectDatabase.objects.values_list('databasehashkey', flat=True).get(objecthashkey=objecthashkey)
            data_database = Database.objects.filter(databasehashkey=databasehashkey).values()[0]
            data_dict = {
                "database_application":data_database['applicationname'], "database_name":data_database['databasename'],
                "database_hostname":data_database['hostname'], "database_port":data_database['port'], 
                "database_user":data_database['username'], "database_password":data_database['password'],
                "objecthashkey":objecthashkey, "object_name":objecthashkey[11:],
                "createdby":self.request.user.username
            }
            dataframe = Desc(**data_dict).SQLServerDesc()
        
        elif engine == 'file':
            if datainit is None:
                
                ## Get Server Info
                serverhashkey = ObjectServer.objects.values_list('serverhashkey', flat=True).get(objecthashkey=objecthashkey)
                data_server = Server.objects.filter(serverhashkey=serverhashkey).values()[0]
                
                ## Get File Info
                filehashkey = ObjectFile.objects.values_list('filehashkey', flat=True).get(objecthashkey=objecthashkey)
                data_file = File.objects.filter(filehashkey=filehashkey).values()[0]

                ## Get Type File Info
                objecttypehashkey = ObjectObjectType.objects.values_list('objecttypehashkey', flat=True).get(objecthashkey=objecthashkey)
                data_type = ObjectType.objects.filter(objecttypehashkey=objecttypehashkey).values()[0]

                data_dict = {
                    "server_name":data_server['servername'], "server_hostname":data_server['hostname'],
                    "server_user":data_server['user'], "server_password":data_server['password'], 
                    "file_name":data_file['filename'], "file_path":data_file['path'],
                    "file_delimiter":data_file['delimiter'], "format_type":data_type['objecttype'],
                    "objecthashkey":objecthashkey, "createdby":self.request.user.username
                }
                
                dataframe = Desc(**data_dict).FileDesc()
                
            elif datainit is not None:
                dataframe = datainit
                dataframe['objecthashkey_id'] = str(objecthashkey)
                dataframe["objectdeschashkey"] = dataframe['objecthashkey_id'].map(str) + dataframe['deschashkey'].map(str)
                dataframe['sourcesystemcreatedby'] = str(self.request.user.username)
                dataframe['sourcesystemcreatedtime'] = self.sourcesystemcreatedtime
        
        elif engine == 'cosmos':
            ## Get Database Info
            databasehashkey = ObjectDatabase.objects.values_list('databasehashkey', flat=True).get(objecthashkey=objecthashkey)
            data_database = Database.objects.filter(databasehashkey=databasehashkey).values()[0]

            ## Get Server Info
            servertunnelhashkey = ObjectServerTunnel.objects.values_list('servertunnelhashkey', flat=True).get(objecthashkey=objecthashkey)
            data_server = ServerTunnel.objects.filter(servertunnelhashkey=servertunnelhashkey).values()[0]

            data_dict = {
                "servertunnel_name":data_server['servertunnelname'], "servertunnel_hostname":data_server['hostname'],
                "servertunnel_port":data_server['port'], "servertunnel_user":data_server['user'],
                "servertunnel_password":data_server['password'], "servertunnel_pk_user":data_server['private_key_user'],
                "servertunnel_pk_password":data_server['private_key_password'], "database_application":data_database['applicationname'],
                "database_name":data_database['databasename'], "database_hostname":data_database['hostname'], "database_port":data_database['port'],
                "database_user":data_database['username'], "database_password":data_database['password']
            }

            dataframe = Desc(**data_dict).CosmosDesc()
        
        elif engine == 'hive':
            if datainit is not None:
                dataframe = self.hiveColumnDesc(dataframe = datainit)
                dataframe['objecthashkey_id'] = str(objecthashkey)
                dataframe["objectdeschashkey"] = dataframe['objecthashkey_id'].map(str) + dataframe['deschashkey'].map(str)
                dataframe['sourcesystemcreatedby'] = str(self.request.user.username)
                dataframe['sourcesystemcreatedtime'] = self.sourcesystemcreatedtime
            
            elif datainit is None:
                ### Check Object Process Source
                try:
                    src_objecthashkey_id = ObjectProcess.objects.values_list('src_objecthashkey_id', flat=True).get(dest_objecthashkey_id=objecthashkey)
                except Exception as e:
                    src_objecthashkey_id = None
                
                if src_objecthashkey_id:
                    dataframe = read_frame(ObjectDesc.objects.filter(objecthashkey_id=src_objecthashkey_id))
                    dataframe['objecthashkey_id'] = str(objecthashkey)
                    dataframe["objectdeschashkey"] = dataframe['objecthashkey_id'].map(str) + dataframe['deschashkey'].map(str)
                    dataframe['sourcesystemcreatedby'] = str(self.request.user.username)
                    dataframe['sourcesystemcreatedtime'] = self.sourcesystemcreatedtime
                else:
                    messages.info(request, "Process Hive Desc doesn't Exist")
        
        return dataframe, dataframe["objectdeschashkey"].iloc[0]

    def saveDF(self, dataframe):
        user = settings.DATABASES['explore']['USER']
        password = settings.DATABASES['explore']['PASSWORD']
        database_name = settings.DATABASES['explore']['NAME']
        hostname = settings.DATABASES['explore']['HOST']
        database_url = 'postgresql://{user}:{password}@{hostname}:5432/{database_name}'.format(
                        user=user,
                        password=password,
                        database_name=database_name,
                        hostname=hostname
                    )
        engine = create_engine(database_url, echo=False)
        dataframe.to_sql("objectdesc", engine, schema='explore', if_exists='append', index=False)
        print(dataframe)

    def mainProcess(self):
        objectdeschashkey = []
        try:
            if self.object1 and (self.dataframe_source is not None):
                df, objectdesc = self.generateDesc(self.object1)
                self.saveDF(df)
                objectdeschashkey.append(str(objectdesc))
                # status = "Success"
                if self.object2:
                    df, objectdesc = self.generateDesc(self.object2, df)
                    self.saveDF(df)
                    objectdeschashkey.append(str(objectdesc))
                    # status = "Success"
            elif self.dataframe_source:
                df, objectdesc = self.generateDesc(self.object2, self.dataframe_source)
                self.saveDF(df)
                objectdeschashkey.append(str(objectdesc))
                # status = "Success"
            status = "Success"
        except Exception as e:
            status = "Failed"
        
        return df, objectdeschashkey
