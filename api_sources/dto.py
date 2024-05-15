from dataclasses import dataclass

@dataclass
class SourceDTO:
    sourceId: int
    sourceOriginalName: str
    sourceEngName: str
    sourceAbbreviation: str