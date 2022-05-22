from django.shortcuts import render, HttpResponse


# Create your views here.

# Create your views here.


def index(request):
    # return HttpResponse("homw works")
    return render(request, "authencation/home.html")
def login(request):
    # return HttpResponse("homw works")
    return render(request, "authencation/login.html")
def register(request):
    # return HttpResponse("homw works")
    return render(request, "authencation/register.html")