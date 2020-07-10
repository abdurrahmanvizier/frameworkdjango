import sys
import pandas as pd
from datetime import datetime

from django.db.models import Max

from .funtions import *
from .process_object_desc import Desc

from framework.models import *
from framework.forms import ObjectRelationForm

from scripts.generateobjectdesc import ManualDesc

class MultipleObject:
    def __init__(self):
        print('Generate Multiple Object Relation')

    def addForm(self, request, **keydict):
        form = ObjectRelationForm(initial={
                'createdby': request.user.username,
            })
        ## List
        data_dict = {
            keydict["objecthashkey"]:"Object", keydict["objectownerhashkey"]:"ObjectOwner",
            keydict["objectstorageenginehashkey"]:"ObjectStorageEngine", keydict["objectobjecttypehashkey"]:"ObjectObjectType", 
            keydict["objectdatabasehashkey"]:"ObjectDatabase", keydict["objectserverhashkey"]:"ObjectServer",
            keydict["objectservertunnelhashkey"]:"ObjectServerTunnel", keydict["objectfilehashkey"]:"ObjectFile", 
            keydict["objectobjectpartitionhashkey"]:"ObjectObjectPartition", keydict["objectobjectsnapshothashkey"]:"ObjectObjectSnapShot", 
            keydict["objectqueryhashkey"]:"ObjectQuery", keydict["objectdeschashkey"]:"ObjectDesc"
        }
        ## Generate Object Instance

        ## Fake Commit
        chackpoint_form = form.save(commit=False)

    
    def checkhashkey(self, request, df_inputs):
        for i in range(1,4):
            for x in  range(df_inputs["objectname_{}".format(i)].count()):
                if df_inputs["objectname_{}".format(i)][x] != 'nan':
                    if (str(df_inputs['ownerhashkey_{}'.format(i)][x]) != 'nan') and (Owner.objects.filter(ownerhashkey=str(df_inputs['ownerhashkey_{}'.format(i)][x])).exists() == False):
                        messages.info(request, "Ownerhashkey doesn't Exist")
                        return redirect("addoneobject")
                    if (str(df_inputs['storageenginehashkey_{}'.format(i)][x]) != 'nan') and (StorageEngine.objects.filter(storageenginehashkey=str(df_inputs['storageenginehashkey_{}'.format(i)][x])).exists() == False):
                        messages.info(request, "StorageEnginehashkey doesn't Exist")
                        return redirect("addoneobject")
                    if (str(df_inputs['objecttypehashkey_{}'.format(i)][x]) != 'nan') and (ObjectType.objects.filter(objecttypehashkey=str(df_inputs['objecttypehashkey_{}'.format(i)][x])).exists() == False):
                        messages.info(request, "ObjectTypehashkey doesn't Exist")
                        return redirect("addoneobject")
                    if (str(df_inputs['databasehashkey_{}'.format(i)][x]) != 'nan') and (Database.objects.filter(databasehashkey=str(df_inputs['databasehashkey_{}'.format(i)][x])).exists() == False):
                        messages.info(request, "Databasehashkey doesn't Exist")
                        return redirect("addoneobject")
                    if (str(df_inputs['serverhashkey_{}'.format(i)][x]) != 'nan') and (Server.objects.filter(serverhashkey=str(df_inputs['serverhashkey_{}'.format(i)][x])).exists() == False):
                        messages.info(request, "Serverhashkey doesn't Exist")
                        return redirect("addoneobject")
                    if (str(df_inputs['servertunnelhashkey_{}'.format(i)][x]) != 'nan') and (ServerTunnel.objects.filter(servertunnelhashkey=str(df_inputs['servertunnelhashkey_{}'.format(i)][x])).exists() == False):
                        messages.info(request, "ServerTunnelhashkey doesn't Exist")
                        return redirect("addoneobject")
                    if (str(df_inputs['filehashkey_{}'.format(i)][x]) != 'nan') and (File.objects.filter(filehashkey=str(df_inputs['filehashkey_{}'.format(i)][x])).exists() == False):
                        messages.info(request, "Filehashkey doesn't Exist")
                        return redirect("addoneobject")
                    if (str(df_inputs['objectpartitionhashkey_{}'.format(i)][x]) != 'nan') and (PartitionBy.objects.filter(objectpartitionhashkey=str(df_inputs['objectpartitionhashkey_{}'.format(i)][x])).exists() == False):
                        messages.info(request, "Partitionhashkey doesn't Exist")
                        return redirect("addoneobject")
                    if (str(df_inputs['objectsnapshothashkey_{}'.format(i)][x]) != 'nan') and (SnapShot.objects.filter(objectsnapshothashkey=str(df_inputs['objectsnapshothashkey_{}'.format(i)][x])).exists() == False):
                        messages.info(request, "Snapshothashkey doesn't Exist")
                        return redirect("addoneobject")
                    if (str(df_inputs['queryhashkey_{}'.format(i)][x]) != 'nan') and (Query.objects.filter(queryhashkey=str(df_inputs['queryhashkey_{}'.format(i)][x])).exists() == False):
                        messages.info(request, "Queryhashkey doesn't Exist")
                        return redirect("addoneobject")
                    if str(i) != str("1"):
                        if (str(df_inputs['processenginehashkey_{}'.format(i)][x]) != 'nan') and (ProcessEngine.objects.filter(processenginehashkey=str(df_inputs['processenginehashkey_{}'.format(i)][x])).exists() == False):
                            messages.info(request, "Process Engine doesn't Exist")
                            return redirect("addprocessengine")
                        if (str(df_inputs['usershashkey_{}'.format(i)][x]) != 'nan') and (ObjectUser.objects.filter(userhashkey=str(df_inputs['usershashkey_{}'.format(i)][x])).exists() == False):
                            messages.info(request, "Object User doesn't Exist")
                            return redirect("adduser")

    def InputObject(self, request, df_inputs):
        #check nan
        sourcesystemcreatedby = request.user.username
        sourcesystemcreatedtime = datetime.now()
        for i in range(1,4):
            if df_inputs["objectname_{}".format(i)][0] != 'nan':
                if str(i) == str("1"):
                    tamplate_cols = ["objectname_{i}", "objectdesc_{i}", "ownerhashkey_{i}", "storageenginehashkey_{i}",
                                    "objecttypehashkey_{i}", "databasehashkey_{i}", "serverhashkey_{i}", "servertunnelhashkey_{i}", "filehashkey_{i}",
                                    "objectpartitionhashkey_{i}", "objectsnapshothashkey_{i}", "queryhashkey_{i}"]
                    col = [x.format(i=i) for x in tamplate_cols]
                    df_input = df_inputs[col]
                    df_input.columns = ["objectname", "objectdesc", "ownerhashkey", "storageenginehashkey",
                                        "objecttypehashkey", "databasehashkey", "serverhashkey", "servertunnelhashkey", "filehashkey",
                                        "objectpartitionhashkey", "objectsnapshothashkey", "queryhashkey"]
                    list_objecthashkey_source = self.InputObjectSource(request, df_input, sourcesystemcreatedby, sourcesystemcreatedtime)
                else:
                    tamplate_cols = ["objectname_{i}", "objectdesc_{i}", "ownerhashkey_{i}", "storageenginehashkey_{i}",
                                    "objecttypehashkey_{i}", "databasehashkey_{i}", "serverhashkey_{i}", "servertunnelhashkey_{i}", "filehashkey_{i}",
                                    "objectpartitionhashkey_{i}", "objectsnapshothashkey_{i}", "queryhashkey_{i}",
                                    "processenginehashkey_{i}", "usershashkey_{i}"]
                    col = [x.format(i=i) for x in tamplate_cols]
                    df_input = df_inputs[col]
                    df_input.columns = ["objectname", "objectdesc", "ownerhashkey", "storageenginehashkey",
                                        "objecttypehashkey", "databasehashkey", "serverhashkey", "servertunnelhashkey", "filehashkey",
                                        "objectpartitionhashkey", "objectsnapshothashkey", "queryhashkey",
                                        "processenginehashkey", "usershashkey"]
                    ### Len Harus Sama
                    if len(list_objecthashkey_source) == len(df_input):
                        df_input['objecthashkey'] = list_objecthashkey_source
                        list_objecthashkey_source = self.InputObjectTarget(request, df_input, sourcesystemcreatedby, sourcesystemcreatedtime)


    def InputObjectSource(self, request, df_input, sourcesystemcreatedby, sourcesystemcreatedtime):
        list_objecthashkey_source = []
        #input Object
        for x in range(df_input.objectname.count()):
            # objecthashkey = engine_post.Object(spark, df_input.objectname[x], df_input.objectdesc[x])
            objecthashkey = addobject(request, df_input.objectname[x], df_input.objectdesc[x], sourcesystemcreatedby, sourcesystemcreatedtime)
            list_objecthashkey_source.append(objecthashkey)
            ## Change objecthashkey string to objecthashkey object django
            objecthashkey = Object.objects.get(objecthashkey=objecthashkey)
            if str(df_input.ownerhashkey[x]) != "nan":
                # engine_post.ObjectOwner(spark, objecthashkey, str(df_input.ownerhashkey[x]))
                objectownerhashkey = addobjectowner(request, objecthashkey, str(df_input.ownerhashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectStorageEngine
            if str(df_input.storageenginehashkey[x]) != "nan":
                # engine_post.ObjectStorageEngine(spark, objecthashkey, str(df_input.storageenginehashkey[x]))
                objectstorageenginehashkey = addobjectstorageengine(request, objecthashkey, str(df_input.storageenginehashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectObjectType
            if str(df_input.objecttypehashkey[x]) != "nan":
                # engine_post.ObjectObjectType(spark, objecthashkey, str(df_input.objecttypehashkey[x]))
                objectobjecttypehashkey = addobjectobjecttype(request, objecthashkey, str(df_input.objecttypehashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectDatabase
            if str(df_input.databasehashkey[x]) != "nan":
                # engine_post.ObjectDatabase(spark, objecthashkey, str(df_input.databasehashkey[x]))
                objectdatabasehashkey = addobjectdatabase(request, objecthashkey, str(df_input.databasehashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectServer
            if str(df_input.serverhashkey[x]) != "nan":
                # engine_post.ObjectServer(spark, objecthashkey, str(df_input.serverhashkey[x]))
                objectserverhashkey = addobjectserver(request, objecthashkey, str(df_input.serverhashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectServerTunnel
            if str(df_input.servertunnelhashkey[x]) != "nan":
                # engine_post.ObjectServerTunnel(spark, objecthashkey, str(df_input.servertunnelhashkey[x]))
                objectservertunnelhashkey = addobjectservertunnel(request, objecthashkey, str(df_input.servertunnelhashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectFile
            if str(df_input.filehashkey[x]) != "nan":
                # engine_post.ObjectFile(spark, objecthashkey, str(df_input.filehashkey[x]))
                objectfilehashkey = addobjectfile(request, objecthashkey, str(df_input.filehashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectObjectPartition
            if str(df_input.objectpartitionhashkey[x]) != "nan":
                # engine_post.ObjectObjectPartition(spark, objecthashkey, str(df_input.objectpartitionhashkey[x]))
                objectobjectpartitionhashkey = addobjectobjectpartition(request, objecthashkey, str(df_input.objectpartitionhashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectObjectSnapshot
            if str(df_input.objectsnapshothashkey[x]) != "nan":
                # engine_post.ObjectObjectSnapshot(spark, objecthashkey, str(df_input.objectsnapshothashkey[x]))
                objectobjectsnapshothashkey = addobjectobjectsnapshot(request, objecthashkey, str(df_input.objectsnapshothashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectQuery
            if str(df_input.queryhashkey[x]) != "nan":
                # engine_post.ObjectQuery(spark, objecthashkey, str(df_input.queryhashkey[x]))
                objectprocesshashkey = addobjectquery(request, objecthashkey, str(df_input.queryhashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectDesc
            storageengine = str(df_input.storageenginehashkey[x])
            # print(storageengine)
            self.dataframe_desc, objectdeschashkey = ManualDesc(request = request, object1 = objecthashkey).mainProcess()
            objectdeschashkey = objectdeschashkey[0]
            
            ### Add to Form
            self.addForm(request, {
                "objecthashkey":objecthashkey, "objectownerhashkey":objectownerhashkey,"objectstorageenginehashkey":objectstorageenginehashkey,
                "objectobjecttypehashkey":objectobjecttypehashkey, "objectdatabasehashkey":objectdatabasehashkey, "objectserverhashkey":objectserverhashkey,
                "objectservertunnelhashkey":objectservertunnelhashkey, "objectfilehashkey":objectfilehashkey, "objectobjectpartitionhashkey":objectobjectpartitionhashkey,
                "objectobjectsnapshothashkey":objectobjectsnapshothashkey, "objectqueryhashkey":objectqueryhashkey, "objectdeschashkey":objectdeschashkey
            })

        return list_objecthashkey_source

    def InputObjectTarget(self, request, df_input, sourcesystemcreatedby, sourcesystemcreatedtime):
        # input Object
        list_objecthashkey_source = []
        for x in range(df_input.objectname.count()):
            objecthashkey_source = str(df_input.objecthashkey[x])
            # objecthashkey_target = engine_post.Object(spark, df_input.objectname[x], df_input.objectdesc[x])
            objecthashkey_target = addobject(request, df_input.objectname[x], df_input.objectdesc[x], sourcesystemcreatedby, sourcesystemcreatedtime)
            objecthashkey = objecthashkey_target
            list_objecthashkey_source.append(objecthashkey_target)
            ## Change objecthashkey string to objecthashkey object django
            objecthashkey = Object.objects.get(objecthashkey=objecthashkey)
            if str(df_input.ownerhashkey[x]) != "nan":
                # engine_post.ObjectOwner(spark, objecthashkey, str(df_input.ownerhashkey[x]))
                addobjectowner(request, objecthashkey, str(df_input.ownerhashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectStorageEngine
            if str(df_input.storageenginehashkey[x]) != "nan":
                # engine_post.ObjectStorageEngine(spark, objecthashkey, str(df_input.storageenginehashkey[x]))
                addobjectstorageengine(request, objecthashkey, str(df_input.storageenginehashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectObjectType
            if str(df_input.objecttypehashkey[x]) != "nan":
                # engine_post.ObjectObjectType(spark, objecthashkey, str(df_input.objecttypehashkey[x]))
                addobjectobjecttype(request, objecthashkey, str(df_input.objecttypehashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectDatabase
            if str(df_input.databasehashkey[x]) != "nan":
                # engine_post.ObjectDatabase(spark, objecthashkey, str(df_input.databasehashkey[x]))
                addobjectdatabase(request, objecthashkey, str(df_input.databasehashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectServer
            if str(df_input.serverhashkey[x]) != "nan":
                # engine_post.ObjectServer(spark, objecthashkey, str(df_input.serverhashkey[x]))
                addobjectserver(request, objecthashkey, str(df_input.serverhashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectServerTunnel
            if str(df_input.servertunnelhashkey[x]) != "nan":
                # engine_post.ObjectServerTunnel(spark, objecthashkey, str(df_input.servertunnelhashkey[x]))
                addobjectservertunnel(request, objecthashkey, str(df_input.servertunnelhashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectFile
            if str(df_input.filehashkey[x]) != "nan":
                # engine_post.ObjectFile(spark, objecthashkey, str(df_input.filehashkey[x]))
                addobjectfile(request, objecthashkey, str(df_input.filehashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectObjectPartition
            if str(df_input.objectpartitionhashkey[x]) != "nan":
                # engine_post.ObjectObjectPartition(spark, objecthashkey, str(df_input.objectpartitionhashkey[x]))
                addobjectobjectpartition(request, objecthashkey, str(df_input.objectpartitionhashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectObjectSnapshot
            if str(df_input.objectsnapshothashkey[x]) != "nan":
                # engine_post.ObjectObjectSnapshot(spark, objecthashkey, str(df_input.objectsnapshothashkey[x]))
                addobjectobjectsnapshot(request, objecthashkey, str(df_input.objectsnapshothashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectQuery
            if str(df_input.queryhashkey[x]) != "nan":
                # engine_post.ObjectQuery(spark, objecthashkey, str(df_input.queryhashkey[x]))
                addobjectquery(request, objecthashkey, str(df_input.queryhashkey[x]), sourcesystemcreatedby, sourcesystemcreatedtime)
            # input ObjectDesc
            storageengine = str(df_input.storageenginehashkey[x])
            # print(storageengine)
            self.dataframe_desc = ManualDesc(request = request, object2 = objecthashkey_target, dataframe_source = self.dataframe_desc).mainProcess()            

            if ((str(objecthashkey_source) and str(objecthashkey_target)) != 'nan'):
                addobjectprocess(request, objecthashkey_source, objecthashkey_target, df_input.processenginehashkey[x], df_input.usershashkey[x], sourcesystemcreatedby, sourcesystemcreatedtime)
                # engine_post.ObjectProcess(spark, str(objecthashkey_source),
                #                           str(objecthashkey_target),
                #                           str(df_input.processenginehashkey[x]),
                #                           str(df_input.usershashkey[x]))
        return list_objecthashkey_source

    def ConvertFloat(self, df):
        for i, j in zip(df.columns, df.dtypes):
            if 'float' in str(j):
                df[i] = df[i].apply(lambda x: '{:.0f}'.format(x))
        return df

    def Main(self, request, file_location):
        
        df_input = pd.read_excel("{}".format(file_location), sheet_name='object_relation')
        df_input = self.ConvertFloat(df_input)
        df_input = df_input.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        self.checkhashkey(request, df_input)
        # print(df_input)
        # self.InputObject(request, df_input)
        try:
            self.InputObject(request, df_input)
            status = 'Generate Success'
        except Exception as e:
            status = 'Generate Failed'
            problem = ""

        return status

