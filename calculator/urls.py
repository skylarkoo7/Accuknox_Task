from django.urls import path, include
from rest_framework.routers import DefaultRouter
from calculator.views import CalculatorViewSet

router = DefaultRouter()
router.register(r'calculator', CalculatorViewSet, basename='calculator')

urlpatterns = [
    path('', include(router.urls)),
]
