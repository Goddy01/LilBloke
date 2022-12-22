"""movie_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('grid-catalog/', views.grid_catalog, name='grid_catalog'),
    path('list-catalog/', views.list_catalog, name='list_catalog'),
    # path('movie-details/', views.movie_details, name='movie_details'),
    path('pricing-plan/', views.pricing_plan, name='pricing_plan'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about, name='about'),
    path('404/', views.error_404, name='404'),
    path('accounts/', include('accounts.urls', 'accounts')),
    path('core/', include('core.urls', 'core')),
    path('search/', views.movies_search, name='movies_search'),
    path('movie/<movie_id>/', views.movie_details, name='movie_details'),
    path('tv/<tv_id>/', views.tv_details, name='tv_details'),
    # path('movie/latest/', views.get_latest_movies, name='latest_movies'),
    # path('tv/latest/', views.get_latest_tv_shows, name='latest_tv_shows'),
    path('movies/popular/', views.get_popular_movies, name='get_popular_movies'),
    path('tv_shows/popular/', views.get_popular_tv_shows, name='popular_tv_shows'),
    path('movie/genre/animation/', views.get_animation_movies, name='animation_movies'),
    path('movie/upcoming/', views.get_upcoming_movies, name='upcoming_movies'),
    path('tv/upcoming/', views.get_upcoming_tv_shows, name='upcoming_tv_shows'),
    path('movies-catalog/', views.movies_catalog, name='movies_catalog'),
    path('tv-shows-catalog/', views.tv_shows_catalog, name='tv_shows_catalog'),
    path('movie/<movie_id>/make-comment/', views.movie_make_comment, name='movie_make_comment'),
    path('tv/<tv_id>/make-comment/', views.tv_show_make_comment, name='tv_make_comment'),
    path('movie/add_to_watchlist/<movie_id>/', views.add_to_watchlist_movie, name='add_to_watchlist_movie'),
    path('tv/add_to_watchlist/<tv_id>/', views.add_to_watchlist_tv, name='add_to_watchlist_tv'),
    path('remove_from_watchlist/<movie_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('watchlist/', views.watchlist, name='watchlist'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)