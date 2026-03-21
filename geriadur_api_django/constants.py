GENDER_CHOICES = {
  0: "GM",
  1: "GF",
  2: "GN",
  3: "GU",
  4: "NO",
}

WORDCLASS_CHOICES = {
  0: "WN",
  1: "WV",
  2: "WADJ",
  3: "WADV",
  4: "WART",
  5: "WPRN",
  6: "WPREP",
  7: "WCONJ",
  8: "WAF",
}


GENDER_CHOICES_REVERSE = {v: k for k, v in GENDER_CHOICES.items()}
WORDCLASS_CHOICES_REVERSE = {v: k for k, v in WORDCLASS_CHOICES.items()}

def get_keys_by_value(json_obj, target_value):
    for key, value in json_obj.items():
        if value == target_value:
          return key

from enum import Enum

class GenderEnum(Enum):
    GM = 0
    GF = 1
    GN = 2
    GU = 3
    NO = 4
    
    
class LanguageEnum(Enum):
    LB = 0
    LOB = 1
    LBQ = 2
    LC = 3
    LE = 4
    LF = 5
    LG = 6
    LGER = 7
    LIE = 8
    LIR = 9
    LOI = 10
    LS = 11
    LPC = 12
    LW = 13
    LLT = 14
    
class WordClassEnum(Enum):
    WN = 0
    WV = 1
    WADJ = 2
    WADV = 3
    WART = 4
    WPRN = 5
    WPREP = 6
    WCONJ = 7
    WAF = 8