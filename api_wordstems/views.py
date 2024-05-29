from geriadur_api_django.models import WordStem
from .serializer import WordStemSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class WordstemsViewSet(viewsets.ModelViewSet):
    serializer_class = WordStemSerializer
    #print('show_wordstems')
    
    def get_queryset(self):
        print("testGetAll")
        wordstems = WordStem.objects.all()
        return wordstems
    
    @action(detail=False, methods=['get'], url_path='Str')
    def getProtoCelticStrList(self, request):
        print("testGetPcRadicals")
        pcRadicals = WordStem.objects.all()
        pcRadicalsStr = []
        for radical in pcRadicals:
            pcRadicalsStr.append({"id" :radical.word_stem_id,
                         "name":radical.word_stem_name})
        return Response(pcRadicalsStr)