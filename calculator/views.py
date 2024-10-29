import threading
import logging
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from django.db import transaction
from calculator.serializers import CalculationSerializer
from calculator.signals import operation_done

logger = logging.getLogger(__name__)

class CalculatorViewSet(GenericViewSet):
    def get_serializer_class(self):
        if self.action in ("add", "subtract"):
            return CalculationSerializer
        return super().get_serializer_class()

    @action(detail=False, methods=['get'])
    def add(self, request):
        thread_add = threading.current_thread().name
        logger.info(f"Running in thread from views.py: {thread_add}")

        try:
            with transaction.atomic():
                result = 10 + 5
                data = {"operation": "addition", "result": result}
                serializer = self.get_serializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save() 
                operation_done.send(sender=None, operation="addition", result=result)
                raise Exception("Rolling back transaction for testing")
        except Exception as e:
            return Response({"error": str(e)})

    @action(detail=False, methods=['get'])
    def subtract(self, request):
        thread_sub = threading.current_thread().name
        logger.info(f"Running in thread from views.py: {thread_sub}")

        try:
            with transaction.atomic():
                result = 10 - 5
                data = {"operation": "subtraction", "result": result}
                serializer = self.get_serializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save() 
                operation_done.send(sender=None, operation="subtraction", result=result)
                raise Exception("Rolling back transaction for testing")
        except Exception as e:
            return Response({"error": str(e)})
