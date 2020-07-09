# views.py
from django.shortcuts import render, redirect
from django.conf import settings

def index(request):
    if request.user.is_authenticated:           
        return render(request,'index.html')
    else:
        return redirect('/inventory%s?next=%s' % (settings.LOGIN_URL, request.path))
        