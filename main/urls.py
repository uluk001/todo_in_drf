from django.urls import path
from main import views

urlpatterns = [
    path('create/', views.CreateToDoView.as_view()),
    path('todos/', views.ListTodoView.as_view()),
    path('retrive/<int:pk>', views.RetrieveTodoView.as_view()),
    path('destroy', views.DestroyTodoView  .as_view()),
]
