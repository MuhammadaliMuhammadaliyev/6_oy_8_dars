from .views import ListView, DetailDeleteUpdate
from django.urls import path

urlpatterns = [
    path('list/', ListView.as_view()),
    path('detail/<int:pk>', DetailDeleteUpdate.as_view()),
    # path('delete/<int:pk>', DeleteView.as_view()),
    # path('update/<int:pk>', UpdateView.as_view()),
    # path('create', ListView.as_view())
]