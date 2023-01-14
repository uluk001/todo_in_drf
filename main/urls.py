from django.urls import path
from main import views

urlpatterns = [
    path('create/', views.CreateToDoView.as_view()),
]
