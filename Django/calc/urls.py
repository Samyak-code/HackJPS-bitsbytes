from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('search',views.search, name='search'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('donate', views.donate, name='donate'),
    path('Form',views.Form, name='Form'),
]


