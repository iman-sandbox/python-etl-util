from ..elastic import ElasticSearchClient
import logging

class ReportingService:
    def __init__(self, elastic_client: ElasticSearchClient):
        self.elastic_client = elastic_client
        self.logger = logging.getLogger(__name__)

    def log_pipeline_execution(self, pipeline_name: str, status: str, timestamp: int, metrics: dict):
        # TODO: Push logs/metrics to Elasticsearch
        self.logger.info(f"Logging execution: {pipeline_name}, {status}, {timestamp}, {metrics}")