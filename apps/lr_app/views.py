# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'lr_templates/index.html')

def register(request):
    results = User.objects.register_validation(request.POST)

    if results[0]:

        request.session['user_id'] = results[1].id
        print "******* You registered yo! ******"
        return redirect("/second_app/success")
    else:
        for err in results[1]:
            messages.error(request, err)
        return redirect('/lr_app')

def login(request):
    results = User.objects.login_validation(request.POST)
    
    if results[0]:
        request.session['user_id'] = results[1].id 
        print "******* logged in yo! ******"
        return redirect("/second_app/success")
    else:
        for err in results[1]:
            messages.error(request, err)
        return redirect('/lr_app')

def logout(request):
    request.session.flush()
    print "++++++++ logged out +++++++++"
    return redirect('/lr_app')