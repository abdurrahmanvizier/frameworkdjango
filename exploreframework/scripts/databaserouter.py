from framework.models import *

ROUTED_MODELS = [
    Object, ObjectDatabase, CreateObject, ObjectDesc, ObjectFile, ObjectObjectPartition,
    ObjectObjectSnapShot, ObjectObjectType, ObjectOwner, ObjectProcess,
    ObjectProcessLog, ObjectProcessObjectSnapShotLog, ObjectQuery, ObjectServer,
    ObjectServerTunnel, ObjectStorageEngine, ObjectType, ObjectUser, Owner, 
    StorageEngine, Database, PartitionBy, File, Server, ServerTunnel, SnapShot, Query,
    Process, ProcessEngine, Engine, MultipleRelation
]


class MyDBRouter(object):

    def db_for_read(self, model, **hints):
        if model in ROUTED_MODELS:
            return 'explore'
        return None

    def db_for_write(self, model, **hints):
        if model in ROUTED_MODELS:
            return 'explore'
        return None