from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from scripts import multipleobjectform
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    path('deleteall/', views.deleteall, name='deleteall'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('frameworklist/', views.frameworklist, name='listframework'),
    path('frameworkinput/', views.frameworkinput, name='inputframework'),
    path('multipleframeworkinput/', multipleobjectform.CreateObjectView.as_view(), name='multipleframeworkinput'),
    path('multipleframeworkinput/checkmultiple/', views.checkmultiple, name='checkmultiple'),
    path('multipleframeworkupdate/', multipleobjectform.UpdateObjectView.as_view(), name='multipleframeworkupdate'),

    path('database/', views.database, name='database'),
    path('database/adddatabase/', views.createDatabase, name='adddatabase'),
    path('database/update_database/<str:pk>/', views.updateDatabase, name="update_database"),

    path('owner/', views.owner, name='owner'),
    path('owner/addowner/', views.createOwner, name='addowner'),
    path('owner/update_owner/<str:pk>/', views.updateOwner, name="update_owner"),

    path('storageengine/', views.storageengine, name='storageengine'),
    path('storageengine/addstorageengine/', views.createStorageEngine, name='addstorageengine'),
    path('storageengine/update_storageengine/<str:pk>/', views.updateStorageEngine, name="update_storageengine"),

    path('objecttype/', views.objecttype, name='objecttype'),
    path('objecttype/addobjecttype/', views.createObjectType, name='addobjecttype'),
    path('objecttype/update_objecttype/<str:pk>/', views.updateObjectType, name="update_objecttype"),

    path('partition/', views.partition, name='partition'),
    path('partition/addpartition/', views.createPartitionBy, name='addpartition'),
    path('partition/update_partition/<str:pk>/', views.updatePartitionBy, name="update_partition"),

    path('snapshot/', views.snapshot, name='snapshot'),
    path('snapshot/addsnapshot/', views.createSnapShot, name='addsnapshot'),
    path('snapshot/update_snapshot/<str:pk>/', views.updateSnapShot, name="update_snapshot"),

    path('server/', views.server, name='server'),
    path('server/addserver/', views.createServer, name='addserver'),
    path('server/update_server/<str:pk>/', views.updateServer, name="update_server"),

    path('servertunnel/', views.servertunnel, name='servertunnel'),
    path('servertunnel/addservertunnel/', views.createServerTunnel, name='addservertunnel'),
    path('servertunnel/update_servertunnel/<str:pk>/', views.updateServerTunnel, name="update_servertunnel"),

    path('file/', views.files, name='files'),
    path('file/addfile/', views.createFile, name='addfile'),
    path('file/update_file/<str:pk>/', views.updateFile, name="update_file"),

    path('query/', views.query, name='query'),
    path('query/addquery/', views.createQuery, name='addquery'),
    path('query/update_query/<str:pk>/', views.updateQuery, name="update_query"),

    path('user/', views.user, name='user'),
    path('user/adduser/', views.createUser, name='adduser'),
    path('user/update_user/<str:pk>/', views.updateUser, name="update_user"),

    path('process/', views.process, name='process'),
    path('process/addprocess/', views.createProcess, name='addprocess'),
    path('process/update_process/<str:pk>/', views.updateProcess, name="update_process"),

    path('engine/', views.engine, name='engine'),
    path('engine/addengine/', views.createEngine, name='addengine'),
    path('engine/update_engine/<str:pk>/', views.updateEngine, name="update_engine"),

    path('processengine/', views.processengine, name='processengine'),
    path('processengine/addprocessengine/', views.createProcessEngine, name='addprocessengine'),
    path('processengine/update_processengine/<str:pk>/', views.updateProcessEngine, name="update_processengine"),

    path('object/', views.objects, name='object'),
    path('object/addoneobject/', views.createOneObject, name='addoneobject'),
    path('object/addoneobject/oneobject/', views.createOneObject, name='oneobject'),
    path('object/addmultiobject/', views.createProcessEngine, name='addmultiobject'),
    path('object/delete_object/<str:pk>/', views.updateProcessEngine, name="delete_object"),

    path('objectsprocessrelation/', views.objectsprocessrelation, name='objectsprocessrelation'),
    path('objectsprocessrelation/addoneobjectsprocessrelation/', views.createObjectProcessRelation, name='addoneobjectsprocessrelation'),
    path('objectsprocessrelation/update_objectsprocessrelation/<str:pk>/', views.updateObjectProcessRelation, name='update_objectsprocessrelation'),

    path('multiplerelation/', views.multiplerelation, name='multiplerelation'),
    path('multiplerelation/addmultiplerelation/', views.createMultipleRelation, name='addmultiplerelation'),
    path('multiplerelation/generate_multiplerelation/<str:pk>/', views.generateMultipleRelation, name="generate_mutiplerelation"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)