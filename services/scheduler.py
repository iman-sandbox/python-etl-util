from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import logging

class SchedulerService:
    def __init__(self, cron_expression: str):
        self.cron_expression = cron_expression
        self.scheduler = BackgroundScheduler()
        self.logger = logging.getLogger(__name__)

    def start(self, pipeline):
        trigger = CronTrigger.from_crontab(self.cron_expression)
        self.scheduler.add_job(pipeline.run, trigger)
        self.scheduler.start()
        self.logger.info("Scheduler started")

    def stop(self):
        self.scheduler.shutdown()
        self.logger.info("Scheduler stopped")