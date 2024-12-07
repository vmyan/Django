from django.urls import path
from measurement.views import SensorView, SensorDetailView, MeasurementView

urlpatterns = [
    # Эндпоинт для работы с датчиками: список и создание
    path('sensors/', SensorView.as_view(), name='sensor-list-create'),

    # Эндпоинт для получения и обновления конкретного датчика
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),

    # Эндпоинт для добавления измерения
    path('measurements/', MeasurementView.as_view(), name='measurement-create'),
]
