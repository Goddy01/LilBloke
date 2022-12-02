from django.shortcuts import render, redirect
from dotenv import load_dotenv, find_dotenv
import os, requests

load_dotenv(find_dotenv())

TMDB_API_KEY = os.environ.get('TMDB_API_KEY')
# Create your views here.
def tv_series_search(request, q=None):
    query = request.GET.get('q')
    request.session['query'] = query
    query = request.session['query']
    if query:
        tv_data = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={query}").json()

        movies_data = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={query}").json()
    elif q:
        tv_data = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={q}").json()

        movies_data = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={q}").json()
    else:
        return redirect('404')
    # genres = requests.get(f"https://api.themoviedb.org/3/genre/tv/list?api_key={TMDB_API_KEY}")

    return render(request, 'search_result.html', {'data':tv_data, 'query': query, 'tv_data_count': len(tv_data["results"]), 'movies_data_count': len(movies_data["results"])})

def movies_search(request, q):
    query = request.GET.get('q')
    request.session['query'] = query
    query = request.session['query']
    if query:
        movies_data = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={query}").json()

        tv_data = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={query}").json()
    elif q:
        movies_data = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={q}").json()

        tv_data = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={q}").json()
    else:
        return redirect('404')

    return render(request, 'search_result.html', {'data': movies_data, 'query': query, 'movies_data_count': len(movies_data["results"]), 'tv_data_count': len(tv_data["results"])})

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
