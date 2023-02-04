from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Type(models.TextChoices):
    DIRECTOR = 'director'
    WRITER = 'writer'
    ACTOR = 'actor'


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    types =  models.CharField(
        max_length=20,
        choices=Type.choices,
    )
    create_date = models.DateTimeField(verbose_name='creation date',
                                       auto_now_add=True,
                                       db_index=True
                                    )
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Genre(models.Model):
    title = models.CharField(max_length=50)
    create_date = models.DateTimeField(
        verbose_name='creation date',
        auto_now_add=True,
        db_index=True
        )
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class Mpa_Rating(models.TextChoices):
    G = 'G'
    PG = 'PG'
    PG13 = 'PG-13'
    R = 'R'
    NC17 = 'NC-17'


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True,max_length=5000)
    poster = models.ImageField(
        upload_to=r'movie_poster/%Y/%m/%d/',
        verbose_name='poster',
        unique=False,
    )
    bg_picture = models.ImageField(
        upload_to=r'movie_bg_picture/%Y/%m/%d/',
        verbose_name='bg_picture',
        unique=False,
    )
    release_year = models.PositiveIntegerField(verbose_name='release year')
    mpa_rating = models.CharField(
        max_length=20,
        choices=Mpa_Rating.choices,
    )
    imdb_rating = models.FloatField(
        verbose_name='score', 
        validators=[MinValueValidator(0), MaxValueValidator(10)]
        )
    duration = models.PositiveIntegerField(verbose_name='duration')
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        related_name='genre_movie',
        )
    directors = models.ManyToManyField(
        Person,
        related_name='movie_directors',

    )
    writers = models.ManyToManyField(
        Person,
        related_name='movie_writers',
    )
    stars = models.ManyToManyField(
        Person,
        related_name='movie_stars',
    )
    create_date = models.DateTimeField(verbose_name='creation date',
                                       auto_now_add=True,
                                       db_index=True
                                    )
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'