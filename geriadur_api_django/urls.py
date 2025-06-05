from . import views
from django.urls import path, include


urlpatterns = [
    path("api", views.home),
    path("api/wordstems/", include("api_wordstems.urls")),
    path("api/properNouns/", include("api_propernouns.urls")),
    path("api/sessionGameData/", include("api_sessiongame.urls")),
    path("api/sources/", include("api_sources.urls")),
    path("api/semanticFields/", include("api_semanticfield.urls")),
]
