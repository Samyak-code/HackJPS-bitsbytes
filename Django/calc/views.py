from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html',{'name':'Hello world'})

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def donate(request):
    return render(request, 'donate.html',{'name':'Hello world'})

def Form(request):
    return render(request, 'Form.html',{'name':'Hello world'})


def search(request):
    return HttpResponse('This is a search')