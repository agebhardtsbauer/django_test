from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import re
from django.shortcuts import render
from html.parser import HTMLParser


# Create your views here.

def home(request):
    print("http://127.0.0.1:8000/hello/alan") ,
    return render(request, 'hello/home.html')

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def about(request):
    return render(request, 'hello/about.html')

def contact(request):
    return render(request, 'hello/contact.html')