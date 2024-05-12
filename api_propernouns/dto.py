from dataclasses import dataclass
from typing import List

@dataclass
class ProperNounsDTO:
    currentName: str
    etymoName: str
    #wordStemsPC: List[str]
    descrFr: str
    descrEng: str
    shortDescrFr: str
    shortDescrEng: str
    wordTheme: int
    litTransFr: str
    litTransEng: str
    litTransType: int
    place: str
    country: str
    period: str
    year: int