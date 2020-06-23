import django_filters

from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from crispy_forms.helper import FormHelper

from django_filters import CharFilter
from django import forms
from .models import *


class OwnerFilter(django_filters.FilterSet):
    ownername = CharFilter(label='Owner Name', field_name='ownername', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedby = CharFilter(label='Created By', field_name='sourcesystemcreatedby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedtime = CharFilter(label='Created At', field_name='sourcesystemcreatedtime', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Owner
        fields = '__all__'

        exclude = ('ownerhashkey')
    
    def __init__(self, *args, **kwargs):
        super(OwnerFilter, self).__init__(*args, **kwargs)


class UserFilter(django_filters.FilterSet):
    username = CharFilter(label='User Name', field_name='username', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    resourcepool = CharFilter(label='Resource Pool', field_name='resourcepool', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedby = CharFilter(label='Created By', field_name='sourcesystemcreatedby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedtime = CharFilter(label='Created At', field_name='sourcesystemcreatedtime', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = ObjectUser
        fields = '__all__'

        exclude = ('userhashkey')
    
    def __init__(self, *args, **kwargs):
        super(UserFilter, self).__init__(*args, **kwargs)


class StorageEngineFilter(django_filters.FilterSet):
    storageenginetype = CharFilter(label='Storage Engine Name', field_name='storageenginetype', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedby = CharFilter(label='Created By', field_name='sourcesystemcreatedby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedtime = CharFilter(label='Created At', field_name='sourcesystemcreatedtime', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = StorageEngine
        fields = '__all__'

        exclude = ('storageenginehashkey')
    
    def __init__(self, *args, **kwargs):
        super(StorageEngineFilter, self).__init__(*args, **kwargs)


class ObjectTypeFilter(django_filters.FilterSet):
    objecttype = CharFilter(label='Object Type', field_name='objecttype', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedby = CharFilter(label='Created By', field_name='sourcesystemcreatedby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedtime = CharFilter(label='Created At', field_name='sourcesystemcreatedtime', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = ObjectType
        fields = '__all__'

        exclude = ('objecttypehashkey')
    
    def __init__(self, *args, **kwargs):
        super(ObjectTypeFilter, self).__init__(*args, **kwargs)


class PartitionByFilter(django_filters.FilterSet):
    partitionby = CharFilter(label='Partition By', field_name='partitionby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedby = CharFilter(label='Created By', field_name='sourcesystemcreatedby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedtime = CharFilter(label='Created At', field_name='sourcesystemcreatedtime', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = PartitionBy
        fields = '__all__'

        exclude = ('objectpartitionhashkey')
    
    def __init__(self, *args, **kwargs):
        super(PartitionByFilter, self).__init__(*args, **kwargs)


class SnapShotFilter(django_filters.FilterSet):
    snapshot1 = CharFilter(label='Snapshot 1', field_name='snapshot1', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    snapshot2 = CharFilter(label='Snapshot 2', field_name='snapshot2', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedby = CharFilter(label='Created By', field_name='sourcesystemcreatedby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedtime = CharFilter(label='Created At', field_name='sourcesystemcreatedtime', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = SnapShot
        fields = '__all__'

        exclude = ('objectsnapshothashkey')
    
    def __init__(self, *args, **kwargs):
        super(SnapShotFilter, self).__init__(*args, **kwargs)


class ServerFilter(django_filters.FilterSet):
    servername = CharFilter(label='Server Name', field_name='servername', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    hostname = CharFilter(label='Hostname', field_name='hostname', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedby = CharFilter(label='Created By', field_name='sourcesystemcreatedby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedtime = CharFilter(label='Created At', field_name='sourcesystemcreatedtime', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Server
        fields = '__all__'

        exclude = ('serverhashkey', 'user', 'password')
    
    def __init__(self, *args, **kwargs):
        super(ServerFilter, self).__init__(*args, **kwargs)


class ServerTunnelFilter(django_filters.FilterSet):
    servertunnelname = CharFilter(label='Server Name', field_name='servertunnelname', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    hostname = CharFilter(label='Hostname', field_name='hostname', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedby = CharFilter(label='Created By', field_name='sourcesystemcreatedby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedtime = CharFilter(label='Created At', field_name='sourcesystemcreatedtime', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = ServerTunnel
        fields = '__all__'

        exclude = ('servertunnelhashkey', 'port', 'user', 'password', 'private_key_user', 'private_key_password')
    
    def __init__(self, *args, **kwargs):
        super(ServerTunnelFilter, self).__init__(*args, **kwargs)


class DatabaseFilter(django_filters.FilterSet):
    applicationname = CharFilter(label='Application Name', field_name='applicationname', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    databasename = CharFilter(label='Database Name', field_name='databasename', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    hostname = CharFilter(label='Hostname', field_name='hostname', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedby = CharFilter(label='Created By', field_name='sourcesystemcreatedby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedtime = CharFilter(label='Created At', field_name='sourcesystemcreatedtime', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Database
        fields = '__all__'

        exclude = ('databasehashkey', 'port', 'databasetype', 'password', 'username')
    
    def __init__(self, *args, **kwargs):
        super(DatabaseFilter, self).__init__(*args, **kwargs)


class FileFilter(django_filters.FilterSet):
    filename = CharFilter(label='User Name', field_name='filename', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = CharFilter(label='Resource Pool', field_name='location', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedby = CharFilter(label='Created By', field_name='sourcesystemcreatedby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedtime = CharFilter(label='Created At', field_name='sourcesystemcreatedtime', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = File
        fields = '__all__'

        exclude = ('filehashkey', 'delimiter', 'path', )
    
    def __init__(self, *args, **kwargs):
        super(FileFilter, self).__init__(*args, **kwargs)


class QueryFilter(django_filters.FilterSet):
    name = CharFilter(label='Query Name', field_name='name', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    desc = CharFilter(label='Description', field_name='desc', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedby = CharFilter(label='Created By', field_name='sourcesystemcreatedby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedtime = CharFilter(label='Created At', field_name='sourcesystemcreatedtime', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Query
        fields = '__all__'

        exclude = ('queryhashkey', 'path')
    
    def __init__(self, *args, **kwargs):
        super(QueryFilter, self).__init__(*args, **kwargs)


class ProcessFilter(django_filters.FilterSet):
    processcode = CharFilter(label='Process Code', field_name='processcode', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    processdesc = CharFilter(label='Process Description', field_name='processdesc', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedby = CharFilter(label='Created By', field_name='sourcesystemcreatedby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedtime = CharFilter(label='Created At', field_name='sourcesystemcreatedtime', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Process
        fields = '__all__'

        exclude = ('processhashkey')
    
    def __init__(self, *args, **kwargs):
        super(ProcessFilter, self).__init__(*args, **kwargs)


class EngineFilter(django_filters.FilterSet):
    enginename = CharFilter(label='Engine Name', field_name='enginename', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedby = CharFilter(label='Created By', field_name='sourcesystemcreatedby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedtime = CharFilter(label='Created At', field_name='sourcesystemcreatedtime', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Engine
        fields = '__all__'

        exclude = ('enginehashkey')
    
    def __init__(self, *args, **kwargs):
        super(EngineFilter, self).__init__(*args, **kwargs)


class ProcessEngineFilter(django_filters.FilterSet):
    processhashkey = CharFilter(label='Process Code', field_name='processhashkey', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    enginehashkey = CharFilter(label='Engine Name', field_name='enginehashkey', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedby = CharFilter(label='Created By', field_name='sourcesystemcreatedby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedtime = CharFilter(label='Created At', field_name='sourcesystemcreatedtime', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = ProcessEngine
        fields = '__all__'

        exclude = ('processenginehashkey')
    
    def __init__(self, *args, **kwargs):
        super(ProcessEngineFilter, self).__init__(*args, **kwargs)


class ObjectFilter(django_filters.FilterSet):
    objecthashkey = CharFilter(label='Filter Object By', field_name='objecthashkey', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    objectdesc = CharFilter(label='Description Object', field_name='objectdesc', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedby = CharFilter(label='Created By', field_name='sourcesystemcreatedby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedtime = CharFilter(label='Created At', field_name='sourcesystemcreatedtime', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Object
        fields = '__all__'

        exclude = ('objectcode', 'objectname')
    
    def __init__(self, *args, **kwargs):
        super(ObjectFilter, self).__init__(*args, **kwargs)


class MultipleRelationFilter(django_filters.FilterSet):
    createdby = CharFilter(label='Created By', field_name='createdby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = CharFilter(label='Status', field_name='status', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = MultipleRelation
        fields = ('createdby','status')

        exclude = ('id', 'filepath', 'createdat', 'excel')
    
    def __init__(self, *args, **kwargs):
        super(MultipleRelationFilter, self).__init__(*args, **kwargs)


class ObjectProcessFilter(django_filters.FilterSet):
    src_objecthashkey = CharFilter(label='Object Source', field_name='src_objecthashkey', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    dest_objecthashkey = CharFilter(label='Object Destinitions', field_name='dest_objecthashkey', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    processenginehashkey = CharFilter(label='Process Engine', field_name='processenginehashkey', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    userhashkey = CharFilter(label='User', field_name='userhashkey', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedby = CharFilter(label='Created By', field_name='sourcesystemcreatedby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedtime = CharFilter(label='Created At', field_name='sourcesystemcreatedtime', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = ObjectProcess
        fields = '__all__'

        exclude = ('objectprocesshashkey')
    
    def __init__(self, *args, **kwargs):
        super(ObjectProcessFilter, self).__init__(*args, **kwargs)

class ObjectAllFilter(django_filters.FilterSet):
    objecthashkey = CharFilter(label='Filter Object By', field_name='objecthashkey', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedby = CharFilter(label='Created By', field_name='sourcesystemcreatedby', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sourcesystemcreatedtime = CharFilter(label='Created At', field_name='sourcesystemcreatedtime', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = CreateObject
        fields = ('objecthashkey', 'sourcesystemcreatedby', 'sourcesystemcreatedtime')
        # search_fields = ["objecthashkey__objecthashkey", "sourcesystemcreatedby", "sourcesystemcreatedtime"]
    
    def __init__(self, *args, **kwargs):
        super(ObjectAllFilter, self).__init__(*args, **kwargs)