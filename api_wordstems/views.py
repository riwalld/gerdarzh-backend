
from django.http import HttpResponse
from geriadur_api_django.models import SemanticField, Source, WordStem
from .dto import WordstemBasicDTO
from .serializer import WordStemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status, viewsets
from dataclasses import asdict
from geriadur_api_django.constants import GenderEnum, WordClassEnum, LanguageEnum
from rest_framework.decorators import action

class WordstemsViewSet(viewsets.ModelViewSet):
    serializer_class = WordStemSerializer
    #print('show_wordstems')
    
    
    def get_queryset(self):
        wordstems = WordStem.objects.all()
        return wordstems
    
    
    """
    def create(self,request):
        print(request.data)
        data = request.data
        serializer = WordStemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

        new_worstem = WordStem.objects.create(
            gender = data['gender'],
            word_class = data['word_class'],
            word_stem_language = data['word_stem_language'],
            word_stem_name = data['word_stem_name'],
            first_occurence = data['first_occurence'],
            sem_field = data['sem_field'],
            descr_eng = data['descr_eng'],
            descr_fr = data['descr_fr'],
            phonetic = data['phonetic'],
            ref_words_eng = data['ref_words_eng'],
            ref_words_fr = data['ref_words_fr'])
        
        new_worstem.save()
        for source in data['sources']:
            source_entity = Source.objects.get(abbreviation=source["abbreviation"])
            new_worstem.sources.add(source_entity)

        serializer = WordStemSerializer(new_worstem)
        return Response(serializer.data)"""