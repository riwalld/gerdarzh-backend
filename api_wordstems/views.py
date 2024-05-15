from geriadur_api_django.models import WordStem
from .serializer import WordStemSerializer
from rest_framework import viewsets

class WordstemsViewSet(viewsets.ModelViewSet):
    serializer_class = WordStemSerializer
    #print('show_wordstems')
    
    def get_queryset(self):
        wordstems = WordStem.objects.all()
        return wordstems