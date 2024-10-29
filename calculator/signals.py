import time
import threading
import logging
from django.dispatch import receiver, Signal
from django.db.models.signals import post_save
from .models import Calculation, Log
operation_done = Signal()

logger = logging.getLogger(__name__)

@receiver(operation_done)
def operation_signal_handler(sender, **kwargs):
    operation = kwargs.get("operation")
    result = kwargs.get("result")
    current_thread = threading.current_thread().name
    #question2
    logger.info(f"Signal handler running in thread: {current_thread}")
    logger.info(f"Operation '{operation}' performed with result: {result}")
    #question1
    time.sleep(5)
    logger.info("Signal processing completed.")


@receiver(post_save, sender=Calculation)
def create_log_on_calculation_save(sender, instance, **kwargs):
    logger.info("Signal handler started.")
    # Create a log entry whenever a Calculation instance is saved
    Log.objects.create(message=f"Calculation performed: {instance.operation}, Result: {instance.result}")
    logger.info("Signal handler completed.")