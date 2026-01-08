from .views import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import path

urlpatterns = [
    path('list/', ListView.as_view()),
    path('detail/<int:pk>', DetailView.as_view()),
    path('delete/<int:pk>', DeleteView.as_view()),
    path('update/<int:pk>', UpdateView.as_view()),
    path('create', CreateView.as_view())
]