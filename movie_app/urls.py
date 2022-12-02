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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('grid-catalog/', views.grid_catalog, name='grid_catalog'),
    path('list-catalog/', views.list_catalog, name='list_catalog'),
    path('movie-details/', views.movie_details, name='movie_details'),
    path('tv-series-details/', views.tv_series_details, name='tv_series_details'),
    path('pricing-plan/', views.pricing_plan, name='pricing_plan'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about, name='about'),
    path('404/', views.error_404, name='404'),
    path('accounts/', include('accounts.urls', 'accounts')),
    path('core/', include('core.urls', 'core')),
    path('tv-series-search/', views.tv_series_search, name='tv_series_search'),
    path('movies-search/<q>/', views.movies_search, name='movies_search'),
]
