from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django_tables2 import RequestConfig

from .models import ServiceUser
from .tables import PersonTable
# Create your views here.

def index(request):
    return render(request, 'OnTheGo/home.html', {'ServiceUser':ServiceUser.objects.all()})

def service_user_page(request):
    path = request.META['PATH_INFO']
    id = int(path.replace('/',''))
    for i in ServiceUser.objects.all():
        print(type(i.id))
        if i.id == id:
            user = i
            break
    return render(request, 'OnTheGo/Service_Users.html', {'x':user})
