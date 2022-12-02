from django.shortcuts import render, redirect
from dotenv import load_dotenv, find_dotenv
import os, requests

load_dotenv(find_dotenv())

TMDB_API_KEY = os.environ.get('TMDB_API_KEY')
# Create your views here.
def tv_series_search(request):
    query = request.GET.get('q')
    if query:
        data = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={query}")
    else:
        return redirect('404')
    genres = requests.get(f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}")
    print('GENRES: ', genres.json())
    return render(request, 'search_result.html', {'data':data.json(), 'query': query, 'genres': genres})

# def search_resukt(request):
#     return render(request, 'search_result.html')
def home(request):
    return render(request, 'core/index.html')

def grid_catalog(request):
    return render(request, 'catalog1.html')

def list_catalog(request):
    return render(request, 'catalog2.html')

def movie_details(request):
    return render(request, 'details1.html')

def tv_series_details(request):
    return render(request, 'details2.html')

def pricing_plan(request):
    return render(request, 'pricing.html')

def faq(request):
    return render(request, 'faq.html')

def about(request):
    return render(request, 'about.html')

def error_404(request):
    return render(request, '404.html')
