from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='task-list'),
    path('create/', views.TaskCreate.as_view(), name='task-create'),
    path('toggle/<str:pk>/', views.toggle_task, name='toggle-task'),
]