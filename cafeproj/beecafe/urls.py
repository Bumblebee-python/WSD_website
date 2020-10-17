from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name= 'home'),
    path('about', views.Aboutus, name= 'contact'),
    path('contact', views.contactus, name= 'contact'),
    path('menu', views.menulist, name= 'contact'),
]