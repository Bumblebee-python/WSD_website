from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepageview, name = 'homepageview'),
    path('about', views.aboutpageview, name = 'aboutpageview'),
    path('contact', views.contactpageview, name = 'contactpageview'),
]