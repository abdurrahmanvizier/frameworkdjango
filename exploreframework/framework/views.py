from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

from django.core.files.storage import FileSystemStorage

from django.urls import reverse_lazy

from funky_sheets.formsets import HotView

### Change when going to prod
from .models import *

from .forms import *
from .filters import *
from .decorators import *

from scripts.processmultipleobject import MultipleObject
from scripts.generateobjectdesc import ManualDesc

from scripts import multipleobjectform
from scripts import funtions as fcs


import os

# Create your views here.
@allowed_users(allowed_user=['adiden', 'testing', 'agrabdur7137'])
def home(request):
    total_object = Object.objects.all().count()
    total_owner = Owner.objects.all().count()
    total_storageengine = StorageEngine.objects.all().count()
    total_objecttype = ObjectType.objects.all().count()
    total_partition = PartitionBy.objects.all().count()
    total_server = Server.objects.all().count()
    total_servertunnel = ServerTunnel.objects.all().count()
    total_files = File.objects.all().count()
    total_database = Database.objects.all().count()
    total_snapshot = SnapShot.objects.all().count()
    total_query = Query.objects.all().count()
    total_process = Process.objects.all().count()
    total_engine = Engine.objects.all().count()
    total_processengine = ProcessEngine.objects.all().count()
    total_user = ObjectUser.objects.all().count()

    context = {
        'total_object':total_object,
        'total_owner':total_owner,
        'total_storageengine':total_storageengine,
        'total_objecttype':total_objecttype,
        'total_partition':total_partition,
        'total_server':total_server,
        'total_servertunnel':total_servertunnel,
        'total_files':total_files,
        'total_database':total_database,
        'total_snapshot':total_snapshot,
        'total_query':total_query,
        'total_process':total_process,
        'total_engine':total_engine,
        'total_processengine':total_processengine,
        'total_user':total_user,
    }
    print(context)
    return render(request, 'dashboard.html', context)

@unauthenticated_user
def registerPage(request):
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        # print(form)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            group = Group.objects.get(name='testing')
            user.groups.add(group)
            
            messages.success(request, 'Account was created for ' + username)
            
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_login = authenticate(request, username = username, password = password)
        if user_login is not None:
            # print(user_login)
            login(request, user_login)
            return redirect('home')
        else:
            messages.info(request, "Username and Password is Incorrect")
    
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    total_object = Object.objects.all().count()
    total_owner = Owner.objects.all().count()
    total_storageengine = StorageEngine.objects.all().count()
    total_objecttype = ObjectType.objects.all().count()
    total_partition = PartitionBy.objects.all().count()
    total_server = Server.objects.all().count()
    total_servertunnel = ServerTunnel.objects.all().count()
    total_files = File.objects.all().count()
    total_database = Database.objects.all().count()
    total_snapshot = SnapShot.objects.all().count()
    total_query = Query.objects.all().count()
    total_process = Process.objects.all().count()
    total_engine = Engine.objects.all().count()
    total_processengine = ProcessEngine.objects.all().count()
    total_user = ObjectUser.objects.all().count()

    context = {
        'total_object':total_object,
        'total_owner':total_owner,
        'total_storageengine':total_storageengine,
        'total_objecttype':total_objecttype,
        'total_partition':total_partition,
        'total_server':total_server,
        'total_servertunnel':total_servertunnel,
        'total_files':total_files,
        'total_database':total_database,
        'total_snapshot':total_snapshot,
        'total_query':total_query,
        'total_process':total_process,
        'total_engine':total_engine,
        'total_processengine':total_processengine,
        'total_user':total_user,
    }
    print(context)
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def frameworklist(request):
    objects_rel = CreateObject.objects.all()[:5]
    objectproc = ObjectProcess.objects.all()[:5]
    context = {"objects_rel":objects_rel, "objectproc":objectproc}
    objectq = request.GET.get('objecthashkey')
    sourcesystemcreatedbyq = request.GET.get('sourcesystemcreatedby')
    sourcesystemcreatedtimeq = request.GET.get('sourcesystemcreatedtime')
    if objectq:
        objectq = objectq.split(',')
        objects_rel = CreateObject.objects.filter(objecthashkey__in=objectq)
        objectproc = ObjectProcess.objects.filter(src_objecthashkey__in=objectq)
        context = {"objects_rel":objects_rel, "objectproc":objectproc}
        return render(request, 'frameworklist.html', context)
    elif sourcesystemcreatedbyq:
        objects_rel = CreateObject.objects.filter(sourcesystemcreatedby=sourcesystemcreatedbyq)
        objectproc = ObjectProcess.objects.filter(sourcesystemcreatedby=sourcesystemcreatedbyq)
        context = {"objects_rel":objects_rel, "objectproc":objectproc}
        return render(request, 'frameworklist.html', context)
    elif sourcesystemcreatedtimeq:
        objects_rel = CreateObject.objects.filter(sourcesystemcreatedtime__contains=sourcesystemcreatedtimeq)
        objectproc = ObjectProcess.objects.filter(sourcesystemcreatedtime__contains=sourcesystemcreatedtimeq)
        context = {"objects_rel":objects_rel, "objectproc":objectproc}
        return render(request, 'frameworklist.html', context)
    # print(objectq, sourcesystemcreatedbyq, sourcesy stemcreatedtimeq)
    # myFilterObjectAll = ObjectAllFilter(request.GET, queryset=objects_rel)
    # print(myFilterObjectAll.get)
    # objects_rel = myFilterObjectAll.qs

    # context = {"objects_rel":objects_rel}

    return render(request, 'frameworklist.html', context)

@login_required(login_url='login')
def frameworkinput(request):
    return render(request, 'frameworkinput.html')

@login_required(login_url='login')
@allowed_users(allowed_user=['adiden', 'testing', 'agrabdur7137'])
def database(request):
    database = Database.objects.all()
    total_database = database.count()
    form = DatabaseForm(initial={'sourcesystemcreatedby': request.user.username})
    myFilter = DatabaseFilter(request.GET, queryset=database)
    print(myFilter)
    database = myFilter.qs

    context = {"database":database, "total_database":total_database, "form":form, "myFilter":myFilter}

    return render(request, 'frameworkinput/database.html', context)

@login_required(login_url='login')
def createDatabase(request):
    
    # form = DatabaseForm(initial={'sourcesystemcreatedby': request.user.username})
    if request.method == 'POST':
        form = DatabaseForm(request.POST, initial={'sourcesystemcreatedby': request.user.username})
        applicationname = request.POST['applicationname']
        databasename = request.POST['databasename']
        databasehashkey = applicationname+databasename

        if Database.objects.filter(databasehashkey=databasehashkey).exists():
            messages.info(request, "Database Already Exists")
            return redirect("database")

        if form.is_valid():
            form.save()
            messages.success(request, "Database Add")
            return redirect("database")
        
    context = {"form":form}
    return render(request, 'frameworkinput/database.html')

@login_required(login_url='login')
def updateDatabase(request, pk):

    database = Database.objects.get(databasehashkey=pk)
    form = DatabaseForm(instance=database)
    
    if request.method == 'POST':
        form = DatabaseForm(request.POST, instance=database)
        if form.is_valid():
            form.save()
            return redirect('database')
            
    context = {'form':form}
    return render(request, 'frameworkinput/update_form.html', context)


@login_required(login_url='login')
def owner(request):
    owner = Owner.objects.all()
    total_owner = owner.count()
    form = OwnerForm(initial={'sourcesystemcreatedby': request.user.username})
    myFilterOwner = OwnerFilter(request.GET, queryset=owner)
    owner = myFilterOwner.qs

    context = {"owner":owner, "total_owner":total_owner, "form":form, "myFilterOwner":myFilterOwner}

    return render(request, 'frameworkinput/owner.html', context)

@login_required(login_url='login')
def createOwner(request):
    
    # form = DatabaseForm(initial={'sourcesystemcreatedby': request.user.username})
    if request.method == 'POST':
        form = OwnerForm(request.POST, initial={'sourcesystemcreatedby': request.user.username})
        ownername = request.POST['ownername']
        ownerhashkey = ownername

        if Owner.objects.filter(ownerhashkey=ownerhashkey).exists():
            messages.info(request, "Owner Already Exists")
            return redirect("owner")

        if form.is_valid():
            form.save()
            messages.success(request, "Owner Add")
            return redirect("owner")
        
    context = {"form":form}
    return render(request, 'frameworkinput/owner.html')

@login_required(login_url='login')
def updateOwner(request, pk):

    owner = Owner.objects.get(ownerhashkey=pk)
    form = OwnerForm(instance=owner)
    
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner')
            
    context = {'form':form}
    return render(request, 'frameworkinput/update_form.html', context)

@login_required(login_url='login')
def storageengine(request):
    storageengine = StorageEngine.objects.all()
    total_storageengine = storageengine.count()
    form = StorageEngineForm(initial={'sourcesystemcreatedby': request.user.username})
    myFilterStorageEngine = StorageEngineFilter(request.GET, queryset=storageengine)
    storageengine = myFilterStorageEngine.qs

    context = {"storageengine":storageengine, "total_storageengine":total_storageengine, "form":form, "myFilterStorageEngine":myFilterStorageEngine}

    return render(request, 'frameworkinput/storageengine.html', context)

@login_required(login_url='login')
def createStorageEngine(request):
    # form = DatabaseForm(initial={'sourcesystemcreatedby': request.user.username})
    if request.method == 'POST':
        form = StorageEngineForm(request.POST, initial={'sourcesystemcreatedby': request.user.username})
        storageenginetype = request.POST['storageenginetype']
        storageenginehashkey = storageenginetype

        if StorageEngine.objects.filter(storageenginehashkey=storageenginehashkey).exists():
            messages.info(request, "Storage Engine Already Exists")
            return redirect("storageengine")

        if form.is_valid():
            form.save()
            messages.success(request, "Storage Engine Add")
            return redirect("storageengine")
        
    context = {"form":form}
    return render(request, 'frameworkinput/storageengine.html')

@login_required(login_url='login')
def updateStorageEngine(request, pk):

    storageengine = StorageEngine.objects.get(storageenginehashkey=pk)
    form = StorageEngineForm(instance=storageengine)

    if request.method == 'POST':
        form = StorageEngineForm(request.POST, instance=storageengine)
        if form.is_valid():
            form.save()
            return redirect('storageengine')
            
    context = {'form':form}
    return render(request, 'frameworkinput/update_form.html', context)


@login_required(login_url='login')
def objecttype(request):
    objecttype = ObjectType.objects.all()
    total_objecttype = objecttype.count()
    form = ObjectTypeForm(initial={'sourcesystemcreatedby': request.user.username})
    myFilterObjectType = ObjectTypeFilter(request.GET, queryset=objecttype)
    objecttype = myFilterObjectType.qs

    context = {"objecttype":objecttype, "total_objecttype":total_objecttype, "form":form, "myFilterObjectType":myFilterObjectType}

    return render(request, 'frameworkinput/objecttype.html', context)

@login_required(login_url='login')
def createObjectType(request):
    # form = DatabaseForm(initial={'sourcesystemcreatedby': request.user.username})
    if request.method == 'POST':
        form = ObjectTypeForm(request.POST, initial={'sourcesystemcreatedby': request.user.username})
        objecttypehashkey = request.POST['objecttype']

        if ObjectType.objects.filter(objecttypehashkey=objecttypehashkey).exists():
            messages.info(request, "Object Type Already Exists")
            return redirect("objecttype")

        if form.is_valid():
            form.save()
            messages.success(request, "Object Type Add")
            return redirect("objecttype")
        
    context = {"form":form}
    return render(request, 'frameworkinput/objecttype.html')

@login_required(login_url='login')
def updateObjectType(request, pk):

    objecttype = ObjectType.objects.get(objecttypehashkey=pk)
    form = ObjectTypeForm(instance=objecttype)

    if request.method == 'POST':
        form = ObjectTypeForm(request.POST, instance=objecttype)
        if form.is_valid():
            form.save()
            return redirect('objecttype')
            
    context = {'form':form}
    return render(request, 'frameworkinput/update_form.html', context)


@login_required(login_url='login')
def partition(request):
    partition = PartitionBy.objects.all()
    total_partition = partition.count()
    form = PartitionByForm(initial={'sourcesystemcreatedby': request.user.username})
    myFilterPartitionBy = PartitionByFilter(request.GET, queryset=partition)
    partition = myFilterPartitionBy.qs

    context = {"partition":partition, "total_partition":total_partition, "form":form, "myFilterPartitionBy":myFilterPartitionBy}

    return render(request, 'frameworkinput/partition.html', context)

@login_required(login_url='login')
def createPartitionBy(request):
    # form = DatabaseForm(initial={'sourcesystemcreatedby': request.user.username})
    if request.method == 'POST':
        form = PartitionByForm(request.POST, initial={'sourcesystemcreatedby': request.user.username})
        partitionby = request.POST['partitionby']

        if PartitionBy.objects.filter(partitionby=partitionby).exists():
            messages.info(request, "Partition Already Exists")
            return redirect("partition")

        if form.is_valid():
            form.save()
            messages.success(request, "Partition Add")
            return redirect("partition")
        
    context = {"form":form}
    return render(request, 'frameworkinput/partition.html')

@login_required(login_url='login')
def updatePartitionBy(request, pk):

    partition = PartitionBy.objects.get(objectpartitionhashkey=pk)
    form = PartitionByForm(instance=partition)

    if request.method == 'POST':
        form = PartitionByForm(request.POST, instance=partition)
        if form.is_valid():
            form.save()
            return redirect('partition')
            
    context = {'form':form}
    return render(request, 'frameworkinput/update_form.html', context)


@login_required(login_url='login')
def snapshot(request):
    snapshot = SnapShot.objects.all()
    total_snapshot = snapshot.count()
    form = SnapShotForm(initial={'sourcesystemcreatedby': request.user.username})
    myFilterSnapShot = SnapShotFilter(request.GET, queryset=snapshot)
    snapshot = myFilterSnapShot.qs

    context = {"snapshot":snapshot, "total_snapshot":total_snapshot, "form":form, "myFilterSnapShot":myFilterSnapShot}

    return render(request, 'frameworkinput/snapshot.html', context)

@login_required(login_url='login')
def createSnapShot(request):
    # form = DatabaseForm(initial={'sourcesystemcreatedby': request.user.username})
    if request.method == 'POST':
        form = SnapShotForm(request.POST, initial={'sourcesystemcreatedby': request.user.username})
        snapshot1 = request.POST['snapshot1']
        snapshot2 = request.POST['snapshot2']

        if (SnapShot.objects.filter(snapshot1=snapshot1).exists()) and (SnapShot.objects.filter(snapshot2=snapshot2).exists()):
            messages.info(request, "Snapshot Already Exists")
            return redirect("snapshot")

        if form.is_valid():
            form.save()
            messages.success(request, "Snapshot Add")
            return redirect("snapshot")
        
    context = {"form":form}
    return render(request, 'frameworkinput/snapshot.html')

@login_required(login_url='login')
def updateSnapShot(request, pk):

    snapshot = SnapShot.objects.get(objectsnapshothashkey=pk)
    form = SnapShotForm(instance=snapshot)

    if request.method == 'POST':
        form = SnapShotForm(request.POST, instance=snapshot)
        if form.is_valid():
            form.save()
            return redirect('snapshot')
            
    context = {'form':form}
    return render(request, 'frameworkinput/update_form.html', context)


@login_required(login_url='login')
def user(request):
    user = ObjectUser.objects.all()
    total_user = user.count()
    form = UserForm(initial={'sourcesystemcreatedby': request.user.username})
    myFilterUser = UserFilter(request.GET, queryset=user)
    user = myFilterUser.qs

    context = {"user":user, "total_user":total_user, "form":form, "myFilterUser":myFilterUser}

    return render(request, 'frameworkinput/user.html', context)

@login_required(login_url='login')
def createUser(request):
    
    # form = DatabaseForm(initial={'sourcesystemcreatedby': request.user.username})
    if request.method == 'POST':
        form = UserForm(request.POST, initial={'sourcesystemcreatedby': request.user.username})
        username = request.POST['username']
        resourcepool = request.POST['resourcepool']
        userhashkey = username+resourcepool

        if ObjectUser.objects.filter(userhashkey=userhashkey).exists():
            messages.info(request, "User Already Exists")
            return redirect("user")

        if form.is_valid():
            form.save()
            messages.success(request, "User Add")
            return redirect("user")
        
    context = {"form":form}
    return render(request, 'frameworkinput/user.html')

@login_required(login_url='login')
def updateUser(request, pk):

    user = ObjectUser.objects.get(userhashkey=pk)
    form = UserForm(instance=user)
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user')
            
    context = {'form':form}
    return render(request, 'frameworkinput/update_form.html', context)


@login_required(login_url='login')
def server(request):
    server = Server.objects.all()
    total_server = server.count()
    form = ServerForm(initial={'sourcesystemcreatedby': request.user.username})
    myFilterServer = ServerFilter(request.GET, queryset=server)
    server = myFilterServer.qs

    context = {"server":server, "total_server":total_server, "form":form, "myFilterServer":myFilterServer}

    return render(request, 'frameworkinput/server.html', context)

@login_required(login_url='login')
def createServer(request):
    # form = DatabaseForm(initial={'sourcesystemcreatedby': request.user.username})
    if request.method == 'POST':
        form = ServerForm(request.POST, initial={'sourcesystemcreatedby': request.user.username})
        serverhashkey = request.POST['servername']

        if Server.objects.filter(serverhashkey=serverhashkey).exists():
            messages.info(request, "Server Already Exists")
            return redirect("server")

        if form.is_valid():
            form.save()
            messages.success(request, "Server Add")
            return redirect("server")
        
    context = {"form":form}
    return render(request, 'frameworkinput/server.html')

@login_required(login_url='login')
def updateServer(request, pk):

    server = Server.objects.get(serverhashkey=pk)
    form = ServerForm(instance=server)

    if request.method == 'POST':
        form = ServerForm(request.POST, instance=server)
        if form.is_valid():
            form.save()
            return redirect('server')
            
    context = {'form':form}
    return render(request, 'frameworkinput/update_form.html', context)


@login_required(login_url='login')
def servertunnel(request):
    servertunnel = ServerTunnel.objects.all()
    total_servertunnel = servertunnel.count()
    form = ServerTunnelForm(initial={'sourcesystemcreatedby': request.user.username})
    myFilterServerTunnel = ServerTunnelFilter(request.GET, queryset=servertunnel)
    servertunnel = myFilterServerTunnel.qs

    context = {"servertunnel":servertunnel, "total_servertunnel":total_servertunnel, "form":form, "myFilterServerTunnel":myFilterServerTunnel}

    return render(request, 'frameworkinput/servertunnel.html', context)

@login_required(login_url='login')
def createServerTunnel(request):
    # form = DatabaseForm(initial={'sourcesystemcreatedby': request.user.username})
    if request.method == 'POST':
        form = ServerTunnelForm(request.POST, initial={'sourcesystemcreatedby': request.user.username})
        servertunnelhashkey = request.POST['servertunnelname']

        if ServerTunnel.objects.filter(servertunnelhashkey=servertunnelhashkey).exists():
            messages.info(request, "ServerTunnel Already Exists")
            return redirect("servertunnel")

        if form.is_valid():
            form.save()
            messages.success(request, "ServerTunnel Add")
            return redirect("servertunnel")
        
    context = {"form":form}
    return render(request, 'frameworkinput/servertunnel.html')

@login_required(login_url='login')
def updateServerTunnel(request, pk):

    servertunnel = ServerTunnel.objects.get(servertunnelhashkey=pk)
    form = ServerTunnelForm(instance=servertunnel)

    if request.method == 'POST':
        form = ServerTunnelForm(request.POST, instance=servertunnel)
        if form.is_valid():
            form.save()
            return redirect('servertunnel')
            
    context = {'form':form}
    return render(request, 'frameworkinput/update_form.html', context)


@login_required(login_url='login')
def files(request):
    fileo = File.objects.all()
    total_file = fileo.count()
    form = FileForm(initial={'sourcesystemcreatedby': request.user.username})
    myFilterFile = FileFilter(request.GET, queryset=fileo)
    fileo = myFilterFile.qs

    context = {"file":fileo, "total_file":total_file, "form":form, "myFilterFile":myFilterFile}

    return render(request, 'frameworkinput/file.html', context)

@login_required(login_url='login')
def createFile(request):
    # form = DatabaseForm(initial={'sourcesystemcreatedby': request.user.username})
    if request.method == 'POST':
        form = FileForm(request.POST, initial={'sourcesystemcreatedby': request.user.username})
        filename = request.POST['filename']
        location = request.POST['location']
        filehashkey = filename+location

        if File.objects.filter(filehashkey=filehashkey).exists():
            messages.info(request, "File Already Exists")
            return redirect("files")

        if form.is_valid():
            form.save()
            messages.success(request, "File Add")
            return redirect("files")
        
    context = {"form":form}
    return render(request, 'frameworkinput/file.html')

@login_required(login_url='login')
def updateFile(request, pk):

    fileo = File.objects.get(filehashkey=pk)
    form = FileForm(instance=fileo)

    if request.method == 'POST':
        form = FileForm(request.POST, instance=fileo)
        if form.is_valid():
            form.save()
            return redirect('files')
            
    context = {'form':form}
    return render(request, 'frameworkinput/update_form.html', context)


@login_required(login_url='login')
def query(request):
    query = Query.objects.all()
    total_query = query.count()
    form = QueryForm(initial={'sourcesystemcreatedby': request.user.username})
    myFilterQuery = QueryFilter(request.GET, queryset=query)
    query = myFilterQuery.qs

    context = {"query":query, "total_query":total_query, "form":form, "myFilterQuery":myFilterQuery}

    return render(request, 'frameworkinput/query.html', context)

@login_required(login_url='login')
def createQuery(request):
    # form = DatabaseForm(initial={'sourcesystemcreatedby': request.user.username})
    if request.method == 'POST':
        form = QueryForm(request.POST, initial={'sourcesystemcreatedby': request.user.username})
        name = request.POST['name']

        if Query.objects.filter(name=name).exists():
            messages.info(request, "Query Already Exists")
            return redirect("query")

        if form.is_valid():
            form.save()
            messages.success(request, "Query Add")
            return redirect("query")
        
    context = {"form":form}
    return render(request, 'frameworkinput/query.html')

@login_required(login_url='login')
def updateQuery(request, pk):

    query = Query.objects.get(queryhashkey=pk)
    form = QueryForm(instance=query)

    if request.method == 'POST':
        form = QueryForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('query')
            
    context = {'form':form}
    return render(request, 'frameworkinput/update_form.html', context)


@login_required(login_url='login')
def process(request):
    process = Process.objects.all()
    total_process = process.count()
    form = ProcessForm(initial={'sourcesystemcreatedby': request.user.username})
    myFilterProcess = ProcessFilter(request.GET, queryset=process)
    process = myFilterProcess.qs

    context = {"process":process, "total_process":total_process, "form":form, "myFilterProcess":myFilterProcess}

    return render(request, 'frameworkinput/process.html', context)

@login_required(login_url='login')
def createProcess(request):
    
    # form = DatabaseForm(initial={'sourcesystemcreatedby': request.user.username})
    if request.method == 'POST':
        form = ProcessForm(request.POST, initial={'sourcesystemcreatedby': request.user.username})
        processdesc = request.POST['processdesc']

        if Process.objects.filter(processdesc=processdesc).exists():
            messages.info(request, "Process Already Exists")
            return redirect("process")

        if form.is_valid():
            form.save()
            messages.success(request, "Process Add")
            return redirect("process")
        
    context = {"form":form}
    return render(request, 'frameworkinput/process.html')

@login_required(login_url='login')
def updateProcess(request, pk):

    process = Process.objects.get(processhashkey=pk)
    form = ProcessForm(instance=process)
    
    if request.method == 'POST':
        form = ProcessForm(request.POST, instance=process)
        if form.is_valid():
            form.save()
            return redirect('process')
            
    context = {'form':form}
    return render(request, 'frameworkinput/update_form.html', context)


@login_required(login_url='login')
def engine(request):
    engine = Engine.objects.all()
    total_engine = engine.count()
    form = EngineForm(initial={'sourcesystemcreatedby': request.user.username})
    myFilterEngine = EngineFilter(request.GET, queryset=engine)
    engine = myFilterEngine.qs

    context = {"engine":engine, "total_engine":total_engine, "form":form, "myFilterEngine":myFilterEngine}

    return render(request, 'frameworkinput/engine.html', context)

@login_required(login_url='login')
def createEngine(request):
    
    # form = DatabaseForm(initial={'sourcesystemcreatedby': request.user.username})
    if request.method == 'POST':
        form = EngineForm(request.POST, initial={'sourcesystemcreatedby': request.user.username})
        enginename = request.POST['enginename']

        if Engine.objects.filter(enginename=enginename).exists():
            messages.info(request, "Engine Already Exists")
            return redirect("engine")

        if form.is_valid():
            form.save()
            messages.success(request, "Engine Add")
            return redirect("engine")
        
    context = {"form":form}
    return render(request, 'frameworkinput/engine.html')

@login_required(login_url='login')
def updateEngine(request, pk):

    engine = Engine.objects.get(enginehashkey=pk)
    form = EngineForm(instance=engine)
    
    if request.method == 'POST':
        form = EngineForm(request.POST, instance=engine)
        if form.is_valid():
            form.save()
            return redirect('engine')
            
    context = {'form':form}
    return render(request, 'frameworkinput/update_form.html', context)


@login_required(login_url='login')
def processengine(request):
    processengine = ProcessEngine.objects.all()
    total_processengine = processengine.count()
    form = ProcessEngineForm(initial={'sourcesystemcreatedby': request.user.username})
    myFilterProcessEngine = ProcessEngineFilter(request.GET, queryset=processengine)
    processengine = myFilterProcessEngine.qs

    context = {
        "processengine":processengine, 
        "total_processengine":total_processengine, 
        "form":form, 
        "myFilterProcessEngine":myFilterProcessEngine
    }

    return render(request, 'frameworkinput/processengine.html', context)

@login_required(login_url='login')
def createProcessEngine(request):
    # form = DatabaseForm(initial={'sourcesystemcreatedby': request.user.username})
    if request.method == 'POST':
        form = ProcessEngineForm(request.POST, initial={'sourcesystemcreatedby': request.user.username})
        processhashkey = request.POST['processhashkey']
        enginehashkey = request.POST['enginehashkey']
        processenginehashkey = processhashkey+enginehashkey

        if ProcessEngine.objects.filter(processenginehashkey=processenginehashkey).exists():
            messages.info(request, "Process Engine Already Exists")
            return redirect("processengine")
        elif Process.objects.filter(processhashkey=processhashkey).exists() == False:
            messages.info(request, "Process Not Exists")
            return redirect("process")
        elif Engine.objects.filter(enginehashkey=enginehashkey).exists() == False:
            messages.info(request, "Engine Not Exists")
            return redirect("engine")

        if form.is_valid():
            form.save()
            messages.success(request, "Process Engine Add")
            return redirect("processengine")
        
    context = {"form":form}
    return render(request, 'frameworkinput/processengine.html')

@login_required(login_url='login')
def updateProcessEngine(request, pk):

    processengine = Processengine.objects.get(processenginehashkey=pk)
    form = ProcessEngineForm(instance=processengine)
    
    if request.method == 'POST':
        form = ProcessEngineForm(request.POST, instance=processengine)
        if form.is_valid():
            form.save()
            return redirect('processengine')
            
    context = {'form':form}
    return render(request, 'frameworkinput/update_form.html', context)


@login_required(login_url='login')
def objects(request):
    objects = Object.objects.all()
    total_object = objects.count()
    myFilterObject = ObjectFilter(request.GET, queryset=objects)
    objects = myFilterObject.qs

    context = {"objects":objects, "total_object":total_object, "myFilterObject":myFilterObject}

    return render(request, 'frameworkinput/objectmanual.html', context)

@login_required(login_url='login')
def createOneObject(request):
    form = ObjectRelationForm(initial={
            'createdby': request.user.username,
        })
    # form = DatabaseForm(initial={'sourcesystemcreatedby': request.user.username})
    if request.method == 'POST':
        form = ObjectRelationForm(request.POST,
                                  initial={
                                        'createdby': request.user.username,
                                    })
        sourcesystemcreatedtime = datetime.now()
        form.is_valid()
        objecthashkey = fcs.addobject(request, form.cleaned_data['objectname'], form.cleaned_data['objectdesc'], form.cleaned_data['sourcesystemcreatedby'], sourcesystemcreatedtime)
        form.cleaned_data['objecthashkey'] = objecthashkey
        form.cleaned_data['sourcesystemcreatedtime'] = sourcesystemcreatedtime
        object_instance = Object.objects.get(objecthashkey=objecthashkey)
        # fcs.inputoneobject(request, object_instance, form)
        try:
            fcs.inputoneobject(request, object_instance, form)
            messages.info(request, "Object {} Success Created".format(str(objecthashkey)))
        except Exception as e:
            print(e)
            messages.info(request, "Error Created Object")
            return redirect("addoneobject")
        if form.is_valid():
            print('Harus Kesini DULU')
            chackpoint_form = form.save(commit=False)
            chackpoint_form.objecthashkey = object_instance
            chackpoint_form.sourcesystemcreatedtime = sourcesystemcreatedtime
            chackpoint_form.save()
            if 'Submit' == request.POST['submit']:
                return redirect("object")
            elif 'Create Another' == request.POST['submit']:
                return redirect("addoneobject")
        
    context = {"form":form}
    return render(request, 'frameworkinput/input_form.html', context)

@login_required(login_url='login')
def generateMultipleRelation(request, pk):

    multiplerelation = MultipleRelation.objects.get(id=pk)
    print(request.method)
    if (request.method == 'POST') and ('Generate' in request.POST) and (multiplerelation.status != 'Generate Success'):
        status = MultipleObject().Main(request, multiplerelation.excel.path)
        multiplerelation.status = status  
        # print(status)      
        if multiplerelation.status == 'Generate Success':
            multiplerelation.status = status
            multiplerelation.save()
            return HttpResponseRedirect(request.path_info)

    elif (request.method == 'POST') and ('Generate' in request.POST) and (multiplerelation.status == 'Generate Success'):
        messages.info(request, "This File Has been Generate")
        return HttpResponseRedirect(request.path_info)
            
    elif (request.method == 'POST') and ('ExitLog' in request.POST):
        messages.info(request, "Multiple Relation {} is Created".format(pk))
        return redirect('multiplerelation')
    
    # context = {'form':form}
    return render(request, 'frameworkinput/processlog.html')


@login_required(login_url='login')
def multiplerelation(request):
    objectmultiple = MultipleRelation.objects.all()
    total_file = objectmultiple.count()
    form = MultipleRelationForm(initial={
            'createdby': request.user.username,
            'filepath' : 'objectrelation/multiple/',
            'status': 'Upload',
        })
    myFilterFile = MultipleRelationFilter(request.GET, queryset=objectmultiple)
    objectmultiple = myFilterFile.qs

    context = {"objectmultiple":objectmultiple, "total_file":total_file, "form":form, "myFilterFile":myFilterFile}

    return render(request, 'frameworkinput/objectmultiple.html', context)

@login_required(login_url='login')
def createMultipleRelation(request):
    # form = DatabaseForm(initial={'sourcesystemcreatedby': request.user.username})
    if request.method == 'POST':
        form = MultipleRelationForm(request.POST, 
                                    request.FILES, initial={
                                        'createdby': request.user.username,
                                        'filename' : request.FILES['excel'],
                                        'filepath' : 'objectrelation/multiple/',
                                        'status': 'Upload',
                                    })
        if form.is_valid():
            # cleaned_data = form.cleaned_data
            chackpoint_form = form.save(commit=False)
            chackpoint_form.filename = request.FILES['excel']
            chackpoint_form.filepath = 'objectrelation/multiple/'
            chackpoint_form.save()
            messages.success(request, "File Object Add")
            return redirect("multiplerelation")
        
    context = {"form":form}
    return render(request, 'frameworkinput/objectmultiple.html')

@login_required(login_url='login')
def generateMultipleRelation(request, pk):

    multiplerelation = MultipleRelation.objects.get(id=pk)
    print(request.method)
    if (request.method == 'POST') and ('Generate' in request.POST) and (multiplerelation.status != 'Generate Success'):
        status = MultipleObject().Main(request, multiplerelation.excel.path)
        multiplerelation.status = status  
        # print(status)      
        if multiplerelation.status == 'Generate Success':
            multiplerelation.status = status
            multiplerelation.save()
            return HttpResponseRedirect(request.path_info)

    elif (request.method == 'POST') and ('Generate' in request.POST) and (multiplerelation.status == 'Generate Success'):
        messages.info(request, "This File Has been Generate")
        return HttpResponseRedirect(request.path_info)
            
    elif (request.method == 'POST') and ('ExitLog' in request.POST):
        messages.info(request, "Multiple Relation {} is Created".format(pk))
        return redirect('multiplerelation')
    
    # context = {'form':form}
    return render(request, 'frameworkinput/processlog.html')


def objectsprocessrelation(request):

    objectprocess = ObjectProcess.objects.all()
    total_objectprocess = objectprocess.count()
    form = ObjectProcesRelationForm(initial={'sourcesystemcreatedby': request.user.username})
    myFilterObjectProcess = ObjectProcessFilter(request.GET, queryset=objectprocess)
    objectprocess = myFilterObjectProcess.qs

    context = {"objectprocess":objectprocess, "total_objectprocess":total_objectprocess, "form":form, "myFilterObjectProcess":myFilterObjectProcess}

    return render(request, 'frameworkinput/objectprocessrelation.html', context)

@login_required(login_url='login')
def createObjectProcessRelation(request):
    form = ObjectProcesRelationForm(initial={
            'GenerateObjectDesc': False,
            'sourcesystemcreatedby': request.user.username,
        })
    # form = DatabaseForm(initial={'sourcesystemcreatedby': request.user.username})
    if request.method == 'POST':
        form = ObjectProcesRelationForm(request.POST,
                                            initial={
                                                    'sourcesystemcreatedby': request.user.username,
                                                })

        src_objecthashkey = request.POST['src_objecthashkey']
        dest_objecthashkey = request.POST['dest_objecthashkey']
        processenginehashkey = request.POST['processenginehashkey']
        objectprocesshashkey = "{}{}{}".format(src_objecthashkey,dest_objecthashkey,processenginehashkey)

        if request.POST.get('GenerateObjectDesc'):
            print("Kesini")
            ManualDesc(request, src_objecthashkey, dest_objecthashkey).mainProcess()
        
        if ObjectProcess.objects.filter(objectprocesshashkey=objectprocesshashkey).exists():
            messages.info(request, "Object Process Already Exists")
            return redirect("objectsprocessrelation")
        elif src_objecthashkey == dest_objecthashkey:
            messages.info(request, "Object Source and Target Same")
            return redirect("objectsprocessrelation")

        if form.is_valid():
            # form.save()
            messages.success(request, "Object Process Add")
            return redirect("objectsprocessrelation")
        
    context = {"form":form}
    return render(request, 'frameworkinput/objectprocess.html', context)

@login_required(login_url='login')
def updateObjectProcessRelation(request, pk):
    objectprocess = ObjectProcess.objects.get(objectprocesshashkey=pk)
    form = ObjectProcess(instance=objectprocess)
    
    if request.method == 'POST':
        form = ObjectProcesRelationForm(request.POST, instance=objectprocess)
        if form.is_valid():
            form.save()
            return redirect('objectsprocessrelation')
            
    context = {'form':form}
    return render(request, 'frameworkinput/update_form.html', context)


def checkmultiple(request):
    form = multipleobjectform
    print(multipleobjectform)
    return redirect('home')


@login_required(login_url='login')
def deleteall(request):
    if request.user.username:
        print(request.user.username)
    if request.method == "POST":
        Object.objects.all().delete()
        Owner.objects.all().delete()
        StorageEngine.objects.all().delete()
        ObjectType.objects.all().delete()
        PartitionBy.objects.all().delete()
        Server.objects.all().delete()
        ServerTunnel.objects.all().delete()
        File.objects.all().delete()
        Database.objects.all().delete()
        SnapShot.objects.all().delete()
        Query.objects.all().delete()
        Process.objects.all().delete()
        Engine.objects.all().delete()
        ProcessEngine.objects.all().delete()
        ObjectUser.objects.all().delete()

        CreateObject.objects.all().delete()

        return redirect('inputframework')
    return render(request, 'delete_all.html')


@login_required(login_url='login')
def objectdesc(request):
    pass