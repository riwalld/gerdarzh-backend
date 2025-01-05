
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.home),
    path('wordstems/', include('api_wordstems.urls')),
    path('properNouns/', include('api_propernouns.urls')),
    path('sessionGameData/', include('api_sessiongame.urls')),
    path('sources/', include('api_sources.urls')),
    path('semanticFields/', include('api_semanticfield.urls')),
]
