
from dataclasses import dataclass

@dataclass
class PointStruct:
    id: str
    vector: list[float]
    payload: dict