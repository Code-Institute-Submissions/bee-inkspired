from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

# Create your views here.
from .models import * 
from .forms import *
from .decorators import unauthenticated_user, allowed_users

# General nav links
def home(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')

# Put next 14 days into a list
def week(days):
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    dates_list = []
    for i in range (0, days):
        x = tomorrow + timedelta(days=i)
        dates_list.append(x.strftime('%Y-%m-%d'))
    return dates_list

# Booking flash design appointment page
@login_required
def book(request):
    dates = week(14)
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer')

    context = {
        'form':form,
        'dates':dates
    }
    return render(request, 'book.html', context)

# Amend flash design appointment 
@login_required
def updateBooking(request, pk):
    booking = Booking.objects.get(id=pk)
    form = BookingForm(instance=booking)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('customer')

    context = {
        'form':form,
    }
    return render(request, 'update-booking.html', context)

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
    bookings = request.user.customer.booking_set.all()
    context = {
        'bookings':bookings, 
    }
    return render(request, 'dashboard-user.html',context)

# Artist dashboard
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    bookings = Booking.objects.all()
    enquiry = Enquiry.objects.all()
    total_bookings = bookings.count()
    enquiry_bookings = enquiry.count()

    context = {
        'bookings':bookings, 
        'total_bookings':total_bookings,
        'enquiry':enquiry,
        'enquiry_bookings':enquiry_bookings
    }
    return render(request, 'dashboard-artist.html', context)