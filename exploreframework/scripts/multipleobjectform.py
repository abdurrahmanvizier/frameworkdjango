from django import forms
from django.urls import reverse_lazy

from funky_sheets.formsets import HotView

from framework.models import CreateObject


class CreateObjectView(HotView):
    # Define model to be used by the view
    model = CreateObject
    # Define template
    print(model)
    template_name = 'frameworkinput/multipleinput_form.html'
    # Define custom characters/strings for checked/unchecked checkboxes
    checkbox_checked = 'yes' # default: true
    checkbox_unchecked = 'no' # default: 'false'
    # Define prefix for the formset which is constructed from Handsontable spreadsheet on submission
    prefix = 'table'
    # Define success URL
    success_url = reverse_lazy('multipleframeworkupdate')
    
    # Define fields to be included as columns into the Handsontable spreadsheet
    fields = (
        'objectname',
        'ownerhashkey',
        'storageenginehashkey',
        'objecttypehashkey',
        'databasehashkey',
        'serverhashkey',
        'servertunnelhashkey',
        'filehashkey',
        'objectpartitionhashkey',
        'objectsnapshothashkey', 
        'queryhashkey',
        'objectdesc',
    )

    # Define extra formset factory kwargs
    factory_kwargs = {
        'widgets' : {     
            'objectname': forms.TextInput(attrs={'required': 'true'}),
            'objectdesc': forms.TextInput(attrs={'required': 'true'}),
            'ownerhashkey': forms.Select(attrs={'required': 'false'}),
            'storageenginehashkey': forms.Select(attrs={'required': 'false'}),
            'objecttypehashkey': forms.Select(attrs={'required': 'false'}),
            'databasehashkey': forms.Select(attrs={'required': 'false'}),
            'serverhashkey': forms.Select(attrs={'required': 'false'}),
            'servertunnelhashkey': forms.Select(attrs={'required': 'false'}),
            'filehashkey': forms.Select(attrs={'required': 'false'}),
            'objectpartitionhashkey': forms.Select(attrs={'required': 'false'}),
            'objectsnapshothashkey': forms.Select(attrs={'required': 'false'}),
            'queryhashkey': forms.Select(attrs={'required': 'false'}),               
        },
        'labels' : {
            'objectname': ('Object Name'),
            'objectdesc': ('Object Desc'),
            'ownerhashkey': ('Owner'),
            'storageenginehashkey': ('Storage'),
            'objecttypehashkey': ('Type'),
            'databasehashkey': ('Database'),
            'serverhashkey': ('Server'),
            'servertunnelhashkey': ('Server Tunnel'),
            'filehashkey': ('File'),
            'objectpartitionhashkey': ('Partition'),
            'objectsnapshothashkey': ('Snapshot'),
            'queryhashkey': ('Query'),
            'sourcesystemcreatedby': ('CreatedBy'),
        }
    }
    # Define Handsontable settings as defined in Handsontable docs

    hot_settings = {
        # 'columnSorting': 'true',
        'contextMenu': 'true',
        'autoWrapRow': 'true',
        'rowHeaders': 'true',
        'contextMenu': 'true',
        'search': 'true',
        'licenseKey': 'non-commercial-and-evaluation',
    }

    # hx

class UpdateObjectView(CreateObjectView):
  template_name = 'frameworkinput/multipleupdate_form.html'
  # Define 'update' action
  action = 'multipleframeworkupdate'
  # Define 'update' button
  button_text = 'Update'

  hot_settings = {
        # 'columnSorting': 'true',
        'contextMenu': 'true',
        'autoWrapRow': 'true',
        'rowHeaders': 'true',
        'contextMenu': 'true',
        'search': 'true',
        'licenseKey': 'non-commercial-and-evaluation',
    }