from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'base.html')

def gallery(request):
    return render(request, 'gallery.html')

def artist(request):
    return render(request, 'artist.html')

def contact(request):
    return render(request, 'contact.html')

def book(request):
    return render(request, 'book.html')

