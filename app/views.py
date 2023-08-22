from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

# Create your views here.
from .models import * 

def home(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')

def artist(request):
    return render(request, 'artist.html')

def contact(request):
    return render(request, 'contact.html')

def book(request):
    return render(request, 'book.html')

def login(request):
    return render(request, 'login.html')


def dashboarduser(request):
    bookings = Booking.objects.all()
    # context = {'bookings':bookings}

    return render(request, 'dashboard-user.html', {'bookings':bookings})

def dashboard(request):
    return render(request, 'dashboard-artist.html')