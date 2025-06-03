from .config import PipelineConfig, SlackChannel, EmailChannel
import logging

class MonitoringService:
    def __init__(self, config: PipelineConfig):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def start(self):
        # TODO: Consume Kafka events and monitor
        self.logger.info("MonitoringService started")

    def send_alert(self, message: str):
        for channel in self.config.alert_channels:
            if isinstance(channel, SlackChannel):
                self.send_slack_alert(channel.channel_name, message)
            elif isinstance(channel, EmailChannel):
                self.send_email_alert(channel.email, message)

    def send_slack_alert(self, channel_name: str, message: str):
        # TODO: Implement Slack API call
        self.logger.info(f"Slack alert to {channel_name}: {message}")

    def send_email_alert(self, email: str, message: str):
        # TODO: Implement Email sending
        self.logger.info(f"Email alert to {email}: {message}")