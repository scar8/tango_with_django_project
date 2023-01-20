from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    about_link = '<a href="rango/about/">Click here to go to the about page</a>'
    return HttpResponse("Rango says hey there partner! " + about_link)

def about(request):
    index_link = '<a href="/">Click here to return to the index page</a>'
    return HttpResponse("Rango says here is the about page. " + index_link)
