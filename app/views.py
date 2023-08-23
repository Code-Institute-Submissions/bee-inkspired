from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from .forms import BookingForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import * 

def home(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')

def artist(request):
    return render(request, 'artist.html')

def studio(request):
    return render(request, 'studio.html')

# booking flash design appointment page
def book(request):

    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form':form,
    }
    return render(request, 'book.html', context)





def updateBooking(request, pk):

    booking = Booking.objects.get(id=pk)
    form = BookingForm(instance=booking)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {
        'form':form,
    }
    return render(request, 'book.html', context)




def cancelBooking(request, pk):
    booking = Booking.objects.get(id=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('/')
        
    context = {
        'booking':booking
    }
    return render(request, 'delete.html', context)



def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form':form
    }
    return render(request, 'register.html', context)



def login(request):

    context = {

    }
    return render(request, 'login.html', context)









# user dashboard
def client(request, pk):
    customer = Customer.objects.get(id=pk)
    booking = Booking.objects.all()
    bookings = customer.booking_set.all()
    context = {
        'customer':customer,
        'bookings':bookings,
    }
    return render(request, 'dashboard-user.html', context)


# artist dashboard
def dashboard(request):
    bookings = Booking.objects.all()
    total_bookings = bookings.count()
    context = {
        'bookings':bookings, 
        'total_bookings':total_bookings
    }
    return render(request, 'dashboard-artist.html', context)