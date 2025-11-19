from django.urls import path
from .views import AlertsList, AlertDismiss

urlpatterns = [
    path("api/alerts", AlertsList.as_view()),
    path("api/alerts/<str:pk>/dismiss", AlertDismiss.as_view()),
]
