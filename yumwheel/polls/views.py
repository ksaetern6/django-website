from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    context = {"variable":"CINS 465 Hello World"}
    return render(request,"default.html",context)

def restaurant(request):
    context = {"variable":"restaurant name"}
    return render(request, "restaurant.html", context)

def register(request):
    #if we're POSTing information to the website
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #if information of user is valid
        if form.is_valid():
            form.save()
            return(redirect('/login'))

    #else we are GETting the website page
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request,'register.html',args)
