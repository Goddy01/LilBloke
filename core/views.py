from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def grid_catalog(request):
    return render(request, 'catalog1.html')

def list_catalog(request):
    return render(request, 'catalog2.html')

def movie_detail(request):
    return render(request, 'details1.html')

def tv_series_detail(request):
    return render(request, 'details2.html')

def pricing(request):
    return render(request, 'pricing.html')

def faq(request):
    return render(request, 'faq.html')

def about(request):
    return render(request, 'about.html')

def error_404(request):
    return render(request, '404.html')