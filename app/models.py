from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Customer model
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

# Tag model
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

# Flash designs model
class Design(models.Model):
    name = models.CharField(max_length=200, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

# Appointment booking model
class Booking(models.Model):
    STATUS = (
        ('booked','booked'),
        ('available','available')
    )
    PREFERENCE = (
        ('radio','radio'),
        ('talking','talking'),
        ('silence','silence'),
        ('not fused','not fused')
    )
    date = models.DateField(default=date.today)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    design = models.ForeignKey(Design, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    preference = models.CharField(max_length=200, null=True, choices=PREFERENCE)