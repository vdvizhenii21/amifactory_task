from rest_framework import serializers
from .models import Person, Genre, Movie
from drf_extra_fields.fields import Base64ImageField


class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'first_name', 'last_name')
        model = Person


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'title')
        model = Genre
    

class MovieSerializer(serializers.ModelSerializer):

    genre = GenreSerializer(many=True, read_only=True)
    directors = PersonSerializer(many=True, read_only=True)
    writers = PersonSerializer(many=True, read_only=True)
    stars = PersonSerializer(many=True, read_only=True)
    poster = Base64ImageField()
    bg_picture = Base64ImageField()

    class Meta:
        exclude = ('create_date', 'date_updated')
        model = Movie