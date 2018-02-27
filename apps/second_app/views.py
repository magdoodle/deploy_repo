# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..lr_app.models import User
from models import Friend
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def success(request):
    user = User.objects.get(id=request.session["user_id"])
    context = {
        "current_user": user.alias,
        "all_users": User.objects.exclude(id=request.session['user_id']),
    
        # "all_users": User.objects.exclude(friend_requester=request.session['user_id']).exclude(friendee=request.session['user_id']),
       # "all_pokes": Poke.objects.all(),
        #Poke.objects.exclude(poke_receiver=request.session['user_id']),
        "my_friends": Friend.objects.filter(requester=request.session['user_id']),
        "friend_adds": Friend.objects.filter(future_friend=request.session['user_id']),
        #'poke_friends': Poke.objects.filter(poke_receiver=user).order_by("count"),  
        "my_add": Friend.objects.filter(future_friend=request.session['user_id'])
        }
    return render(request, "second_templates/index.html", context)

# def requestadded(request):
#     return render(request, "second_templates/index")

def addFriend(request):
    # p = Poke.objects.get(id=id)
    u = User.objects.get(id=request.session['user_id'])
    print u
    # p.poke_receiver.add(poke_sender)

    # print p.poke_receiver.all()
    #print request.POST['poke_receiver.id']
    Friend.objects.addFriend(sender=request.session['user_id'], receiver=request.POST['future_friend'])
    # results = Poke.objects.get(id=id)
    # context = {
    #     "this_poker": results,
    #     #"this_poker": Poke.objects.get(id=request.session['poke']).poke_sender,
    #     "all_pokees": results.poke_receiver.all()
    #     }
    # print "******** POKES ALL DAY *********!!"
    # print results
    return redirect('/second_app/success')

def profile_info(request, id):
    results = Friend.objects.get(id=id)
    context = {
        "this_friend": results,
        #"item_wishers": Trip.objects.get(id=request.session['trip']).destination,
        #"friends_profile": 
        # "item_wish_owners": results.get(added_by=request.session['user_id']),
        #"item_wishers": Wish.objects.get(item_name="Soccer Ball").wishers.all()
        } 
    print results
    return render(request, 'second_templates/profile.html', context)

def remove_friend(request, id):
    u = User.objects.get(id=request.session['user_id'])
    f = Friend.objects.get(id=id)
    print f
    print id 
    print u
    u.friend_requester.remove(f)
    # print f.friend_requester.all()
    return redirect('/second_app/success')