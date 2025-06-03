from dataclasses import dataclass
from typing import Dict, Any

class Document:
    pass

@dataclass
class EventDocument(Document):
    timestamp: int
    data: Dict[str, Any]

@dataclass
class InformationDocument(Document):
    id: str
    info: Dict[str, Any]