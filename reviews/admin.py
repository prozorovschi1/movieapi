from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'average_rating')  
    search_fields = ('title',)  
    list_filter = ('release_date', 'average_rating')