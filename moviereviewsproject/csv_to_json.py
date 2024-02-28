import pandas as pd
import json

#lee el archivo csv
df = pd.read_csv('movies_initial.csv')

#guarda el dataframe en un archivo json
df.to_json('movies_initial.json', orient='records')

with open('movies.json', 'r') as file:
    movies = json.load(file)
    
for i in range(100):
    movie = movies[i]
    print(movie)
    break