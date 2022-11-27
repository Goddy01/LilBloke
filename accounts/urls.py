from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('sent/', views.activation_sent_view, name='activation_sent'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate_account, name='activate'),

]