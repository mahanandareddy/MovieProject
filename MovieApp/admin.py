from django.contrib import admin
from MovieApp.models import Movies

class MoviesAdmin(admin.ModelAdmin):
    list_display = ['release_date','movie','actor','actress','rating']

admin.site.register(Movies,MoviesAdmin)
