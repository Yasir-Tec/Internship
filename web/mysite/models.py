from django.db import models


# Create your models here.

class user(models.Model):
    departments = (
        ('cse', 'CSE'),
        ('mech', 'MECH'),
        ('civil', 'CIVIL'),
        ('auto', 'AUTO')
    )
    div = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3')

    )
    division = models.CharField(max_length=40, choices=div, blank=True)
    fname = models.CharField(max_length=40, default=True, blank='NOT ALLOTED')
    lname = models.CharField(max_length=40, default=True, blank=True)
    department = models.CharField(max_length=40, choices=departments, null=True)
    email = models.CharField(max_length=50, default=None, blank=True)
    mobile = models.CharField(max_length=50, default=None, blank=True)
    username = models.CharField(max_length=50, default=None, blank=True)
    password = models.CharField(max_length=50, default=None, blank=True)