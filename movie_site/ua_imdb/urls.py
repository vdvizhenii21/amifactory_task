from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet

router_v1 = DefaultRouter()

router_v1.register('movie', MovieViewSet, basename='movie')
router_v1.register('genre', GenreViewSet, basename='genre')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]