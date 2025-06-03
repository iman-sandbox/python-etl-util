import json
from .documents import Document
import logging

class ElasticSearchClient:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def insert(self, document: Document):
        json_doc = json.dumps(document.__dict__)
        self.logger.info(f"Inserting document to Elasticsearch: {json_doc}")
        # TODO: Implement actual ES insert logic here

    def update(self, document: Document):
        json_doc = json.dumps(document.__dict__)
        self.logger.info(f"Updating document in Elasticsearch: {json_doc}")
        # TODO: Implement actual ES update logic here