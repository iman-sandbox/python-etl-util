from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from .documents import Document

T = TypeVar('T', bound=Document)

class ExtractionSource(ABC, Generic[T]):
    @abstractmethod
    def extract(self) -> T:
        pass

class KafkaSource(ExtractionSource[T]):
    def __init__(self, topic: str):
        self.topic = topic

    def extract(self) -> T:
        # TODO: Implement Kafka consuming + parsing to Document T
        raise NotImplementedError("Kafka extraction not implemented")

class QueryApiSource(ExtractionSource[T]):
    def __init__(self, url: str):
        self.url = url

    def extract(self) -> T:
        # TODO: Implement REST API call + parsing to Document T
        raise NotImplementedError("Query API extraction not implemented")

class ExtractionSourceFactory:
    @staticmethod
    def create(source_type: str, config: dict) -> ExtractionSource:
        st = source_type.lower()
        if st == 'kafka':
            return KafkaSource(config['topic'])
        elif st == 'queryapi':
            return QueryApiSource(config['url'])
        else:
            raise ValueError(f"Unsupported source type: {source_type}")