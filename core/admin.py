from django.contrib import admin
from .models import Comment, Watchlist
# Register your models here.

admin.site.register(Comment)
admin.site.register(Watchlist)