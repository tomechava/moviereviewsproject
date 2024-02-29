from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64

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

def statistics_view(request):
    matplotlib.use('Agg')
    #obtener todas las peliculas
    all_movies = Movie.objects.all()
    
    
    #PLOT 1: MOVIES PER YEAR
    #crear un diccionario para contar las peliculas por año
    movie_counts_by_year = {}
    
    #filtrar las peliculas por año y contar cuantas peliculas hay por año
    for movie in all_movies:
        year = movie.year if movie.year else "None"
        if year in movie_counts_by_year:
            movie_counts_by_year[year] += 1
        else:
            movie_counts_by_year[year] = 1
    
    #ancho de las barras
    bar_width = 0.5
    #Posicion de las barras
    bar_positions_year = range(len(movie_counts_by_year))
    
    #crear la grafica de barras
    plt.bar(bar_positions_year, movie_counts_by_year.values(), width=bar_width, align='center')
    
    #personalizar la grafica
    plt.title('Movies per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.xticks(bar_positions_year, movie_counts_by_year.keys(), rotation=90)
    
    #ajustar el espaciado entre las barras
    plt.subplots_adjust(bottom=0.3)
    
    #Guardar la grafica en un objeto de tipo BytesIO
    buffer_year = io.BytesIO()
    plt.savefig(buffer_year, format='png')
    buffer_year.seek(0)
    plt.close()
    
    #convertir el objeto de tipo BytesIO a un string base64
    image_png = buffer_year.getvalue()
    buffer_year.close()
    graphic_per_year = base64.b64encode(image_png)
    graphic_per_year = graphic_per_year.decode('utf-8')
    
    
    #PLOT 2: MOVIES PER GENRE
    movie_counts_by_genre = {}
    for movie in all_movies:
        if movie.genre:
            genres = movie.genre.split(",")
            first_genre = genres[0].strip()
            if first_genre in movie_counts_by_genre:
                movie_counts_by_genre[first_genre] += 1
            else:
                movie_counts_by_genre[first_genre] = 1
            
    bar_positions_genre = range(len(movie_counts_by_genre))
    plt.bar(bar_positions_genre, movie_counts_by_genre.values(), width=bar_width, align='center')
    plt.title('Movies per Genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.xticks(bar_positions_genre, movie_counts_by_genre.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.3)

    buffer_genre = io.BytesIO()
    plt.savefig(buffer_genre, format='png')
    buffer_genre.seek(0)
    plt.close()

    graphic_per_genre = base64.b64encode(buffer_genre.getvalue()).decode('utf-8')
    buffer_genre.close()
    
    #renderizar el template con la grafica
    return render(request, 'statistics.html', {'graphic_per_year':graphic_per_year, 'graphic_per_genre':graphic_per_genre})
    

