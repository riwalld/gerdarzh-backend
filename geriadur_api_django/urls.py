from django.contrib import admin

from geriadur_api_django.settings import ADMIN_URL
from django.urls import path, include
from .views import  GetOneProperNounByNameView, WordstemsViewSet, PropernousAPIView, SourcesAPIView, SemanticFieldsAPIView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("wordstems", WordstemsViewSet, basename="wordstems")

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
]
