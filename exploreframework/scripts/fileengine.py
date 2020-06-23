import os
import re
import pexpect
import subprocess

from os import environ
from datetime import datetime
from builtins import min as bmin
from builtins import max as bmax

class Get:
    def __init__(self, createdby = None):
        print("File Get Functions")
        now = datetime.now()
        if createdby:
            self.sourcesystemcreatedby = createdby
        else:
            self.sourcesystemcreatedby = environ.get('USER')
        self.sourcesystemcreatedtime = (now.strftime("%Y-%m-%d %H:%M:%S"))

    def ReadData(self, formattype = None, delimiter = None, encodingtype = "UTF-8", header = "true", targetpath = None, path = None, filename = None, snapshotvalue2 = None):
        if formattype not in ['xls', 'xlsx']:
            if 'nothere' not in filename:
                df = (self.spark.read \
                      .format(str(formattype)) \
                      .option("parserLib", "univocity") \
                      .option("multiLine", "true") \
                      .option("sep", str(delimiter)) \
                      .option("encoding", str(encodingtype)) \
                      .option("header", str(header))
                      .load("{targetpath}://{path}/{filename}_{snapshotvalue2}.{formattype}".format(targetpath = targetpath, path = path, filename = filename, snapshotvalue2 = snapshotvalue2, formattype = formattype)))                                    
            
            print(df.count())
        else:
            print("File format Excel,,, Temporary use pandas")
            print("import pandas as pd")
            import pandas as pd
            df_p = pd.read_excel("{path}/{filename}_{snapshotvalue2}.{formattype}".format(path = path, filename = filename, snapshotvalue2 = snapshotvalue2, formattype = formattype), keep_default_na=False)
            print("Convert Pandas Dataframe to Spark Dataframe")
            myschema = [StructField(x, StringType(), True) for x in df_p.columns]
            df = self.spark.createDataFrame(df_p, schema=StructType(myschema))

        return df

    def LoadData(self, file_path = None, file_name = None, file_delimiter = None, object_type_source = None, server_name = None, snapshotname1 = None, snapshotvalue1 = None, snapshotvalue2 = None):
        ### Update Last Snapshot with New Snapshot
        #snapshotvalue2 = self.SnapshotFile(snapshotvalue2)
        if str(server_name) == "hdfs":
            targetpath = "hdfs"
            df = self.ReadData(formattype = object_type_source, delimiter = file_delimiter, targetpath = targetpath, path = file_path, filename = file_name, snapshotvalue2 = snapshotvalue2)
        else:
            targetpath = "file"
            df = self.ReadData(formattype = object_type_source, delimiter = file_delimiter, targetpath = targetpath, path = file_path, filename = file_name, snapshotvalue2 = snapshotvalue2)

        #snapshotvalue1 = self.SnapshotDataFrame(dataframe = df, snapshotname1 = snapshotvalue1)
        if snapshotvalue1:
            df = df.filter(df[str(snapshotname1)] > str(snapshotvalue1))

        return df

    def SnapshotDataFrame(self, dataframe = None, snapshotname1 = None):
        if snapshotname1:
            # maxdataframevalue = dataframe.agg({"{}".format(str(snapshotname1)): "max"}).collect()[0][0]
            maxdataframevalue = dataframe[snapshotname1].max()
        else:
            print("No Snapshot 1")
            maxdataframevalue = ""
        return maxdataframevalue
    
    def FileMax(self, servername = None, serverhostname = None, serverusername = None, serverpassword = None, filename = None, filepath = None, fileformat = None):
        queryLinux = """find {filepath}/{filename}_[0-9]*.{fileformat}  -type f -printf '%T@ %p\n' | sort -n | tail -1| cut -f2- -d' '""".format(
                        filepath=filepath, filename=filename, fileformat=fileformat)
        print(queryLinux)
        if str(servername) == str("edgedrc"):
            printhasil = subprocess.check_output('{}'.format(queryLinux), shell = True)
            print(printhasil)
        else:
            child = pexpect.spawn(
                '''ssh {serverusername}@{serverhostname} "{}" '''.format(queryLinux, serverusername=serverusername, serverhostname=serverhostname))
            r = child.expect("{serverusername}@{serverhostname}'s password:".format(serverusername=serverusername,
                                                                                    serverhostname=serverhostname))

            if r == 0:
                child.sendline('{}'.format(serverpassword))
                printhasil = child.readlines()[-1]
                child.expect(pexpect.EOF, timeout=20)
                print('Get Max Snapshot File in Server {servername} Success'.format(servername=servername))
            else:
                print('Get Max Snapshot File in Server {servername} Failed'.format(servername=servername))
            
        printhasil = printhasil.replace("{filepath}/{filename}_".format(filepath=filepath, filename=filename), '').replace(".{fileformat}".format(fileformat=fileformat), '').replace('\r', '').replace('\n', '').replace('\t', '')
        return printhasil

    def SnapshotFileMax(self, servername = None, serverhostname = None, serverusername = None, serverpassword = None, filename = None, filepath = None, fileformat = None):
        if str(servername) == str("edgedrc"):
            listfile = os.listdir(filepath)
            listfile_filter = [x for x in listfile if filename in x]
            listfile_snapshot = [x.replace('{}_'.format(filename), '').replace('.{}'.format(fileformat), '') for x in listfile_filter]
            return bmin(listfile_snapshot)
        else:
            child = pexpect.spawn(
                """ssh {serverusername}@{serverhostname} find "{filepath}/{filename}_*.{fileformat}" -printf "%f," """.format(
                    serverusername=serverusername, serverhostname=serverhostname, filepath=filepath,
                    filename=filename, fileformat=fileformat))
            r = child.expect("{serverusername}@{serverhostname}'s password:".format(serverusername=serverusername,
                                                                                    serverhostname=serverhostname))

            if r == 0:
                child.sendline('{}'.format(serverpassword))
                printhasil = child.readlines()[-1].split(',')
                child.expect(pexpect.EOF, timeout=20)
                print('Get Max Snapshot File in Server {servername} Success'.format(servername=servername))
            else:
                print('Get Max Snapshot File in Server {servername} Failed'.format(servername=servername))
            listfile_snapshot = [x.replace('{}_'.format(filename), '').replace('.{}'.format(fileformat), '') for x in printhasil if len(x) >= 1]
            return bmin(listfile_snapshot)

    def SnapshotFileDay(self, snapshotvalue2 = None):
        ### Check Len Snapshot for knowing format Date in file ex "%Y(Year)%m(Month)%d(Days)"
        print(snapshotvalue2)
        if int(len(snapshotvalue2)) == int(6):
            #date_now = datetime.datetime.today().strftime("%Y%m")
            date_now = datetime.datetime.today().strftime("%Y%m%d")
            date_oneplus = (datetime.datetime.today() + datetime.timedelta(days = 1)).strftime("%Y%m%d")
        elif int(len(snapshotvalue2)) == int(8):
            date_past = datetime.datetime.strptime(snapshotvalue2, "%Y%m%d")
            date_now = datetime.datetime.today().strftime("%Y%m%d")
            date_oneplus = (date_past + datetime.timedelta(days=1)).strftime("%Y%m%d")
            #date_oneplus = (datetime.datetime.today() + datetime.timedelta(days = 1)).strftime("%Y%m%d")
        ### Check Equivalent date_now with last_snapshotvalue
        ### Update last_snapshotvalue with date_oneplus
        if str(snapshotvalue2) == str(date_now):
            ### Update value last_snapshot_source_1
            return str(snapshotvalue2)
        else:
            return str(date_oneplus)

    def SnapshotFileMonth(self, snapshotvalue2 = None):
        ### Check Len Snapshot for knowing format Date in file ex "%Y(Year)%m(Month)%d(Days)"
        print(snapshotvalue2)
        if int(len(snapshotvalue2)) == int(8):
            date_past = datetime.datetime.strptime(snapshotvalue2, "%Y%m%d")
            date_now = datetime.datetime.today().strftime("%Y%m%d")
            date_oneplus = (date_past + relativedelta(months=1)).strftime("%Y%m%d")
            #date_oneplus = (datetime.datetime.today() + datetime.timedelta(days = 1)).strftime("%Y%m%d")
        ### Check Equivalent date_now with last_snapshotvalue
        ### Update last_snapshotvalue with date_oneplus
        if str(snapshotvalue2) == str(date_now):
            ### Update value last_snapshot_source_1
            return str(snapshotvalue2)
        else:
            return str(date_oneplus)

    def SnapshotFileWeek(self, snapshotvalue2 = None):
        ### Check Len Snapshot for knowing format Date in file ex "%Y(Year)%m(Month)%d(Days)"
        print(snapshotvalue2)
        if int(len(snapshotvalue2)) == int(8):
            date_past = datetime.datetime.strptime(snapshotvalue2, "%Y%m%d")
            date_now = datetime.datetime.today().strftime("%Y%m%d")
            date_oneplus = (date_past + datetime.timedelta(days=7)).strftime("%Y%m%d")
            #date_oneplus = (datetime.datetime.today() + datetime.timedelta(days = 1)).strftime("%Y%m%d")
        ### Check Equivalent date_now with last_snapshotvalue
        ### Update last_snapshotvalue with date_oneplus
        if str(snapshotvalue2) == str(date_now):
            ### Update value last_snapshot_source_1
            return str(snapshotvalue2)
        else:
            return str(date_oneplus)

    def ListColumnsOtherServer(self, path_script = None):
        child = pexpect.spawn(
            """ssh {serverusername}@{serverhostname} python '{path_script}' "'{filepath}'" "'{filename}'" "'{filedelimiter}'" "'{fileformat}'" """.format(
                serverusername=self.serverusername, serverhostname=self.serverhostname, filepath=self.filepath, filename=self.filename,
                filedelimiter=self.filedelimiter, fileformat=self.fileformat, path_script = path_script))
        r = child.expect("{serverusername}@{serverhostname}'s password:".format(serverusername=self.serverusername,
                                                                                serverhostname=self.serverhostname))
        if r == 0:
            child.sendline('{}'.format(self.serverpassword))
            printhasil = child.readlines()[-1]
            child.expect(pexpect.EOF, timeout=20)
            print('Get Header File in Server {servername} Success'.format(servername=self.servername))
        else:
            print('Get Header File in Server {servername} Failed'.format(servername=self.servername))
        return str(printhasil)

    def ListColumnsOtherNode(self):
        import pandas as pd
        snapshotfile = self.SnapshotFileMax(servername = self.servername, serverhostname = self.serverhostname, serverusername = self.serverusername, serverpassword = self.serverpassword, filename = self.filename, filepath = self.filepath, fileformat = self.fileformat)
        if str(self.fileformat) == str('json'):
            df = pd.read_json("{}/{}_{}.{}".format(self.filepath, self.filename, snapshotfile, self.fileformat))
        elif str(self.fileformat) == str('csv'):
            df = pd.read_csv("{}/{}_{}.{}".format(self.filepath, self.filename, snapshotfile, self.fileformat), sep = '{}'.format(self.filedelimiter), low_memory=False)
        elif str(self.fileformat) == str('xls') or str(self.fileformat) == str('xlsx'):
            df = pd.read_excel("{}/{}_{}.{}".format(self.filepath, self.filename, snapshotfile, self.fileformat))
        elif str(self.fileformat) == str('text'):
            df = pd.read_text("{}/{}_{}.{}".format(self.filepath, self.filename, snapshotfile, self.fileformat))
        printhasil = [str(c).replace('.', '_').replace(' ', '_').replace("(","").replace(")","").replace("'", "").replace(":", "").replace("/", "").replace("&", "_").replace("-", "_").lower() for c in df.columns]
        #printhasil = [re.sub("[(). / | -`;:'^$#@!&*]", "_", str(x.lower())) for x in df.columns]
        return str(printhasil)

    def ObjectDesc(self, servername = None, serverhostname = None, serverusername = None, serverpassword = None, filename = None, filepath = None, filedelimiter = None, fileformat = None, objecthashkey = None):
        # Self Variable
        self.servername = servername
        self.serverhostname = serverhostname
        self.serverusername = serverusername
        self.serverpassword = serverpassword
        self.filename = filename
        self.filepath = filepath
        self.filedelimiter = filedelimiter
        self.fileformat = fileformat
        self.objecthashkey = objecthashkey
        # Check Server Name
        if str(self.servername) == str("edgedrc") :
            path_scripts = "/scripts/adi/core/get_header.py"
            printhasil = self.ListColumnsOtherServer(path_script = path_scripts)
        elif str(self.servername) == str("gatewaydrclyl"):
            path_scripts = "/home/adilyl01a000/get_header.py"
            printhasil = self.ListColumnsOtherServer(path_script = path_scripts)
        elif str(self.servername) == str('cariparkirrep'):
            path_scripts = "/home/crpdbadmin/document/mobilitysolution/get_header.py"
            printhasil = self.ListColumnsOtherServer(path_script=path_scripts)
        elif str(self.servername) == str('sevarep'):
            path_scripts = "/home/sevadbadmin/Documents/get_header.py"
            printhasil = self.ListColumnsOtherServer(path_script=path_scripts)
        elif str(self.servername) == str("gatewaypdc") or str(self.servername) == str("gatewaydrc"):
            printhasil = self.ListColumnsOtherNode()
        else:
            print("Wait Until Next Update for Other Server Name, Stay Tune... :)")

        list_columns = re.sub("[|[\r\n]|]|'| ", "", printhasil).split(',')
        list_objecthashkey = [objecthashkey for x in list_columns]
        list_type = ['string' for x in list_columns]
        list_length = ['' for x in list_columns]
        list_key = ['0' for x in list_columns]
        list_nullable = ['0' for x in list_columns]
        data = zip(list_objecthashkey, list_columns, list_type, list_length, list_nullable, list_key)
        column = ['objecthashkey_id', 'deschashkey', 'datatype', 'length', 'nullable', 'primary']
        df = pd.DataFrame(data=data, columns=column)
        df["objectdeschashkey"] = df['objecthashkey_id'].map(str) + df['deschashkey'].map(str)
        df['sourcesystemcreatedby'] = str(self.sourcesystemcreatedby)
        df['sourcesystemcreatedtime'] = self.sourcesystemcreatedtime
        return df
