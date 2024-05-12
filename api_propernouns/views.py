
from django.http import HttpResponse
from geriadur_api_django.models import Propernoun
from .dto import ProperNounsDTO
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dataclasses import asdict
from geriadur_api_django.constants import GenderEnum, WordClassEnum, LanguageEnum

@api_view(['GET', 'POST'])
def crudProperNouns(request):
    if request.method == 'GET':
        properNouns = Propernoun.objects.all()
        properNounsDTOList = []
        for properNoun in properNouns:
            properNounDto = get_properNoun_dto(properNoun)
            properNounsDTOList.append(asdict(properNounDto))
        return Response(properNounsDTOList)

    elif request.method == 'POST':
        return HttpResponse('This is a POST request')

def get_properNoun_dto(propernoun):
    return ProperNounsDTO(
        currentName = propernoun.current_name,
        etymoName = propernoun.etymo_name,
        #wordStemsPC=propernoun.
        wordTheme = propernoun.word_theme,
        descrFr = propernoun.descr_fr,
        descrEng = propernoun.descr_eng,
        shortDescrFr = propernoun.short_descr_fr,
        shortDescrEng = propernoun.short_descr_eng,
        litTransFr = propernoun.lit_trans.lit_trans_fr if propernoun.lit_trans else None,
        litTransEng = propernoun.lit_trans.lit_trans_eng if propernoun.lit_trans else None,
        litTransType = propernoun.lit_trans.lit_trans_type if propernoun.lit_trans else 0,
        place = propernoun.place,
        country = propernoun.country,
        period = propernoun.period,
        year = propernoun.year
    )