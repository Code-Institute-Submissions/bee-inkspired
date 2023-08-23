from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Design(models.Model):
    name = models.CharField(max_length=200, null=True)
    tags = models.ManyToManyField(Tag)
    
    def design_range():
        for i in range(1, 19):
            DESIGN = [i]
        design = models.CharField(max_length=200, null=True, choices=DESIGN)

    def __str__(self):
        return self.name


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
    # date =
    # time =
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    design = models.ForeignKey(Design, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    preference = models.CharField(max_length=200, null=True, choices=PREFERENCE)