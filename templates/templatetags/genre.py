import requests, os
from django import template
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
register = template.Library()
@register.filter()
def genre(movie_id):
    movie = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={os.environ.get('TMDB_API_KEY')}").json()
    movie_genres = movie['genres']
    genres_list = [g['name'] for g in movie_genres]
    print(genres_list)
    return genres_list
