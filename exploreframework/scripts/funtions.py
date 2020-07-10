from django.db.models import Max
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, HttpResponse

from framework.models import *

from datetime import datetime
import json

### Process Object Single
def inputoneobject(request, object_instance, form):
    ## Cleasin Data
    if (str(form.cleaned_data['ownerhashkey']) != 'None') and (Owner.objects.filter(ownerhashkey=str(form.cleaned_data['ownerhashkey'])).exists() == False):
        messages.info(request, "Ownerhashkey doesn't Exist")
        return redirect("addoneobject")
    if (str(form.cleaned_data['storageenginehashkey']) != 'None') and (StorageEngine.objects.filter(storageenginehashkey=str(form.cleaned_data['storageenginehashkey'])).exists() == False):
        messages.info(request, "StorageEnginehashkey doesn't Exist")
        return redirect("addoneobject")
    if (str(form.cleaned_data['objecttypehashkey']) != 'None') and (ObjectType.objects.filter(objecttypehashkey=str(form.cleaned_data['objecttypehashkey'])).exists() == False):
        messages.info(request, "ObjectTypehashkey doesn't Exist")
        return redirect("addoneobject")
    if (str(form.cleaned_data['databasehashkey']) != 'None') and (Database.objects.filter(databasehashkey=str(form.cleaned_data['databasehashkey'])).exists() == False):
        messages.info(request, "Databasehashkey doesn't Exist")
        return redirect("addoneobject")
    if (str(form.cleaned_data['serverhashkey']) != 'None') and (Server.objects.filter(serverhashkey=str(form.cleaned_data['serverhashkey'])).exists() == False):
        messages.info(request, "Serverhashkey doesn't Exist")
        return redirect("addoneobject")
    if (str(form.cleaned_data['servertunnelhashkey']) != 'None') and (ServerTunnel.objects.filter(servertunnelhashkey=str(form.cleaned_data['servertunnelhashkey'])).exists() == False):
        messages.info(request, "ServerTunnelhashkey doesn't Exist")
        return redirect("addoneobject")
    if (str(form.cleaned_data['filehashkey']) != 'None') and (File.objects.filter(filehashkey=str(form.cleaned_data['filehashkey'])).exists() == False):
        messages.info(request, "Filehashkey doesn't Exist")
        return redirect("addoneobject")
    if (str(form.cleaned_data['objectpartitionhashkey']) != 'None') and (PartitionBy.objects.filter(objectpartitionhashkey=str(form.cleaned_data['objectpartitionhashkey'])).exists() == False):
        messages.info(request, "Partitionhashkey doesn't Exist")
        return redirect("addoneobject")
    if (str(form.cleaned_data['objectsnapshothashkey']) != 'None') and (SnapShot.objects.filter(objectsnapshothashkey=str(form.cleaned_data['objectsnapshothashkey'])).exists() == False):
        messages.info(request, "Snapshothashkey doesn't Exist")
        return redirect("addoneobject")
    if (str(form.cleaned_data['queryhashkey']) != 'None') and (Query.objects.filter(queryhashkey=str(form.cleaned_data['queryhashkey'])).exists() == False):
        messages.info(request, "Queryhashkey doesn't Exist")
        return redirect("addoneobject")
    
    ### Process Input
    print("process input heshkey")
    if (str(form.cleaned_data['ownerhashkey']) != 'None'):
        addobjectowner(request, object_instance, str(form.cleaned_data['ownerhashkey']), form.cleaned_data['sourcesystemcreatedby'], form.cleaned_data['sourcesystemcreatedtime'])
        messages.info(request, "Object Owner Hashkey Created")
    if (str(form.cleaned_data['storageenginehashkey']) != 'None'):
        addobjectstorageengine(request, object_instance, str(form.cleaned_data['storageenginehashkey']), form.cleaned_data['sourcesystemcreatedby'], form.cleaned_data['sourcesystemcreatedtime'])
        messages.info(request, "Object Storage Hashkey Created")
    if (str(form.cleaned_data['objecttypehashkey']) != 'None'):
        addobjectobjecttype(request, object_instance, str(form.cleaned_data['objecttypehashkey']), form.cleaned_data['sourcesystemcreatedby'], form.cleaned_data['sourcesystemcreatedtime'])
        messages.info(request, "Object Type Hashkey Created")
    if (str(form.cleaned_data['databasehashkey']) != 'None'):
        addobjectdatabase(request, object_instance, str(form.cleaned_data['databasehashkey']), form.cleaned_data['sourcesystemcreatedby'], form.cleaned_data['sourcesystemcreatedtime'])
        messages.info(request, "Object Database Hashkey Created")
    if (str(form.cleaned_data['serverhashkey']) != 'None'):
        addobjectserver(request, object_instance, str(form.cleaned_data['serverhashkey']), form.cleaned_data['sourcesystemcreatedby'], form.cleaned_data['sourcesystemcreatedtime'])
        messages.info(request, "Object Server Hashkey Created")
    if (str(form.cleaned_data['servertunnelhashkey']) != 'None'):
        addobjectservertunnel(request, object_instance, str(form.cleaned_data['servertunnelhashkey']), form.cleaned_data['sourcesystemcreatedby'], form.cleaned_data['sourcesystemcreatedtime'])
        messages.info(request, "Object ServerTunnel Hashkey Created")
    if (str(form.cleaned_data['filehashkey']) != 'None'):
        addobjectfile(request, object_instance, str(form.cleaned_data['filehashkey']), form.cleaned_data['sourcesystemcreatedby'], form.cleaned_data['sourcesystemcreatedtime'])
        messages.info(request, "Object File Hashkey Created")
    if (str(form.cleaned_data['objectpartitionhashkey']) != 'None'):
        addobjectobjectpartition(request, object_instance, str(form.cleaned_data['objectpartitionhashkey']), form.cleaned_data['sourcesystemcreatedby'], form.cleaned_data['sourcesystemcreatedtime'])
        messages.info(request, "Object Partition Hashkey Created")
    if (str(form.cleaned_data['objectsnapshothashkey']) != 'None'):
        addobjectobjectsnapshot(request, object_instance, str(form.cleaned_data['objectsnapshothashkey']), form.cleaned_data['sourcesystemcreatedby'], form.cleaned_data['sourcesystemcreatedtime'])
        messages.info(request, "ObjectSnapShot Hashkey Created")
    if (str(form.cleaned_data['queryhashkey']) != 'None'):
        addobjectquery(request, object_instance,str(form.cleaned_data['queryhashkey']), form.cleaned_data['sourcesystemcreatedby'], form.cleaned_data['sourcesystemcreatedtime'])
        messages.info(request, "Object Query Hashkey Created")


### Process Relation Object
def addobject(request, objectname, objectdesc, sourcesystemcreatedby, sourcesystemcreatedtime):
    maximum = Object.objects.all().aggregate(Max('objectcode'))['objectcode__max']
    if maximum == None:
        objectcode = "Obj00000001"
    else:
        objectcode = "Obj" + str(int(maximum.strip('Obj')) + 1).zfill(8)
    objecthashkey = str(objectcode) + str(objectname)
    inputdatabase = Object.objects.create(objecthashkey=objecthashkey, objectcode=objectcode, objectname=objectname, 
                                          objectdesc=objectdesc, sourcesystemcreatedby=sourcesystemcreatedby, 
                                          sourcesystemcreatedtime=sourcesystemcreatedtime)
    inputdatabase.save()
    messages.info(request, "Object {} Created".format(objecthashkey))

    return objecthashkey

def addobjectowner(request, objecthashkey, ownerhashkey, sourcesystemcreatedby, sourcesystemcreatedtime):
    objectownerhashkey = "{}{}".format(objecthashkey, ownerhashkey)
    ownerhashkey = Owner.objects.get(ownerhashkey=ownerhashkey)
    inputdatabase = ObjectOwner.objects.create(objectownerhashkey=objectownerhashkey, objecthashkey=objecthashkey, ownerhashkey=ownerhashkey, 
                                          sourcesystemcreatedby=sourcesystemcreatedby, sourcesystemcreatedtime=sourcesystemcreatedtime)
    inputdatabase.save()
    messages.info(request, "Object Owener {} Created".format(objecthashkey))

    return objectownerhashkey

def addobjectstorageengine(request, objecthashkey, storageenginehashkey, sourcesystemcreatedby, sourcesystemcreatedtime):
    objectstorageenginehashkey = "{}{}".format(objecthashkey, storageenginehashkey)
    storageenginehashkey = StorageEngine.objects.get(storageenginehashkey=storageenginehashkey)
    inputdatabase = ObjectStorageEngine.objects.create(objectstorageenginehashkey=objectstorageenginehashkey, objecthashkey=objecthashkey, storageenginehashkey=storageenginehashkey, 
                                          sourcesystemcreatedby=sourcesystemcreatedby, sourcesystemcreatedtime=sourcesystemcreatedtime)
    inputdatabase.save()
    messages.info(request, "Object Storage Engine {} Created".format(objecthashkey))

    return objectstorageenginehashkey

def addobjectobjecttype(request, objecthashkey, objecttypehashkey, sourcesystemcreatedby, sourcesystemcreatedtime):
    objectobjecttypehashkey = "{}{}".format(objecthashkey, objecttypehashkey)
    objecttypehashkey = ObjectType.objects.get(objecttypehashkey=objecttypehashkey)
    inputdatabase = ObjectObjectType.objects.create(objectobjecttypehashkey=objectobjecttypehashkey, objecthashkey=objecthashkey, objecttypehashkey=objecttypehashkey, 
                                          sourcesystemcreatedby=sourcesystemcreatedby, sourcesystemcreatedtime=sourcesystemcreatedtime)
    inputdatabase.save()
    messages.info(request, "Object ObjectType {} Created".format(objecthashkey))

    return objectobjecttypehashkey

def addobjectdatabase(request, objecthashkey, databasehashkey, sourcesystemcreatedby, sourcesystemcreatedtime):
    objectdatabasehashkey = "{}{}".format(objecthashkey, databasehashkey)
    databasehashkey = Database.objects.get(databasehashkey=databasehashkey)
    inputdatabase = ObjectDatabase.objects.create(objectdatabasehashkey=objectdatabasehashkey, objecthashkey=objecthashkey, databasehashkey=databasehashkey, 
                                          sourcesystemcreatedby=sourcesystemcreatedby, sourcesystemcreatedtime=sourcesystemcreatedtime)
    inputdatabase.save()
    messages.info(request, "Object Database {} Created".format(objecthashkey))

    return objectdatabasehashkey

def addobjectserver(request, objecthashkey, serverhashkey, sourcesystemcreatedby, sourcesystemcreatedtime):
    objectserverhashkey = "{}{}".format(objecthashkey, serverhashkey)
    serverhashkey = Server.objects.get(serverhashkey=serverhashkey)
    inputdatabase = ObjectServer.objects.create(objectserverhashkey=objectserverhashkey, objecthashkey=objecthashkey, serverhashkey=serverhashkey, 
                                          sourcesystemcreatedby=sourcesystemcreatedby, sourcesystemcreatedtime=sourcesystemcreatedtime)
    inputdatabase.save()
    messages.info(request, "Object Server {} Created".format(objecthashkey))

    return objectserverhashkey

def addobjectservertunnel(request, objecthashkey, servertunnelhashkey, sourcesystemcreatedby, sourcesystemcreatedtime):
    objectservertunnelhashkey = "{}{}".format(objecthashkey, servertunnelhashkey)
    servertunnelhashkey = ServerTunnel.objects.get(servertunnelhashkey=servertunnelhashkey)
    inputdatabase = ObjectServerTunnel.objects.create(objectservertunnelhashkey=objectservertunnelhashkey, objecthashkey=objecthashkey, servertunnelhashkey=servertunnelhashkey, 
                                          sourcesystemcreatedby=sourcesystemcreatedby, sourcesystemcreatedtime=sourcesystemcreatedtime)
    inputdatabase.save()
    messages.info(request, "Object Server Tunnel {} Created".format(objecthashkey))

    return objectservertunnelhashkey

def addobjectfile(request, objecthashkey, filehashkey, sourcesystemcreatedby, sourcesystemcreatedtime):
    objectfilehashkey = "{}{}".format(objecthashkey, filehashkey)
    filehashkey = File.objects.get(filehashkey=filehashkey)
    inputdatabase = ObjectFile.objects.create(objectfilehashkey=objectfilehashkey, objecthashkey=objecthashkey, filehashkey=filehashkey, 
                                          sourcesystemcreatedby=sourcesystemcreatedby, sourcesystemcreatedtime=sourcesystemcreatedtime)
    inputdatabase.save()
    messages.info(request, "Object File {} Created".format(objecthashkey))

    return objectfilehashkey

def addobjectobjectpartition(request, objecthashkey, objectpartitionhashkey, sourcesystemcreatedby, sourcesystemcreatedtime):
    objectobjectpartitionhashkey = "{}{}".format(objecthashkey, objectpartitionhashkey)
    objectpartitionhashkey = PartitionBy.objects.get(objectpartitionhashkey=objectpartitionhashkey)
    inputdatabase = ObjectObjectPartition.objects.create(objectobjectpartitionhashkey=objectobjectpartitionhashkey, objecthashkey=objecthashkey, objectpartitionhashkey=objectpartitionhashkey, 
                                          sourcesystemcreatedby=sourcesystemcreatedby, sourcesystemcreatedtime=sourcesystemcreatedtime)
    inputdatabase.save()
    messages.info(request, "Object ObjectPartition {} Created".format(objecthashkey))

    return objectobjectpartitionhashkey

def addobjectobjectsnapshot(request, objecthashkey, objectsnapshothashkey, sourcesystemcreatedby, sourcesystemcreatedtime):
    objectobjectsnapshothashkey = "{}{}".format(objecthashkey, objectsnapshothashkey)
    objectsnapshothashkey = SnapShot.objects.get(objectsnapshothashkey=objectsnapshothashkey)
    inputdatabase = ObjectObjectSnapShot.objects.create(objectobjectsnapshothashkey=objectobjectsnapshothashkey, objecthashkey=objecthashkey, objectsnapshothashkey=objectsnapshothashkey, 
                                          sourcesystemcreatedby=sourcesystemcreatedby, sourcesystemcreatedtime=sourcesystemcreatedtime)
    inputdatabase.save()
    messages.info(request, "Object ObjectObjectSnapshot {} Created".format(objecthashkey))

    return objectobjectsnapshothashkey

def addobjectquery(request, objecthashkey, queryhashkey, sourcesystemcreatedby, sourcesystemcreatedtime):
    objectqueryhashkey = "{}{}".format(objecthashkey, queryhashkey)
    queryhashkey = Query.objects.get(queryhashkey=queryhashkey)
    inputdatabase = ObjectQuery.objects.create(objectqueryhashkey=objectqueryhashkey, objecthashkey=objecthashkey, queryhashkey=queryhashkey, 
                                          sourcesystemcreatedby=sourcesystemcreatedby, sourcesystemcreatedtime=sourcesystemcreatedtime)
    inputdatabase.save()
    messages.info(request, "Object Query {} Created".format(objecthashkey))

    return objectqueryhashkey

def addobjectprocess(request, src_objecthashkey, dest_objecthashkey, processenginehashkey, userhashkey, sourcesystemcreatedby, sourcesystemcreatedtime):
    objectprocesshashkey = "{}{}{}".format(src_objecthashkey,dest_objecthashkey,processenginehashkey)
    src_objecthashkey = Object.objects.get(objecthashkey=src_objecthashkey)
    dest_objecthashkey = Object.objects.get(objecthashkey=dest_objecthashkey)
    processenginehashkey = ProcessEngine.objects.get(processenginehashkey=processenginehashkey)
    userhashkey = ObjectUser.objects.get(userhashkey=userhashkey)
    inputdatabase = ObjectProcess.objects.create(objectprocesshashkey=objectprocesshashkey, src_objecthashkey=src_objecthashkey, dest_objecthashkey=dest_objecthashkey, 
                                          userhashkey=userhashkey, processenginehashkey=processenginehashkey,sourcesystemcreatedby=sourcesystemcreatedby, sourcesystemcreatedtime=sourcesystemcreatedtime)
    inputdatabase.save()
    messages.info(request, "Object Process {} Created".format(objectprocesshashkey))

    return objectprocesshashkey
