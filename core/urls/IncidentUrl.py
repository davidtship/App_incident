from django.urls import path
from core.views import IncidentAPIView

urlpatterns = [
    path('api/incidents/', IncidentAPIView.as_view(), name='incident-list'),
]
