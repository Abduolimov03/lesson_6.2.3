from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, 'home_page.html')
def home(request):
    return render(request, 'home.html')
def mobile(request):
    return render(request, 'mobile.html')
def mebel(request):
    return render(request, 'mebel.html')