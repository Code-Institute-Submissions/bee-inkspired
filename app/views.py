from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import * 
from .forms import *
from .decorators import unauthenticated_user, allowed_users, user_booking

# General nav links
def home(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')

# Booking flash design appointment page
@user_booking
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
@user_booking
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

# Send an enquiry
def userEnquiry(request):
    enquiry = EnquiryForm()
    if request.method == 'POST':
        enquiry = EnquiryForm(request.POST)
        if enquiry.is_valid():
            enquiry.save()
            messages.success(request, 'Thank you, your enquiry has been sent and Olivia will be in touch as soon as possible!')
            return
    context = {
        'enquiry':enquiry,
    }
    return render(request, 'book.html', context)

# Delete an enquiry
# def deleteEnquiry(request, pk):
#     enquiry = Enquiry.objects.get(id=pk)
#     if request.method == 'POST':
#         enquiry.delete()
#         return redirect('dashboard')


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

