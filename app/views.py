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

# user dashboard
def dashboarduser(request, pk):
    customer = Customer.objects.get(id=pk)
    bookings = customer.order_set.all()
    context = {
        'customer':customer, 
        'bookings':bookings
    }

    return render(request, 'dashboard-user.html',context)






# artist dashboard
def dashboard(request):
    bookings = Booking.objects.all()
    total_bookings = bookings.count()
    
    context = {
        'bookings':bookings, 
        'total_bookings':total_bookings
    }

    return render(request, 'dashboard-artist.html', context)