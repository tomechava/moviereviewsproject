from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    return render(request, 'home.html', {'name': 'Tomas Echavarria'})

def about(request):
    #return HttpResponse('<h1>About Us</h1>')
    return render(request, 'about.html')


