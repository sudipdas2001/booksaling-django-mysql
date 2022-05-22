from django.shortcuts import render

# Create your views here.
def contact(request):
    # return HttpResponse("homw works")
    return render(request, "contact/contact.html")