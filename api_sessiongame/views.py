
from random import sample, shuffle
from geriadur_api_django.models import Propernoun, LitTrans
from .dto import GameSessionStepDto, PCelticRadicalDto, ProperNameDto
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dataclasses import asdict

@api_view(['GET'])
def getSessionGameData(request):
    properNouns = find_15_proper_nouns_by_word_theme(request.GET.get('wordTheme', None))
    
    sessionGameData = []
    for properNoun in properNouns:
        properNameDto = ProperNameDto(properNoun.current_name, properNoun.etymo_name, properNoun.descr_fr, properNoun.image, properNoun.img_caption)
        proposedLiteralTranslationList = get_5_response_choices(properNoun.lit_trans)
        
        pCelticRadicalList = []
        for wordstemPC in properNoun.wordstempropernoun_set.all():
            
            pCelticRadicalsDto = PCelticRadicalDto(wordstemPC.word_stem.word_stem_name, wordstemPC.word_stem.ref_words_fr)
            pCelticRadicalList.append(pCelticRadicalsDto)

        sessionGameData.append(asdict(GameSessionStepDto(proposedLiteralTranslationList, properNameDto, pCelticRadicalList)))
    return Response(sessionGameData)


def get_5_response_choices(good_lit_trans):
    selected_lit_trans = []
    selected_lit_trans.append({'responseChoice': good_lit_trans.lit_trans_fr, 'correctness': True})

    all_literal_translations = LitTrans.objects.filter(lit_trans_type=good_lit_trans.lit_trans_type)

    # Shuffle the list of literal translations
    all_literal_translations = list(all_literal_translations)
    shuffle(all_literal_translations)

    for literal_trans in all_literal_translations:
        if literal_trans.lit_trans_fr != good_lit_trans.lit_trans_fr:
            selected_lit_trans.append({'responseChoice': literal_trans.lit_trans_fr, 'correctness': False})
        if len(selected_lit_trans) == 5:
            break

    # Shuffle the selected response choices
    shuffle(selected_lit_trans)

    return selected_lit_trans


def find_15_proper_nouns_by_word_theme(word_theme):
    proper_nouns = Propernoun.objects.filter(word_theme=word_theme, confirmed=1)
    return sample(list(proper_nouns), 10)