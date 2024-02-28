from django.core.management.base import BaseCommand
from movie.models import Movie
import os
import json

class Command(BaseCommand):
    help = 'Load movies from movies.json into the Movie model'
    
    def handle(self, *args, **kwargs):
        #Construct the path to the movies.json file
        #Recuerde que la consola debe estar en la carpeta DjangoProjectBase
        #El path del archivo movie.json con respecto a DjangoProjectBase debe ser
        json_file_path = 'movie/management/commands/movies.json'
        
        #load data from the json file
        with open(json_file_path, 'r') as file:
            movies = json.load(file)
            
        #add products to the database
        for i in range(100):
            movie = movies[i]
            #se asegura que la pelicula no exista en la base de datos
            exist = Movie.objects.filter(title = movie['title']).first()
            if not exist:
                Movie.objects.create(title = movie['title'],
                                        image = 'movie/images/default.jpg',
                                        genre = movie['genre'],
                                        year = movie['year'])
                
                
#self.stdout.write(self.style.SUCCESS(f'Successfully added {cont} products to the database')) #print a success message

#python manage.py add_movies_db