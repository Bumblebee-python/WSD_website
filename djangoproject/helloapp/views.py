from django.shortcuts import render


# Create your views here.
def homepageview(request):
    return render(request, 'home.html')

def aboutpageview(request):
    return render(request, 'about.html')

def contactpageview(request):
    return render(request, 'contact.html')