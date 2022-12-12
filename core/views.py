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
    movie = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={TMDB_API_KEY}").json()['results'][0]
    # return JsonResponse(data.json())
    return render(request, 'details1.html', {'data': data.json(), 'movie': movie})


def tv_details(request, tv_id):
    context = {}
    seasons = {}
    data = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}?api_key={TMDB_API_KEY}&language=en-US").json()
    # episodes = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}?api_key=<<api_key>>&language=en-US&append_to_response=all")
    for season in data['seasons']:
        season = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season['season_number']}?api_key={TMDB_API_KEY}&language=en-US").json()
        print('SEASONS: ', seasons)
        seasons[f"{season['season_number']}"] = season
    context['tv_movie'] = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}/videos?api_key={TMDB_API_KEY}").json()['results'][0]
    context['seasons'] = seasons
    context['data'] = data
    return render(request, 'details2.html', context)

def get_latest_movies(request):
    latest_movies = requests.get(f"https://api.themoviedb.org/3/movie/latest?api_key={TMDB_API_KEY}&language=en-US")
    return render(request, 'core/index.html', {'latest_movies': latest_movies})

def get_latest_tv_shows(request):
    latest_tv_shows = requests.get(f"https://api.themoviedb.org/3/tv/latest?api_key={TMDB_API_KEY}&language=en-US")
    return render(request, 'core/index.html', {'latest_tv_shows': latest_tv_shows})

def get_popular_movies(request):
    popular_movies = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=en-US&page=1")
    return render(request, 'core/index.html', {'popular_movies': popular_movies})

def get_popular_tv_shows(request):
    popular_tv_shows = requests.get(f"https://api.themoviedb.org/3/tv/popular?api_key={TMDB_API_KEY}&language=en-US&page=1")
    return render(request, 'core/index.html', {'popular_tv_shows': popular_tv_shows})

def get_animation_movies(request):
    animation_movies = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&language=en-US&sort_by=popularity.desc&page=1&with_genres=16")
    return render(request, 'core/index.html', {'animation_movies': animation_movies})

def get_upcoming_movies(request):
    upcoming_movies = requests.get(f"https://api.themoviedb.org/3/movie/upcoming?api_key={TMDB_API_KEY}&language=en-US&page=1")
    return render(request, 'core/index.html', {'upcoming_movies': upcoming_movies})

def get_upcoming_tv_shows(request):
    upcoming_tv_shows = requests.get(f"https://api.themoviedb.org/3/tv/upcoming?api_key={TMDB_API_KEY}&language=en-US&page=1")
    return render(request, 'core/index.html', {'upcoming_tv_shows': upcoming_tv_shows})

def home(request):
    return render(request, 'core/index.html')

def grid_catalog(request):
    return render(request, 'catalog1.html')

def list_catalog(request):
    return render(request, 'catalog2.html')

def pricing_plan(request):
    return render(request, 'pricing.html')

def faq(request):
    return render(request, 'faq.html')

def about(request):
    return render(request, 'about.html')

def error_404(request):
    return render(request, '404.html')
