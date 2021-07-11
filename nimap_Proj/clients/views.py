from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from .forms import *
# Create your views here.
from .models import *
def home(request):
    total = Client.objects.all()
    totalp = Project.objects.all()
    totalu = User.objects.all()

    total_clients = total.count()
    total_project = totalp.count()
    total_user = totalu.count()
    context = {'totalp':totalp,'total':total,'total_clients':total_clients,'total_project':total_project,'total_user':total_user}
    return render(request,'clients/dashborad.html',context)

def clients_list(request):
    client = Client.objects.all()
    return render(request,'clients/clients_list.html',{'client':client})

def project_list(request):
    project = Project.objects.all()
    return render(request,'clients/project_list.html',{'project':project})

def CreateClients(request):
    form = ClientForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'clients/client_form.html', context)
def CreateProjects(request):
    form = ProjectForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'clients/project_form.html', context)

def updateProjects(request, pk):

    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'clients/project_form.html', context)

def deleteProject(request, pk):
	project = Project.objects.get(id=pk)
	if request.method == "POST":
		project.delete()
		return redirect('/')

	context = {'item':project}
	return render(request, 'clients/delete.html', context)
def myview(request):
    return render(request,'clients/view.html')