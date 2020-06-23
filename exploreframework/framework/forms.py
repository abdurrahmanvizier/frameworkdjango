from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


from .models import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML, Reset


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DatabaseForm(forms.ModelForm):
    class Meta:
        model = Database
        fields = '__all__'
        exclude = ('databasehashkey', 'sourcesystemcreatedtime')
        # sourcesystemcreatedby = forms.CharField(
        #     widget=forms.TextInput(attrs={'readonly':'readonly'})
        # )
        widgets = {
            'applicationname': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'databasename': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'hostname': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'databasetype': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'port': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'required': True, 'class': 'form-control'}),
            'sourcesystemcreatedby': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        labels = {
            'sourcesystemcreatedby': ('Created By'),
        }
    
    def __init__(self, *args, **kwargs):
        super(DatabaseForm, self).__init__(*args, **kwargs)
        self.fields['sourcesystemcreatedby'].disabled = True
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'adddatabase/'
        self.helper.layout = Layout(
            Row(
                Column('applicationname', css_class='form-group col-md-6 mb-0'),
                Column('databasename', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('hostname', css_class='form-group col-md-6 mb-0'),
                Column('port', css_class='form-group col-md-6 mb-0'),
                Column('databasetype', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('username', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'sourcesystemcreatedby',
            HTML('<br>'),
            Submit('submit', 'Submit', css_class='btn btn-sm btn-block'),
        )


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'
        exclude = ('ownerhashkey', 'sourcesystemcreatedtime')
        widgets = {
            'ownername': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'sourcesystemcreatedby': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        labels = {
            'sourcesystemcreatedby': ('Created By'),
        }
    
    def __init__(self, *args, **kwargs):
        super(OwnerForm, self).__init__(*args, **kwargs)
        self.fields['sourcesystemcreatedby'].disabled = True
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'addowner/'
        self.helper.layout = Layout(
            Row(
                Column('ownername', css_class='form-group col-md-6 mb-0'),
                Column('sourcesystemcreatedby', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            HTML('<br>'),
            Submit('submit', 'Submit', css_class='btn btn-sm btn-block'),
        )


class StorageEngineForm(forms.ModelForm):
    class Meta:
        model = StorageEngine
        fields = '__all__'
        exclude = ('storageenginehashkey', 'sourcesystemcreatedtime')
        widgets = {
            'storageenginetype': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'sourcesystemcreatedby': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        labels = {
            'sourcesystemcreatedby': ('Created By'),
        }
    
    def __init__(self, *args, **kwargs):
        super(StorageEngineForm, self).__init__(*args, **kwargs)
        self.fields['sourcesystemcreatedby'].disabled = True
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'addstorageengine/'
        self.helper.layout = Layout(
            Row(
                Column('storageenginetype', css_class='form-group col-md-6 mb-0'),
                Column('sourcesystemcreatedby', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            HTML('<br>'),
            Submit('submit', 'Submit', css_class='btn btn-sm btn-block'),
        )


class ObjectTypeForm(forms.ModelForm):
    class Meta:
        model = ObjectType
        fields = '__all__'
        exclude = ('objecttypehashkey', 'sourcesystemcreatedtime')
        widgets = {
            'objecttype': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'sourcesystemcreatedby': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        labels = {
            'sourcesystemcreatedby': ('Created By'),
        }
    
    def __init__(self, *args, **kwargs):
        super(ObjectTypeForm, self).__init__(*args, **kwargs)
        self.fields['sourcesystemcreatedby'].disabled = True
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'addobjecttype/'
        self.helper.layout = Layout(
            Row(
                Column('objecttype', css_class='form-group col-md-6 mb-0'),
                Column('sourcesystemcreatedby', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            HTML('<br>'),
            Submit('submit', 'Submit', css_class='btn btn-sm btn-block'),
        )


class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = '__all__'
        exclude = ('serverhashkey', 'sourcesystemcreatedtime')
        # sourcesystemcreatedby = forms.CharField(
        #     widget=forms.TextInput(attrs={'readonly':'readonly'})
        # )
        widgets = {
            'servername': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'hostname': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'user': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'required': True, 'class': 'form-control'}),
            'sourcesystemcreatedby': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        labels = {
            'sourcesystemcreatedby': ('Created By'),
        }
    
    def __init__(self, *args, **kwargs):
        super(ServerForm, self).__init__(*args, **kwargs)
        self.fields['sourcesystemcreatedby'].disabled = True
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'addserver/'
        self.helper.layout = Layout(
            Row(
                Column('servername', css_class='form-group col-md-6 mb-0'),
                Column('hostname', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('user', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'sourcesystemcreatedby',
            HTML('<br>'),
            Submit('submit', 'Submit', css_class='btn btn-sm btn-block'),
        )


class ServerTunnelForm(forms.ModelForm):
    class Meta:
        model = ServerTunnel
        fields = '__all__'
        exclude = ('servertunnelhashkey', 'sourcesystemcreatedtime')
        # sourcesystemcreatedby = forms.CharField(
        #     widget=forms.TextInput(attrs={'readonly':'readonly'})
        # )
        widgets = {
            'servertunnelname': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'hostname': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'port': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'user': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'required': True, 'class': 'form-control'}),
            'private_key_user': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'private_key_password': forms.PasswordInput(attrs={'required': True, 'class': 'form-control'}),
            'sourcesystemcreatedby': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        labels = {
            'sourcesystemcreatedby': ('Created By'),
        }
    
    def __init__(self, *args, **kwargs):
        super(ServerTunnelForm, self).__init__(*args, **kwargs)
        self.fields['sourcesystemcreatedby'].disabled = True
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'addservertunnel/'
        self.helper.layout = Layout(
            Row(
                Column('servertunnelname', css_class='form-group col-md-5 mb-0'),
                Column('hostname', css_class='form-group col-md-5 mb-0'),
                Column('port', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('user', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('private_key_user', css_class='form-group col-md-6 mb-0'),
                Column('private_key_password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'sourcesystemcreatedby',
            HTML('<br>'),
            Submit('submit', 'Submit', css_class='btn btn-sm btn-block'),
        )


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
        exclude = ('filehashkey', 'sourcesystemcreatedtime')
        # sourcesystemcreatedby = forms.CharField(
        #     widget=forms.TextInput(attrs={'readonly':'readonly'})
        # )
        widgets = {
            'filename': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'delimiter': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'path': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'sourcesystemcreatedby': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        labels = {
            'sourcesystemcreatedby': ('Created By'),
        }
    
    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        self.fields['sourcesystemcreatedby'].disabled = True
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'addfile/'
        self.helper.layout = Layout(
            Row(
                Column('filename', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('location', css_class='form-group col-md-5 mb-0'),
                Column('delimiter', css_class='form-group col-md-2 mb-0'),
                Column('path', css_class='form-group col-md-5 mb-0'),
                css_class='form-row'
            ),
            'sourcesystemcreatedby',
            HTML('<br>'),
            Submit('submit', 'Submit', css_class='btn btn-sm btn-block'),
        )


class UserForm(forms.ModelForm):
    class Meta:
        model = ObjectUser
        fields = '__all__'
        exclude = ('userhashkey', 'sourcesystemcreatedtime')
        widgets = {
            'username': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'resourcepool': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'sourcesystemcreatedby': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        labels = {
            'sourcesystemcreatedby': ('Created By'),
        }
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['sourcesystemcreatedby'].disabled = True
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'adduser/'
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-6 mb-0'),
                Column('resourcepool', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'sourcesystemcreatedby',
            HTML('<br>'),
            Submit('submit', 'Submit', css_class='btn btn-sm btn-block'),
        )


class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = '__all__'
        exclude = ('queryhashkey', 'sourcesystemcreatedtime')
        widgets = {
            'name': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'path': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'sourcesystemcreatedby': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        labels = {
            'sourcesystemcreatedby': ('Created By'),
        }
    
    def __init__(self, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)
        self.fields['sourcesystemcreatedby'].disabled = True
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'addquery/'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('path', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('desc', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            'sourcesystemcreatedby',
            HTML('<br>'),
            Submit('submit', 'Submit', css_class='btn btn-sm btn-block'),
        )


class PartitionByForm(forms.ModelForm):
    class Meta:
        model = PartitionBy
        fields = '__all__'
        exclude = ('objectpartitionhashkey', 'sourcesystemcreatedtime')
        # sourcesystemcreatedby = forms.CharField(
        #     widget=forms.TextInput(attrs={'readonly':'readonly'})
        # )
        widgets = {
            'partitionby': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'sourcesystemcreatedby': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        labels = {
            'sourcesystemcreatedby': ('Created By'),
        }
    
    def __init__(self, *args, **kwargs):
        super(PartitionByForm, self).__init__(*args, **kwargs)
        self.fields['sourcesystemcreatedby'].disabled = True
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'addpartition/'
        self.helper.layout = Layout(
            Row(
                Column('partitionby', css_class='form-group col-md-6 mb-0'),
                Column('sourcesystemcreatedby', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            HTML('<br>'),
            Submit('submit', 'Submit', css_class='btn btn-sm btn-block'),
        )


class SnapShotForm(forms.ModelForm):
    class Meta:
        model = SnapShot
        fields = '__all__'
        exclude = ('objectsnapshothashkey', 'sourcesystemcreatedtime')
        # sourcesystemcreatedby = forms.CharField(
        #     widget=forms.TextInput(attrs={'readonly':'readonly'})
        # )
        widgets = {
            'snapshot1': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'snapshot2': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'sourcesystemcreatedby': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        labels = {
            'sourcesystemcreatedby': ('Created By'),
        }
    
    def __init__(self, *args, **kwargs):
        super(SnapShotForm, self).__init__(*args, **kwargs)
        self.fields['sourcesystemcreatedby'].disabled = True
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'addsnapshot/'
        self.helper.layout = Layout(
            Row(
                Column('snapshot1', css_class='form-group col-md-6 mb-0'),
                Column('snapshot2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'sourcesystemcreatedby',
            HTML('<br>'),
            Submit('submit', 'Submit', css_class='btn btn-sm btn-block'),
        )


class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = '__all__'
        exclude = ('processhashkey', 'processcode', 'sourcesystemcreatedtime')
        widgets = {
            'processdesc': forms.Textarea(attrs={'required': True, 'class': 'form-control'}),
            'sourcesystemcreatedby': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        labels = {
            'sourcesystemcreatedby': ('Created By'),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProcessForm, self).__init__(*args, **kwargs)
        self.fields['sourcesystemcreatedby'].disabled = True
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'addprocess/'
        self.helper.layout = Layout(
            Row(
                Column('processdesc', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'sourcesystemcreatedby',
            HTML('<br>'),
            Submit('submit', 'Submit', css_class='btn btn-sm btn-block'),
        )


class EngineForm(forms.ModelForm):
    class Meta:
        model = Engine
        fields = '__all__'
        exclude = ('enginehashkey', 'sourcesystemcreatedtime')
        widgets = {
            'enginename': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'sourcesystemcreatedby': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        labels = {
            'sourcesystemcreatedby': ('Created By'),
        }
    
    def __init__(self, *args, **kwargs):
        super(EngineForm, self).__init__(*args, **kwargs)
        self.fields['sourcesystemcreatedby'].disabled = True
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'addengine/'
        self.helper.layout = Layout(
            Row(
                Column('enginename', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'sourcesystemcreatedby',
            HTML('<br>'),
            Submit('submit', 'Submit', css_class='btn btn-sm btn-block'),
        )


class ProcessEngineForm(forms.ModelForm):
    class Meta:
        model = ProcessEngine
        fields = '__all__'
        exclude = ('processenginehashkey', 'sourcesystemcreatedtime')
        widgets = {
            'processhashkey': forms.Select(attrs={'required': True, 'class': 'form-control'}),
            'enginehashkey': forms.Select(attrs={'required': True, 'class': 'form-control'}),
            'sourcesystemcreatedby': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        labels = {
            'sourcesystemcreatedby': ('Created By'),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProcessEngineForm, self).__init__(*args, **kwargs)
        self.fields['sourcesystemcreatedby'].disabled = True
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'addprocessengine/'
        self.helper.layout = Layout(
            Row(
                Column('processhashkey', css_class='form-group col-md-6 mb-0'),
                Column('enginehashkey', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'sourcesystemcreatedby',
            HTML('<br>'),
            Submit('submit', 'Submit', css_class='btn btn-sm btn-block'),
        )


class ObjectRelationForm(forms.ModelForm):
    class Meta:
        model = CreateObject
        fields = '__all__'     
        exclude = ('id', 'objectdeschash')

        widgets = {        
            'objecthashkey': forms.HiddenInput(attrs={'required': True}),
            'objectname': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'objectdesc': forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'ownerhashkey': forms.Select(attrs={'required': False, 'class': 'form-control'}),
            'storageenginehashkey': forms.Select(attrs={'required': False, 'class': 'form-control'}),
            'objecttypehashkey': forms.Select(attrs={'required': False, 'class': 'form-control'}),
            'databasehashkey': forms.Select(attrs={'required': False, 'class': 'form-control'}),
            'serverhashkey': forms.Select(attrs={'required': False, 'class': 'form-control'}),
            'servertunnelhashkey': forms.Select(attrs={'required': False, 'class': 'form-control'}),
            'filehashkey': forms.Select(attrs={'required': False, 'class': 'form-control'}),
            'objectpartitionhashkey': forms.Select(attrs={'required': False, 'class': 'form-control'}),
            'objectsnapshothashkey': forms.Select(attrs={'required': False, 'class': 'form-control'}),
            'queryhashkey': forms.Select(attrs={'required': False, 'class': 'form-control'}),
            'sourcesystemcreatedby': forms.TextInput(attrs={'required': True, 'class': 'form-control', 'readonly': 'readonly'}),
            'sourcesystemcreatedtime': forms.HiddenInput(attrs={'required': True}),
        }
        labels = {
            'sourcesystemcreatedby': ('Created By'),
        }

    def __init__(self, *args, **kwargs):
        super(ObjectRelationForm, self).__init__(*args, **kwargs)
        self.fields['sourcesystemcreatedby'].disabled = True
        self.fields['ownerhashkey'].required = False
        self.fields['storageenginehashkey'].required = False
        self.fields['objecttypehashkey'].required = False
        self.fields['databasehashkey'].required = False
        self.fields['serverhashkey'].required = False
        self.fields['servertunnelhashkey'].required = False
        self.fields['filehashkey'].required = False
        self.fields['objectpartitionhashkey'].required = False
        self.fields['objectsnapshothashkey'].required = False
        self.fields['queryhashkey'].required = False
        self.fields['objecthashkey'].required = False
        self.fields['sourcesystemcreatedtime'].required = False
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'oneobject/'
        self.helper.layout = Layout(
            Row(
                Column('objectname', css_class='form-group col-md-6 mb-0'),
                Column('objectdesc', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('ownerhashkey', css_class='form-group col-md-3 mb-0'),
                Column('storageenginehashkey', css_class='form-group col-md-5 mb-0'),
                Column('objecttypehashkey', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('databasehashkey', css_class='form-group col-md-4 mb-0'),
                Column('serverhashkey', css_class='form-group col-md-4 mb-0'),
                Column('servertunnelhashkey', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('filehashkey', css_class='form-group col-md-6 mb-0'),
                Column('objectpartitionhashkey', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('objectsnapshothashkey', css_class='form-group col-md-6 mb-0'),
                Column('queryhashkey', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'sourcesystemcreatedby',
            HTML('<br>'),
            Row(
                Column(Submit('submit', 'Submit', css_class='btn btn-sm btn-block')),
                Column(Reset('Reset This Form', 'Revert Me!', css_class='btn btn-sm btn-block')),
                Column(Submit('submit', 'Create Another', css_class='btn btn-sm btn-block')),
                css_class='form-row'
            ),
        )

    # def __init__(self, *args, **kwargs):
    #     # first call parent's constructor
    #     super(CreateObject, self).__init__(*args, **kwargs)
    #     # there's a `fields` property now
        

class MultipleRelationForm(forms.ModelForm):
    class Meta:
        model = MultipleRelation
        fields = '__all__'     
        exclude = ('id', 'filename', 'filepath', 'createdat', 'stataus')

        widgets = {        
            'createdby': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'excel': forms.FileInput(attrs={'class': 'custom-file'}),
        }

    def __init__(self, *args, **kwargs):
        super(MultipleRelationForm, self).__init__(*args, **kwargs)
        self.fields['createdby'].disabled = True


class ObjectProcesRelationForm(forms.ModelForm):
    GenerateObjectDesc = forms.BooleanField()
    class Meta:
        model = ObjectProcess
        fields = '__all__'     
        exclude = ('objectprocesshashkey', 'sourcesystemcreatedtime')

        widgets = {        
            'src_objecthashkey': forms.Select(attrs={'required': 'true', 'class': 'form-control'}),
            'dest_objecthashkey': forms.Select(attrs={'required': 'true', 'class': 'form-control'}),
            'processenginehashkey': forms.Select(attrs={'required': 'true', 'class': 'form-control'}),
            'userhashkey': forms.Select(attrs={'required': 'true', 'class': 'form-control'}),
            'GenerateObjectDesc': forms.CheckboxInput(attrs={'required': 'false'}),
            'sourcesystemcreatedby': forms.TextInput(attrs={'required': True, 'class': 'form-control', 'readonly': 'readonly'}),
        }

        labels = {
            'src_objecthashkey': ('Object Source'),
            'dest_objecthashkey': ('Object Target'),
            'processenginehashkey': ('Process Engine'),
            'userhashkey': ('User Engine'),
            'GenerateObjectDesc':('ObjectDesc?'),
            'sourcesystemcreatedby': ('Created By'),
        }

    def __init__(self, *args, **kwargs):
        super(ObjectProcesRelationForm, self).__init__(*args, **kwargs)
        self.fields['sourcesystemcreatedby'].disabled = True
        self.fields['GenerateObjectDesc'].required = False
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'addoneobjectsprocessrelation/'
        self.helper.layout = Layout(
            Row(
                Column('src_objecthashkey', css_class='form-group col-md-3 mb-0'),
                Column('dest_objecthashkey', css_class='form-group col-md-3 mb-0'),
                Column('processenginehashkey', css_class='form-group col-md-3 mb-0'),
                Column('userhashkey', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            'GenerateObjectDesc',
            'sourcesystemcreatedby',
            HTML('<br>'),
            Submit('submit', 'Submit', css_class='btn btn-sm btn-block'),
        )
