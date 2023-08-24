from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import * 
from .forms import BookingForm, CreateUserForm
from .decorators import unauthenticated_user, allowed_users

# General nav links
def home(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')

# Booking flash design appointment page
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

# Amend flash design appointment 
@login_required(login_url='login')
def updateBooking(request, pk):

    booking = Booking.objects.get(id=pk)
    form = BookingForm(instance=booking)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            if request.user.is_staff:
                return redirect('dashboard')
            else:
                return redirect('customer')


    context = {
        'form':form,
    }
    return render(request, 'book.html', context)

# Cancel flash design appointment 
def cancelBooking(request, pk):
    booking = Booking.objects.get(id=pk)
    if request.method == 'POST':
        booking.delete()
        if request.user.is_staff:
            return redirect('dashboard')
        else:
            return redirect('customer')
        
    context = {
        'booking':booking
    }
    return render(request, 'delete.html', context)

# Register new user
@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Welcome to the family ' + user)
            return redirect('login')
    context = {
        'form':form
    }
    return render(request, 'register.html', context)

# Login user
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_staff:
                return redirect('dashboard')
            else:
                return redirect('customer')
        else:
            messages.info(request, 'Username or password is invalid')
    context = {
    }
    return render(request, 'login.html', context)

# Logout user
def logoutUser(request):
    logout(request)
    return redirect('login')


# User dashboard
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def client(request):
    # customer = Customer.objects.all()
    # booking = Booking.objects.all()
    # bookings = customer.booking_set.all()
    # context = {
    #     'customer':customer,
    #     'bookings':bookings,
    # }
    return render(request, 'dashboard-user.html')

# Artist dashboard
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    # bookings = Booking.objects.all()
    # total_bookings = bookings.count()
    # context = {
    #     'bookings':bookings, 
    #     'total_bookings':total_bookings
    # }
    return render(request, 'dashboard-artist.html')