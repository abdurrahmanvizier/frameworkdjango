from rest_framework import serializers

from framework.models import Object

class ObjectSerializer(serializers.HyperlinkedModelSerializer):

    objecthashkey = serializers.ReadOnlyField(source='Object.objecthashkey')

    class Meta:
        model = Object
        fields = ('objecthashkey', 'objectcode', 'objectname', 'objectdesc', 'sourcesystemcreatedby', 'sourcesystemcreatedtime')
        read_only_fields = ('objecthashkey', 'sourcesystemcreatedby')