from django.http import HttpResponse
from django.shortcuts import render

def header(request):
    return render(request,'header.html')

def contect(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'aboutus.html')