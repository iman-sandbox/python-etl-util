from dataclasses import dataclass
from typing import List, Dict, Any, Union
from enum import Enum

class DocumentType(Enum):
    EVENT = 'event'
    INFORMATION = 'information'

@dataclass
class AlertChannel:
    pass

@dataclass
class SlackChannel(AlertChannel):
    channel_name: str

@dataclass
class EmailChannel(AlertChannel):
    email: str

@dataclass
class PipelineConfig:
    schedule_cron: str = "0 0/5 * * * ?"
    alert_failure_threshold: int = 3
    alert_channels: List[AlertChannel] = None
    kafka_config: Dict[str, Any] = None
    elasticsearch_config: Dict[str, Any] = None

    def __post_init__(self):
        if self.alert_channels is None:
            self.alert_channels = [SlackChannel("#alerts")]
        if self.kafka_config is None:
            self.kafka_config = {}
        if self.elasticsearch_config is None:
            self.elasticsearch_config = {}