from . import views
from django.urls import path, include
from api_propernouns.views import (
    GetOneProperNounByNameView,
    ProperNounsViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"properNouns", ProperNounsViewSet, basename="propernouns")

urlpatterns = [
    path("admin", views.home),
    path("api/", include(router.urls)),
    path(
        "api/properNouns/by-name/<str:name>/",
        GetOneProperNounByNameView.as_view(),
        name="propernoun-by-name",
    ),
    path("api/wordstems/", include("api_wordstems.urls")),
    path("api/sessionGameData/", include("api_sessiongame.urls")),
    path("api/sources/", include("api_sources.urls")),
    path("api/semanticFields/", include("api_semanticfield.urls")),
]
