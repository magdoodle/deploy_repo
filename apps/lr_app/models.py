# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from dateutil.relativedelta import relativedelta
from datetime import datetime
from django.db import models
import bcrypt
import re

# Create your models here.
class UserManager(models.Manager):
    def register_validation(self, postData):
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        errors = []
        if len(postData['name']) < 4:
            errors.append("Your name is too short")
        if len(postData['alias']) < 2:
            errors.append("Your alias is too short")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("You must submit a valid email")
        if len(postData['password']) < 8:
            errors.append("Password must be at least 8 character")
        if postData['password'] != postData['c_password']:
            errors.append("Your passwords do not match")
        try:
            if datetime.strptime(postData["birthdate"], '%Y-%m-%d') > datetime.now() - relativedelta(days=1):
                errors.append("You must be born before today")
        except ValueError: 
            errors.append("Please enter a valid date")

        if len(errors) > 0:
            return (False, errors)
        else:
            hash_pw = bcrypt.hashpw(postData['password'].encode('utf-8'), bcrypt.gensalt())

            u = User.objects.create(name=postData['name'], alias=postData['alias'], email=postData['email'], password=hash_pw, birthdate=postData['birthdate'])
            return (True, u)

    def login_validation(self, postData):

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        errors = []
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("You must submit a valid email")
        if len(postData['password']) < 8:
            errors.append("Your password is too short")

        if len(errors) > 0:
            return (False, errors)
        else:
            u = User.objects.filter(email=postData['email'])
            if u: # check to see if i got a user based on username
                print "found a user", 0
                if bcrypt.checkpw(postData['password'].encode('utf-8'), u[0].password.encode('utf-8')):
                    # if true, username and password matches what is in DB
                    return (True, u[0]) # <User Obj>
                    
                else:
                    errors.append("Password is incorrect") 
                    return(False, errors)
            else:
                print "did not find user"
                errors.append("No user exists with this email.") 
                return(False, errors)


class User(models.Model):
    name = models.CharField(max_length=75)
    alias = models.CharField(max_length=50)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=35)
    birthdate = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
	    return 'name: {}, alias: {}'.format(self.name, self.alias)
