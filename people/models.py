from django.db import models

# models for contacts goes here
class Person(models.Model): 
    profile_picture = models. ImageField(blank = True, null = True)
    first = models.CharField(max_length=200, blank = True)
    middle = models.CharField(max_length=200, blank = True)
    last = models.CharField(max_length=200, blank = True)
    header = models.CharField(max_length=300, blank = True)
    birthday = models.DateField(max_length=200, null= True, blank = True)
    phone = models.CharField(max_length=12, blank = True)
    phone2 = models.CharField(max_length=12, blank = True)
    insta = models.CharField(max_length=200, blank = True)
    email  = models.EmailField(max_length=200, null = True, blank = True)
    address = models.CharField(max_length=200, blank = True)
    notes = models.TextField(blank = True)
    prayers = models.TextField(max_length=2000, blank = True)


