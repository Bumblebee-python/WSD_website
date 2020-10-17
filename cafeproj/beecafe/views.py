from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def HomePage(request):
    return render(request, 'home.html')

def Aboutus(request):
    return render(request, 'about.html')

def contactus(request):
    return render(request, 'contact.html')

def menulist(request):
    return render(request, 'menu.html')
    