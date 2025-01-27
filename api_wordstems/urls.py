from django.urls import path, include
from .views import WordstemsViewSet, WordstemViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"", WordstemsViewSet, basename="word_stems")


urlpatterns = [
    path("", include(router.urls)),
    path("<int:pk>", WordstemViewSet.as_view(), name="create"),
]
