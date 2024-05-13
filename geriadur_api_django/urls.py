
from django.contrib import admin
from . import views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('wordstems/', include('api_wordstems.urls')),
    path('properNouns/', include('api_propernouns.urls')),
    path('sessionGameData/', include('api_sessiongame.urls')),

]
