from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views


app_name = 'accounts'
urlpatterns = [
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('sent/', views.activation_sent_view, name='activation_sent'),
    path('activate-account/<slug:uidb64>/<slug:token>/', views.activate_account, name='activate'),
    path('sign-out/', views.sign_out, name='sign_out'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="accounts/password/password_change_done.html"), name="password_change_done"),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password/password_reset_done.html"), name="password_reset_done"),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password/password_reset_complete.html'), name="password_reset_complete"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password/password_reset_form.html', 
        success_url = reverse_lazy('password_reset_complete'),
    ), name="password_reset_confirm"),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password/password_reset.html',
        email_template_name='accounts/password/password_reset_email.html',
        subject_template_name='accounts/password/password_reset_subject.txt',
        success_url = reverse_lazy('password_reset_done'),
    ), name='password_reset'),

]