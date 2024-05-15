
from geriadur_api_django.models import SemanticField
from .serializer import SemantiFieldSerializer
from rest_framework import viewsets

class SemanticFieldsViewSet(viewsets.ModelViewSet):
    serializer_class = SemantiFieldSerializer
    #print('show_wordstems')
    
    def get_queryset(self):
        semField = SemanticField.objects.all()
        return semField