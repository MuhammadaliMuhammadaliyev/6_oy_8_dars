from .views import ListCreateView, DetailUpdateDeleteView
from django.urls import path

urlpatterns = [
    path('list-create/', ListCreateView.as_view()),
    path('detail-update-delete/<int:pk>', DetailUpdateDeleteView.as_view()),
]