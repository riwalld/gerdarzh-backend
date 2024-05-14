from django.http import HttpResponse
from geriadur_api_django.models import Source
from .dto import SourceDTO
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from dataclasses import asdict
from geriadur_api_django.constants import GenderEnum, WordClassEnum, LanguageEnum

@api_view(['GET'])
def crudSources(request):
    if request.method == 'GET':
        sources = Source.objects.all()
        sourcesDto = []
        for source in sources:
            print(source)
            sourceDtO = SourceDTO(source.source_id ,source.source_name_original, source.abbreviation)
            sourcesDto.append(asdict(sourceDtO))
        response = Response(sourcesDto)
        return response