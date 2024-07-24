
from django.shortcuts import render,redirect
from django.http import HttpResponse
#from .models import Departments,Employee,Register,Login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
#from .models import CustomUser


def index(request):
   
    return render(request, 'homepage\index.html')
