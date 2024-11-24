from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse

# Create your views here.
def home_view(request:HttpRequest):
    if request.user.is_authenticated:
        print(request.user.username)
    return render(request,"main/home.html")
def about_view(request:HttpRequest):
    return render(request,"main/about.html")
def contact_view(request:HttpRequest):
    return render(request,"main/contact.html")
