from django_filters import rest_framework as filters

from framework.models import Object

class ObjectFilter(filters.FilterSet):
    
    class Meta:
        model = Object
        fields = ('objecthashkey', 'objectname', 'sourcesystemcreatedby', 'sourcesystemcreatedtime')