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