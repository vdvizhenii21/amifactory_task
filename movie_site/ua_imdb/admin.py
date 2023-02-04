from django.contrib import admin

from .models import Person, Genre, Movie

admin.site.register(Person)
admin.site.register(Genre)
admin.site.register(Movie)
