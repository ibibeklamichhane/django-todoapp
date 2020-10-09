from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    task = Task.objects.all()

    form = TaskForm()

    context = {'task':task,'form':form}
    return render(request,'task/list.html',context)
