
from django.http import HttpResponse
from geriadur_api_django.models import Wordstem
from .dto import WordstemBasicDTO
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dataclasses import asdict
from geriadur_api_django.constants import GenderEnum, WordClassEnum, LanguageEnum

@api_view(['GET', 'POST'])
def crudWordstems(request):
    if request.method == 'GET':
        wordstems = Wordstem.objects.all()
        show_wordstems = []
        for wordstem in wordstems:
            wordstemBasicDto = get_wordstem_basic_dto(wordstem)
            show_wordstems.append(asdict(wordstemBasicDto))
        response = Response(show_wordstems)
        return response

    elif request.method == 'POST':
        return HttpResponse('This is a POST request')

def get_wordstem_basic_dto(ws):
    return WordstemBasicDTO(
        wordStemName=ws.word_stem_name,
        wordStemLanguage= LanguageEnum(ws.word_stem_language).name,
        phonetic=ws.phonetic,
        gender= GenderEnum(ws.gender).name,
        wordClass= WordClassEnum(ws.word_class).name,
        engTranslation=ws.ref_words_eng,
        frTranslation=ws.ref_words_fr,
        semanticField=ws.sem_field.sem_field_name_fr,
        firstOccurrence=ws.first_occurence
    )
