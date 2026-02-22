from rest_framework.response import Response
from geriadur_api_django.dto import SourceDTO
from geriadur_api_django.models import Language, Propernoun
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .serializer import (
    LanguageSerializer,
    MiniWordStemSerializer,
    SemanticFieldSerializer,
    PropernounSerializer,
    WordStemSerializer,
)
from dataclasses import asdict
from geriadur_api_django.models import SemanticField, Source, WordStem
from rest_framework.pagination import PageNumberPagination


class PropernousAPIView(APIView):
    def get(self, request):
        queryset = Propernoun.objects.all().order_by("current_name")
        serializer = PropernounSerializer(queryset, many=True)
        return Response(serializer.data)


class GetOneProperNounByNameView(APIView):
    def get(self, request, name):
        print("teststgeggoesgoien")
        propernoun = Propernoun.objects.filter(current_name=name).first()
        if not propernoun:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PropernounSerializer(propernoun)
        return Response(serializer.data)


class SemanticFieldsAPIView(APIView):
    def get(self, request):
        queryset = SemanticField.objects.all()
        serializer = SemanticFieldSerializer(queryset, many=True)
        return Response(serializer.data)


class SourcesAPIView(APIView):
    def get(self, request):
        sources = Source.objects.all()
        sourcesDto = []
        for source in sources:
            print(source)
            sourceDtO = SourceDTO(
                source.source_id, source.orig_title, source.title, source.abbreviation
            )
            sourcesDto.append(asdict(sourceDtO))
        response = Response(sourcesDto)
        return response


class EpisodePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class WordstemAPIView(APIView):
    def get(self, request, order):
        wordstems = WordStem.objects.all()
        match order:
            case "word":
                wordstems = wordstems.order_by("word_stem_name")
            case "lang":
                wordstems = wordstems.order_by("language")
            case "trans":
                wordstems = wordstems.order_by("fr_translations")
            case "year":
                wordstems = wordstems.order_by("first_occurence")
        paginator = EpisodePagination()
        paginated_qs = paginator.paginate_queryset(wordstems, request)
        serializer = WordStemSerializer(paginated_qs, many=True)
        return paginator.get_paginated_response(serializer.data)


class WordstemStrSetAPIView(APIView):
    def get(self, request):
        wordstems = WordStem.objects.all()
        serializer = MiniWordStemSerializer(wordstems, many=True)
        return Response(serializer.data)

class LanguageSetAPIView(APIView):
    def get(self, request):
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)
    
class ProtoCelticStrAPIView(APIView):
    def get(self, request):
        pcRadicals = WordStem.objects.all()
        pcRadicalsStr = []
        for radical in pcRadicals:
            pcRadicalsStr.append(
                {"id": radical.word_stem_id, "name": radical.word_stem_name}
            )
        return Response(pcRadicalsStr)
