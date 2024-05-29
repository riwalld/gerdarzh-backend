
from django.urls import path, include
from .views import ProperNounsViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'', ProperNounsViewSet, basename='propernouns')

urlpatterns = [
    path('', include(router.urls)),
]
