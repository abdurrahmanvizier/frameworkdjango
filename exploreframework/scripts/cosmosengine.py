# -*- coding: utf-8 -*-

"""
Cosmos Engine

@author: Dul 20200411

"""

from os import environ
from datetime import datetime
from dateutil.parser import parse

import pandas as pd
import numpy as np

class Get:
    def __init__(self, connection = None, client = None, databasename = None):
        print("Cosmos Get Function")
        self.connection = connection
        self.client = client
        self.databasename = databasename
        now = datetime.now()
        self.sourcesystemcreatedby = environ.get('USER')
        self.sourcesystemcreatedtime = (now.strftime("%Y-%m-%d %H:%M:%S"))
    
    def flatten_dict(self, dd, separator='_', prefix=''):
        return { prefix + separator + k if prefix else k : v
                    for kk, vv in dd.items()
                    for k, v in self.flatten_dict(vv, separator, kk).items()
                    } if isinstance(dd, dict) else { prefix : dd }

    def FetchData(self, query = None):
        db = self.connection[self.client]
        col = db[self.databasename]
        if query:
            print(query)
            all_data = list(col.find(query))
        else:
            all_data = list(col.find())
        
        return all_data

    def ConvertToDataframe(self, all_data = None, columns = None):
        flatten = [self.flatten_dict(data) for data in all_data]
        
        if columns:
            df = pd.DataFrame(flatten, columns = columns)
        else:
            # Not Recomended for Getting All Data (FULL LOAD)
            # Cause the process used a BIG RESOURCE 
            df = pd.DataFrame(flatten)

        return df

    def LoadData(self, snapshotname1 = None, snapshotname2 = None, snapshotvalue1 = None, snapshotvalue2 = None):
        if snapshotname1:
            try:
                snapshotvalue1 = parse(snapshotvalue1)
            except:
                snapshotvalue1 = str(snapshotvalue1)
            if snapshotname2:
                try:
                    snapshotvalue2 = parse(snapshotvalue2)
                except:
                    snapshotvalue2 = str(snapshotvalue2)
                querywhere = {'$and': [{snapshotname1: {'$gt': snapshotvalue1}}, {snapshotname2: {'$gt': snapshotvalue2}}]}
                query = querywhere
            else:
                querywhere = {snapshotname1: {'$gt': snapshotvalue1}}
                query = querywhere

            all_data = self.FetchData(query = query)
        else:
            all_data = self.FetchData()

        return all_data

    def TotalRow(self, snapshotname1 = None, snapshotname2 = None, snapshotvalue1 = None, snapshotvalue2 = None):
        if snapshotname1:
            try:
                snapshotvalue1 = parse(snapshotvalue1)
            except:
                snapshotvalue1 = str(snapshotvalue1)
            if snapshotname2:
                try:
                    snapshotvalue2 = parse(snapshotvalue2)
                except:
                    snapshotvalue2 = str(snapshotvalue2)
                querywhere = {'$and': [{snapshotname1: {'$gt': snapshotvalue1}}, {snapshotname2: {'$gt': snapshotvalue2}}]}
                query = querywhere
            else:
                querywhere = {snapshotname1: {'$gt': snapshotvalue1}}
                query = querywhere

            all_data = self.FetchData(query = query)
        else:
            all_data = self.FetchData()

        return len(all_data)

    def Snapshot(self, snapshotname1 = None, snapshotname2 = None):
        # col.find().sort({"created_at": -1}).limit(1)
        # list(col.find().sort([('created_at', -1)]).limit(1))[0]['created_at']
        db = self.connection[self.client]
        col = db[self.databasename]
        if snapshotname2:
            snapshotvalue = list(col.find().sort([(snapshotname1, -1)]).limit(1))[0][snapshotname1]
        else:
            snapshotvalue = list(col.find().sort([(snapshotname1, -1)]).limit(1))[0][snapshotname1]
        
        return snapshotvalue

    def ObjectDesc(self, objecthashkey):
        """
        Keterangan:
        Berdasarkan Dokumentasi MongoDB bahwa Column `_id` selalu ada disetiap document
        "The _id field is always the first field in the document"
        "By default, MongoDB creates a unique index on the _id field during the creation of a collection."
        "https://docs.mongodb.com/manual/core/document/#document-field-order"
        
        Jadi untuk mendapatkan semua column dalam 1 document, harus menggunakan query dibawah ini
            > list(col.find().sort([('_id', -1)]).limit(1))
        """
        db = self.connection[self.client]
        col = db[self.databasename]
        all_data = list(col.find().sort([('_id', -1)]).limit(1))
        flatten = [self.flatten_dict(data) for data in all_data]
        columns_name = flatten[0].keys()
        df = pd.DataFrame(columns_name, columns = ['deschashkey'])
        df['objecthashkey'] = objecthashkey
        df['datatype'] = 'string'
        df['length'] = ''
        df['primary'] = np.where(df['deschashkey'] == '_id', '1', '0')
        df['nullable'] = np.where(df['deschashkey'] == '_id', '0', '1')
        df['objectdeschashkey'] = df['objecthashkey'] + df['deschashkey']
        df['sourcesystemcreatedby'] = self.sourcesystemcreatedby
        df['sourcesystemcreatedtime'] = self.sourcesystemcreatedtime

        return df