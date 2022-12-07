from django.shortcuts import render, redirect
from dotenv import load_dotenv, find_dotenv
import os, requests
from django.http import JsonResponse

load_dotenv(find_dotenv())

TMDB_API_KEY = os.environ.get('TMDB_API_KEY')
# Create your views here.
def movies_search(request, q=None):
    query = request.GET.get('q')
    request.session['query'] = query
    query = request.session['query']
    if query:
        movies_data = requests.get(f"https://api.themoviedb.org/3/search/{request.GET.get('type')}?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={query}").json()
    else:
        return redirect('404')
    # genres = requests.get(f"https://api.themoviedb.org/3/genre/tv/list?api_key={TMDB_API_KEY}")

    return render(request, 'search_result.html', {'data': movies_data, 'query': query, 'type': request.GET.get('type')})

def movie_details(request, movie_id):
    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US")
    return JsonResponse(data.json())
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
