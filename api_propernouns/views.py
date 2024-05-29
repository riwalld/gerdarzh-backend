
from geriadur_api_django.models import Propernoun
from rest_framework import viewsets
from .serializer import PropernounSerializer

class ProperNounsViewSet(viewsets.ModelViewSet):
    serializer_class = PropernounSerializer
    
    def get_queryset(self):
        print("testGetAll")
        propernouns = Propernoun.objects.all()
        return propernouns