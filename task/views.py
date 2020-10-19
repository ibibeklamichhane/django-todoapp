from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    task = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'task':task,'form':form}
    return render(request,'task/list.html',context)



def UpdateTask(request,pk):
    tasks=Task.objects.get(id=pk)

    form = TaskForm(instance=tasks)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')

    context= {'form':form}

    return render(request,'task/update_task.html',context)

def DeleteTask(request,pk):

    item=Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()

        context={'item':item}
        return render(request,'task/delete.html',context)



