from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from .documents import Document
from .extraction import ExtractionSource
from .elastic import ElasticSearchClient
from .config import DocumentType

T = TypeVar('T', bound=Document)

class Pipeline(ABC, Generic[T]):
    def __init__(self, source: ExtractionSource[T], elastic_client: ElasticSearchClient, document_type: DocumentType):
        self.source = source
        self.elastic_client = elastic_client
        self.document_type = document_type

    @abstractmethod
    def transform(self, input_doc: T) -> T:
        pass

    def run(self):
        extracted = self.source.extract()
        transformed = self.transform(extracted)
        if self.document_type == DocumentType.EVENT:
            self.elastic_client.insert(transformed)
        elif self.document_type == DocumentType.INFORMATION:
            self.elastic_client.update(transformed)