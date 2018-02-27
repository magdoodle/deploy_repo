# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..lr_app.models import User

# Create your models here.
class FriendManager(models.Manager):
    def addFriend(self,sender, receiver):
        
		sender = User.objects.get(id=sender)
		receiver = User.objects.get(id=receiver)
		print "***********"
		print "inside FriendManager about to create a friendship"
		print "************"
		existingFriend = Friend.objects.filter(requester=sender, future_friend=receiver)
		if len(existingFriend) > 0:
			existingFriend[0].count += 1
			existingFriend[0].save()
		else:
			Friend.objects.create(requester=sender, future_friend=receiver)
		return "done"

class Friend(models.Model):
    future_friend = models.ForeignKey(User, related_name="friendee")
    requester = models.ForeignKey(User, related_name="friend_requester")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = FriendManager()

    def __str__(self):
	    return 'future_friend: {}, requester: {}'.format(self.future_friend, self.requester)

