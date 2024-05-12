from dataclasses import dataclass

@dataclass
class WordstemBasicDTO:
    wordStemName: str
    wordStemLanguage: str
    phonetic: str
    gender: str
    wordClass: str
    engTranslation: str
    frTranslation: str
    semanticField: int
    firstOccurrence: int