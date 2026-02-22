from django.contrib import admin

from geriadur_api_django.settings import ADMIN_URL
from django.urls import path, include
from .views import (
    GetOneProperNounByNameView,
    LanguageSetAPIView,
    WordstemAPIView,
    WordstemListAPIView,
    PropernousAPIView,
    SourcesAPIView,
    SemanticFieldsAPIView,
    WordstemStrSetAPIView,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path(ADMIN_URL, admin.site.urls),
    path("api/", include(router.urls)),
    path(
        "api/properNouns/by-name/<str:name>/",
        GetOneProperNounByNameView.as_view(),
        name="propernoun-by-name",
    ),
    path("api/properNouns/", PropernousAPIView.as_view()),
    path("api/sessionGameData/", include("api_sessiongame.urls")),
    path("api/sources/", SourcesAPIView.as_view()),
    path("api/semanticFields/", SemanticFieldsAPIView.as_view()),
    path("api/wordstemList/<str:order>/", WordstemListAPIView.as_view()),
    path("api/wordstem/<int:id>/", WordstemAPIView.as_view()),
    path("api/wordstemstrset/", WordstemStrSetAPIView.as_view()),
    path("api/languages/", LanguageSetAPIView.as_view()),
]
