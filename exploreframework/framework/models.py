
from django import forms
from django.db import models
from django.db.models import Max
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

from django_pandas.managers import DataFrameManager

from datetime import datetime
from scripts.validators import validate_file_extension

# Create your models here.

class Database(models.Model):
    databasehashkey = models.TextField(primary_key = True, verbose_name = "Database Hashkey")
    applicationname = models.CharField(max_length=200, null=True, verbose_name = "Application Name")
    databasename = models.CharField(max_length=200, null=True, verbose_name = "Database Name")
    hostname = models.CharField(max_length=200, null=True, verbose_name = "Hostname")
    databasetype = models.CharField(max_length=200, null=True, verbose_name = "Database Type")
    port = models.CharField(max_length=200, null=True, verbose_name = "Port")
    username = models.CharField(max_length=200, null=True, verbose_name = "Username")
    password = models.CharField(max_length=200, null=True, verbose_name = "Password")
    sourcesystemcreatedby = models.CharField(max_length=200, null=True)
    sourcesystemcreatedtime = models.CharField(max_length=200, null=True)

    class Meta:
        managed = True
        db_table = 'database'

    def __str__(self):
        return self.databasehashkey

    def validate_data(self, *args, **kwargs):
        self.databasehashkey = "{}{}".format(self.applicationname, self.databasename)
        self.sourcesystemcreatedtime = datetime.now()

        ## check
        # matching_ = Databases.objects.filter(databasehashkey=self.databasehashkey)
        if Database.objects.filter(databasehashkey=self.databasehashkey).exists():
            # raise forms.ValidationError("Databasehashkey Already Exist")
            return "Databasehashkey Already Exist"
    
    def save(self, *args, **kwargs):
        self.databasehashkey = "{}{}".format(self.applicationname, self.databasename)
        self.sourcesystemcreatedtime = datetime.now()
        # self.validate_data()
        ### create hash in password
        # self.password = make_password(self.password)

        super(Database,self).save(*args,**kwargs)

    def delete_everything(self):
        Database.objects.all().delete()

class Engine(models.Model):
    enginehashkey = models.TextField(primary_key = True, verbose_name = "EngineHashkey")
    enginename = models.TextField(verbose_name = "Engine Name")
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def validate_data(self, *args, **kwargs):
        self.sourcesystemcreatedtime = datetime.now()

        ## check
        # matching_ = Databases.objects.filter(databasehashkey=self.databasehashkey)
        if Engine.objects.filter(enginename=self.enginename).exists():
            # raise forms.ValidationError("Databasehashkey Already Exist")
            return "Databasehashkey Already Exist"
    
    def save(self, *args, **kwargs):
        self.enginehashkey = "{}".format(self.enginename)
        self.sourcesystemcreatedtime = datetime.now()
        # self.validate_data()
        ### create hash in password
        # self.password = make_password(self.password)

        super(Engine,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.enginehashkey
    
    def delete_everything(self):
        Engine.objects.all().delete()
    
    class Meta:
        managed = True
        db_table = 'engine'

class File(models.Model):
    filehashkey = models.TextField(primary_key = True, verbose_name = "FileHashKey")
    filename = models.TextField(verbose_name = "File Name")
    location = models.TextField(verbose_name = "Location Server")
    delimiter = models.TextField(verbose_name = "delimiter")
    path = models.TextField(verbose_name = "Path")
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def __str__(self):
        return self.filehashkey
   
    def save(self, *args, **kwargs):
        self.filehashkey = "{}{}".format(self.filename, self.location)
        self.sourcesystemcreatedtime = datetime.now()
        # self.validate_data()
        ### create hash in password
        # self.password = make_password(self.password)

        super(File,self).save(*args,**kwargs)
    
    def delete_everything(self):
        File.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'file'

class ObjectType(models.Model):
    objecttypehashkey = models.TextField(primary_key = True, verbose_name = "Object Type Hashkey")
    objecttype = models.TextField(verbose_name = "Object Type")
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def __str__(self):
        return self.objecttypehashkey
    
    def save(self, *args, **kwargs):
        self.objecttypehashkey = "{}".format(self.objecttype)
        self.sourcesystemcreatedtime = datetime.now()
        # self.validate_data()
        ### create hash in password
        # self.password = make_password(self.password)

        super(ObjectType,self).save(*args,**kwargs)
    
    def delete_everything(self):
        ObjectType.objects.all().delete()
    
    class Meta:
        managed = True
        db_table = 'objecttype'

class StorageEngine(models.Model):
    storageenginehashkey = models.TextField(primary_key = True, verbose_name = "StorageEngineHashkey")
    storageenginetype = models.TextField(verbose_name = "Storage Engine Type")
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def __str__(self):
        return self.storageenginehashkey
    
    def save(self, *args, **kwargs):
        self.storageenginehashkey = "{}".format(self.storageenginetype)
        self.sourcesystemcreatedtime = datetime.now()
        # self.validate_data()
        ### create hash in password
        # self.password = make_password(self.password)

        super(StorageEngine,self).save(*args,**kwargs)

    def delete_everything(self):
        StorageEngine.objects.all().delete()
    
    class Meta:
        managed = True
        db_table = 'storageengine'

class Owner(models.Model):
    ownerhashkey = models.TextField(primary_key = True, verbose_name = "OwnerHashKey")
    ownername = models.TextField(verbose_name = "Owner Name")
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def __str__(self):
        return self.ownerhashkey

    def validate_data(self, *args, **kwargs):
        self.ownerhashkey = "{}".format(self.ownername)
        self.sourcesystemcreatedtime = datetime.now()

        ## check
        # matching_ = Databases.objects.filter(databasehashkey=self.databasehashkey)
        if Owner.objects.filter(ownerhashkey=self.ownerhashkey).exists():
            # raise forms.ValidationError("Databasehashkey Already Exist")
            return "Ownerhashkey Already Exist"
    
    def save(self, *args, **kwargs):
        self.ownerhashkey = "{}".format(self.ownername)
        self.sourcesystemcreatedtime = datetime.now()
        # self.validate_data()
        ### create hash in password
        # self.password = make_password(self.password)

        super(Owner,self).save(*args,**kwargs)

    def delete_everything(self):
        Owner.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'owner'

class PartitionBy(models.Model):
    objectpartitionhashkey = models.TextField(primary_key = True, verbose_name = "Partition By HashKey")
    partitionby = models.TextField(verbose_name = "Partition By")
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def __str__(self):
        return self.objectpartitionhashkey
    
    def save(self, *args, **kwargs):
        maximum = PartitionBy.objects.all().aggregate(Max('objectpartitionhashkey'))['objectpartitionhashkey__max']
        if maximum == None:
            self.objectpartitionhashkey = "Par00001"
        else:
            self.objectpartitionhashkey = "Par" + str(int(maximum.strip('Par')) + 1).zfill(5)
        
        self.sourcesystemcreatedtime = datetime.now()
        # self.validate_data()
        ### create hash in password
        # self.password = make_password(self.password)

        super(PartitionBy,self).save(*args,**kwargs)

    def delete_everything(self):
        PartitionBy.objects.all().delete()
    
    class Meta:
        managed = True
        db_table = 'objectpartition'

class Process(models.Model):
    processhashkey = models.TextField(primary_key = True, verbose_name = "ProcesHashkey")
    processcode = models.TextField(verbose_name = "Process Code")
    processdesc = models.TextField(verbose_name = "Process Description")
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def __str__(self):
        return self.processhashkey

    def validate_data(self, *args, **kwargs):
        ## check
        # matching_ = Databases.objects.filter(databasehashkey=self.databasehashkey)
        if Process.objects.filter(processdesc=self.processdesc).exists():
            # raise forms.ValidationError("Databasehashkey Already Exist")
            return "Ownerhashkey Already Exist"
    
    def save(self, *args, **kwargs):
        maximum = Process.objects.all().aggregate(Max('processcode'))['processcode__max']
        if maximum == None:
            self.processcode = "Pcs00001"
        else:
            self.processcode = "Pcs" + str(int(maximum.strip('Pcs')) + 1).zfill(5)
        self.processhashkey = self.processcode
        self.sourcesystemcreatedtime = datetime.now()
        # self.validate_data()
        ### create hash in password
        # self.password = make_password(self.password)

        super(Process,self).save(*args,**kwargs)
    
    def delete_everything(self):
        Process.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'process'

class SnapShot(models.Model):
    objectsnapshothashkey = models.TextField(primary_key = True, verbose_name = "Object SnapShot HashKey")
    snapshot1 = models.TextField(verbose_name = "SnapShot 1")
    snapshot2 = models.TextField(verbose_name = "SnapShot 2")
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def __str__(self):
        return self.objectsnapshothashkey

    def save(self, *args, **kwargs):
        maximum = SnapShot.objects.all().aggregate(Max('objectsnapshothashkey'))['objectsnapshothashkey__max']
        if maximum == None:
            self.objectsnapshothashkey = "Snap00001"
        else:
            self.objectsnapshothashkey = "Snap" + str(int(maximum.strip('Snap')) + 1).zfill(5)
        # self.enginehashkey = "{}".format(self.enginename)
        self.sourcesystemcreatedtime = datetime.now()
        # self.validate_data()
        ### create hash in password
        # self.password = make_password(self.password)

        super(SnapShot,self).save(*args,**kwargs)
    
    def delete_everything(self):
        SnapShot.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'objectsnapshot'

class Server(models.Model):
    serverhashkey = models.TextField(primary_key = True, verbose_name = "Server HashKey")
    servername = models.TextField(verbose_name = "Server Name")
    hostname = models.TextField(verbose_name = "Hostname")
    user = models.TextField(verbose_name = "Username")
    password = models.TextField(verbose_name = "Password")
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def __str__(self):
        return self.serverhashkey

    def save(self, *args, **kwargs):
        self.serverhashkey = "{}".format(self.servername)
        self.sourcesystemcreatedtime = datetime.now()
        # self.validate_data()
        ### create hash in password
        # self.password = make_password(self.password)

        super(Server,self).save(*args,**kwargs)
    
    def delete_everything(self):
        Server.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'server'

class ServerTunnel(models.Model):
    servertunnelhashkey = models.TextField(primary_key = True, verbose_name = "Server Tunnel HashKey")
    servertunnelname = models.TextField(verbose_name = "Server Name")
    hostname = models.TextField(verbose_name = "Hostname")
    port = models.TextField(verbose_name = "Port")
    user = models.TextField(verbose_name = "Username")
    password = models.TextField(verbose_name = "Password")
    private_key_user = models.TextField(verbose_name = "Private Key User")
    private_key_password = models.TextField(verbose_name = "Private Key Password")
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def __str__(self):
        return self.servertunnelhashkey

    def save(self, *args, **kwargs):
        self.servertunnelhashkey = "{}".format(self.servertunnelname)
        self.sourcesystemcreatedtime = datetime.now()

        super(ServerTunnel,self).save(*args,**kwargs)
    
    def delete_everything(self):
        ServerTunnel.objects.all().delete()
    
    class Meta:
        managed = True
        db_table = 'servertunnel'

class Query(models.Model):
    queryhashkey = models.TextField(primary_key = True, verbose_name = "Query HashKey")
    name = models.TextField(verbose_name = "Query Name")
    path = models.TextField(verbose_name = "Path")
    desc = models.TextField(verbose_name = "Description")
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def __str__(self):
        return self.queryhashkey

    def save(self, *args, **kwargs):
        self.queryhashkey = "{}".format(self.name)
        self.sourcesystemcreatedtime = datetime.now()
        # self.validate_data()
        ### create hash in password
        # self.password = make_password(self.password)

        super(Query,self).save(*args,**kwargs)
    
    def delete_everything(self):
        Query.objects.all().delete()
    
    class Meta:
        managed = True
        db_table = 'query'

class ProcessEngine(models.Model):
    processenginehashkey = models.TextField(primary_key = True, verbose_name = "ProcesEngineHashkey")
    processhashkey = models.ForeignKey(Process, verbose_name = "ProcesHashkey", null=True, on_delete= models.SET_NULL)
    enginehashkey = models.ForeignKey(Engine, verbose_name = "EngineHashkey", null=True, on_delete= models.SET_NULL)
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def __str__(self):
        return self.processenginehashkey

    def validate_data(self, *args, **kwargs):
        ## check
        # matching_ = Databases.objects.filter(databasehashkey=self.databasehashkey)
        if ProcessEngine.objects.filter(processenginehashkey=self.processenginehashkey).exists():
            # raise forms.ValidationError("Databasehashkey Already Exist")
            return "Process Engine Already Exist"
    
    def save(self, *args, **kwargs):
        self.processenginehashkey = "{}{}".format(self.processhashkey,self.enginehashkey)
        self.sourcesystemcreatedtime = datetime.now()
        # self.validate_data()
        ### create hash in password
        # self.password = make_password(self.password)

        super(ProcessEngine,self).save(*args,**kwargs)
    
    def delete_everything(self):
        ProcessEngine.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'processengine'

class ObjectUser(models.Model):
    userhashkey = models.TextField(primary_key = True, verbose_name = "UserHashkey")
    username = models.TextField(verbose_name = "Username")
    resourcepool = models.TextField(verbose_name = "ResourcePool")
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def __str__(self):
        return self.userhashkey

    def validate_data(self, *args, **kwargs):
        self.userhashkey = "{}".format(self.username)
        self.sourcesystemcreatedtime = datetime.now()

        ## check
        # matching_ = Databases.objects.filter(databasehashkey=self.databasehashkey)
        if ObjectUser.objects.filter(ownerhashkey=self.userhashkey).exists():
            # raise forms.ValidationError("Databasehashkey Already Exist")
            return "Userhashkey Already Exist"
    
    def save(self, *args, **kwargs):
        self.userhashkey = "{}{}".format(self.username, self.resourcepool)
        self.sourcesystemcreatedtime = datetime.now()
        # self.validate_data()
        ### create hash in password
        # self.password = make_password(self.password)

        super(ObjectUser,self).save(*args,**kwargs)
    
    def delete_everything(self):
        ObjectUser.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'objectuser'


### Intial For Object
class Object(models.Model):
    objecthashkey = models.TextField(primary_key = True, verbose_name = "Object HashKey")
    objectcode = models.TextField(verbose_name = "Object Code")
    objectname = models.TextField(verbose_name = "Object Name")
    objectdesc = models.TextField(verbose_name = "Object Descriptions")
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def __str__(self):
        return self.objecthashkey
    
    def delete_everything(self):
        Object.objects.all().delete()
    
    class Meta:
        managed = True
        db_table = 'object'

class ObjectDatabase(models.Model):
    objectdatabasehashkey = models.TextField(primary_key = True, verbose_name = "Object DatabaseHashkey")
    objecthashkey = models.ForeignKey(Object, verbose_name = "ObjectHashkey", null=True, on_delete= models.SET_NULL)
    databasehashkey = models.ForeignKey(Database, verbose_name = "DatabaseHashkey", null=True, on_delete= models.SET_NULL)
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def delete_everything(self):
        ObjectDatabase.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'objectdatabase'

class ObjectProcess(models.Model):
    objectprocesshashkey = models.TextField(primary_key = True, verbose_name = "Object ProcessHashkey")
    src_objecthashkey = models.ForeignKey(Object, verbose_name = "Source ObjectHashkey", null=True, on_delete= models.SET_NULL, related_name='src_objecthashkey')
    dest_objecthashkey = models.ForeignKey(Object, verbose_name = "Destination ObjectHashkey", null=True, on_delete= models.SET_NULL, related_name='dest_objecthashkey')
    processenginehashkey = models.ForeignKey(ProcessEngine, verbose_name = "Proces Engine Hashkey", null=True, on_delete= models.SET_NULL)
    userhashkey = models.ForeignKey(ObjectUser, verbose_name = "UserHashkey", null=True, on_delete= models.SET_NULL)
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def save(self, *args, **kwargs):
        self.objectprocesshashkey = "{}{}{}".format(self.src_objecthashkey, self.dest_objecthashkey, self.processenginehashkey)
        self.sourcesystemcreatedtime = datetime.now()
        # self.validate_data()
        ### create hash in password
        # self.password = make_password(self.password)

        super(ObjectProcess,self).save(*args,**kwargs)
    
    def delete_everything(self):
        ObjectProcess.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'objectprocess'

class ObjectOwner(models.Model):
    objectownerhashkey = models.TextField(primary_key = True, verbose_name = "Object Owner Hashkey")
    objecthashkey = models.ForeignKey(Object, verbose_name = "Object HashKey", null=True, on_delete= models.SET_NULL)
    ownerhashkey = models.ForeignKey(Owner, verbose_name = "Owner Hash Key", null=True, on_delete= models.SET_NULL)
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def delete_everything(self):
        ObjectOwner.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'objectowner'

class ObjectDesc(models.Model):
    objectdeschashkey = models.TextField(primary_key = True, verbose_name = "Object Desc Hashkey")
    objecthashkey = models.ForeignKey(Object, verbose_name = "ObjectHashkey", null=True, on_delete= models.SET_NULL, related_name='objecthashkey_id')
    deschashkey = models.TextField(verbose_name = "Column Name")
    datatype = models.TextField(verbose_name = "Column Type")
    length = models.TextField(verbose_name = "Length", null=True)
    nullable = models.TextField(verbose_name = "Nullabel", null=True)
    primary = models.TextField(verbose_name = "Primary", null=True)
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def delete_everything(self):
        ObjectDesc.objects.all().delete()
    
    class Meta:
        managed = True
        db_table = 'objectdesc'

class ObjectFile(models.Model):
    objectfilehashkey = models.TextField(primary_key = True, verbose_name = "Object File Hashkey")
    objecthashkey = models.ForeignKey(Object, verbose_name = "ObjectHashkey", null=True, on_delete= models.SET_NULL)
    filehashkey = models.ForeignKey(File, verbose_name = "File HashKey", null=True, on_delete= models.SET_NULL)
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def delete_everything(self):
        ObjectFile.objects.all().delete()
    
    class Meta:
        managed = True
        db_table = 'objectfile'

class ObjectObjectPartition(models.Model):
    objectobjectpartitionhashkey = models.TextField(primary_key = True, verbose_name = "Object Partition")
    objecthashkey = models.ForeignKey(Object, verbose_name = "ObjectHashkey", null=True, on_delete= models.SET_NULL)
    objectpartitionhashkey = models.ForeignKey(PartitionBy, verbose_name = "Partition Hashkey", null=True, on_delete= models.SET_NULL)
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def delete_everything(self):
        ObjectObjectPartition.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'objectobjectpartition'

class ObjectObjectSnapShot(models.Model):
    objectobjectsnapshothashkey = models.TextField(primary_key = True, verbose_name = "Object Snapshot")
    objecthashkey = models.ForeignKey(Object, verbose_name = "ObjectHashkey", null=True, on_delete= models.SET_NULL)
    objectsnapshothashkey = models.ForeignKey(SnapShot, verbose_name = "SnapShot Hashkey", null=True, on_delete= models.SET_NULL)
    snapshot1value = models.TextField(verbose_name = "Snapshot 1 Value")
    snapshot2value = models.TextField(verbose_name = "Snapshot 2 Value")
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def delete_everything(self):
        ObjectObjectSnapShot.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'objectobjectsnapshot'

class ObjectObjectType(models.Model):
    objectobjecttypehashkey = models.TextField(primary_key = True, verbose_name = "Object Object Type")
    objecthashkey = models.ForeignKey(Object, verbose_name = "ObjectHashkey", null=True, on_delete= models.SET_NULL)
    objecttypehashkey = models.ForeignKey(ObjectType, verbose_name = "Object Type Hashkey", null=True, on_delete= models.SET_NULL)
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def delete_everything(self):
        ObjectObjectType.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'objectobjecttype'

class ObjectProcessLog(models.Model):
    objectprocessloghashkey = models.TextField(primary_key = True, verbose_name = "Object Process Log")
    objectprocesshashkey = models.TextField(verbose_name = "ObjectProcessHashkey")
    logcode = models.TextField(verbose_name = "Log Code")
    starttime = models.TextField(verbose_name = "Start Time")
    finishtime = models.TextField(verbose_name = "Finish Time")
    processtime = models.TextField(verbose_name = "Process Time")
    status = models.TextField(verbose_name = "Status Process")
    location = models.TextField(verbose_name = "Location Process")
    rowcountsource = models.TextField(verbose_name = "Row Count Source")
    rowcounttarget = models.TextField(verbose_name = "Row Count Target")
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def delete_everything(self):
        ObjectProcessLog.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'objectprocesslog'

class ObjectProcessObjectSnapShotLog(models.Model):
    objectprocessobjectsnapshotloghashkey = models.TextField(primary_key = True)
    objectprocessloghashkey = models.TextField(verbose_name = "ObjectProcessLogHashkey")
    objectobjectsnapshothashkey = models.TextField(verbose_name = "ObjectSnapShot")
    snapshot1value = models.TextField(verbose_name = "SnapShot Value 1")
    snapshot2value = models.TextField(verbose_name = "SnapShot Value 2")
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def delete_everything(self):
        ObjectProcessObjectSnapShotLog.objects.all().delete()
    
    class Meta:
        managed = True
        db_table = 'objectprocessobjectsnapshotlog'

class ObjectQuery(models.Model):
    objectqueryhashkey = models.TextField(primary_key = True, verbose_name = "Object Query HashKey")
    objecthashkey = models.ForeignKey(Object, verbose_name = "Object Hash Key", null=True, on_delete= models.SET_NULL)
    queryhashkey = models.ForeignKey(Query, verbose_name = "Query HashKey", null=True, on_delete= models.SET_NULL)
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def delete_everything(self):
        ObjectQuery.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'objectquery'

class ObjectServer(models.Model):
    objectserverhashkey = models.TextField(primary_key = True, verbose_name = "Object Server HashKey")
    objecthashkey = models.ForeignKey(Object, verbose_name = "Object Hash Key", null=True, on_delete= models.SET_NULL)
    serverhashkey = models.ForeignKey(Server, verbose_name = "Server HashKey", null=True, on_delete= models.SET_NULL)
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def delete_everything(self):
        ObjectServer.objects.all().delete()
    
    class Meta:
        managed = True
        db_table = 'objectserver'

class ObjectServerTunnel(models.Model):
    objectservertunnelhashkey = models.TextField(primary_key = True, verbose_name = "Object Server Tunnel HashKey")
    objecthashkey = models.ForeignKey(Object, verbose_name = "Object Hash Key", null=True, on_delete= models.SET_NULL)
    servertunnelhashkey = models.ForeignKey(ServerTunnel, verbose_name = "Server Tunnel HashKey", null=True, on_delete= models.SET_NULL)
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def delete_everything(self):
        ObjectServerTunnel.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'objectservertunnel'

class ObjectStorageEngine(models.Model):
    objectstorageenginehashkey = models.TextField(primary_key = True, verbose_name = "Object Storage Engine HashKey")
    objecthashkey = models.ForeignKey(Object, verbose_name = "Object Hash Key", null=True, on_delete= models.SET_NULL)
    storageenginehashkey = models.ForeignKey(StorageEngine, verbose_name = "Storage Engine HashKey", null=True, on_delete= models.SET_NULL)
    sourcesystemcreatedby = models.TextField()
    sourcesystemcreatedtime = models.TextField()

    def delete_everything(self):
        ObjectStorageEngine.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'objectstorageengine'

class MultipleRelation(models.Model):
    filename = models.CharField(default="", max_length=100)
    filepath = models.CharField(default="", max_length=100)
    createdby = models.CharField(max_length=100)
    createdat = models.DateTimeField(auto_now=True)
    status = models.CharField(default="", max_length=30)
    excel = models.FileField(upload_to='objectrelation/multiple/', validators=[validate_file_extension])

    def __str__(self):
        return self.createdby
    
    def delete_everything(self):
        MultipleRelation.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'multiplerelation'

class CreateObject(models.Model):
    objecthashkey = models.ForeignKey(Object, null=True, on_delete= models.SET_NULL)
    objectname = models.CharField(max_length=50, verbose_name = "Object Name")
    objectdesc = models.CharField(max_length=255, verbose_name = "objectdesc")
    ownerhashkey = models.ForeignKey(Owner, null=True, on_delete= models.SET_NULL)
    storageenginehashkey = models.ForeignKey(StorageEngine, null=True, on_delete= models.SET_NULL)
    objecttypehashkey = models.ForeignKey(ObjectType, null=True, on_delete= models.SET_NULL)
    databasehashkey = models.ForeignKey(Database, null=True, on_delete= models.SET_NULL)
    serverhashkey = models.ForeignKey(Server, null=True, on_delete= models.SET_NULL)
    servertunnelhashkey = models.ForeignKey(ServerTunnel, null=True, on_delete= models.SET_NULL)
    filehashkey = models.ForeignKey(File, null=True, on_delete= models.SET_NULL)
    objectpartitionhashkey = models.ForeignKey(PartitionBy, null=True, on_delete= models.SET_NULL)
    objectsnapshothashkey = models.ForeignKey(SnapShot, null=True, on_delete= models.SET_NULL)
    queryhashkey = models.ForeignKey(Query, null=True, on_delete= models.SET_NULL)
    objectdeschash = models.CharField(max_length=50, verbose_name = "ObjectDesc Hashkey", default='No ObjectDesc')
    sourcesystemcreatedby = models.TextField(default='Testing', null=False)
    sourcesystemcreatedtime = models.TextField()

    def delete_everything(self):
        CreateObject.objects.all().delete()

    class Meta:
        managed = True
        db_table = 'createobject'

