from dataclasses import dataclass
from typing import List

@dataclass
class ResponseChoiceDto:
    responseChoice: str
    correctness: bool

@dataclass
class PCelticRadicalDto:
    name: str
    translation: str

@dataclass
class ProperNameDto:
    currentName: str
    etymoName: str
    descr: str
    image: str
    imgCaption: str
    
@dataclass
class GameSessionStepDto:
    proposedLiteralTranslationList: List[ResponseChoiceDto]
    properName: ProperNameDto
    celticRadicals: List[PCelticRadicalDto]