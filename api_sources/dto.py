from dataclasses import dataclass


@dataclass
class SourceDTO:
    id: int
    sourceOriginalName: str
    name: str
    sourceAbbreviation: str
