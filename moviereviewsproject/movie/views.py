from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie #import Movie model from models.py

# Create your views here.
def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies':movies})

def about(request):
    #return HttpResponse('<h1>About Us</h1>')
    return render(request, 'about.html')


