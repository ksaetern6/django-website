from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {"variable":"CINS 465 Hello World"}
    return render(request,"default.html",context)

def restaurant(request):
    return render(request, "restaurant.html", context)
