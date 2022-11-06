from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>first view</h1>")
    return render(request, "home.html", {})
    
def about_view(request, *args, **kwargs):
    my_context = {
        "my_text" : "<h2>BIG TEXT</h2>",
        "my_num" : 32211,
        "my_list" : [ 545, 545422, 89978 ]
    }
    return render(request, "about.html", my_context)

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})