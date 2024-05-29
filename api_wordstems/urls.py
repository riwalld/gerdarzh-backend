
from django.urls import path, include
from .views import WordstemsViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'', WordstemsViewSet, basename='word_stems')



urlpatterns = [
    path('', include(router.urls)),
]
