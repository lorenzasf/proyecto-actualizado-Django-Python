# from django.contrib import admin
# from django.urls import path, include
# from . import views

# urlpatterns = [
#     path('get/', views.getTask),
#     path('post/', views.postTask),
#     path('put/<int:pk>/', views.putTask),
#     path('delete/<int:pk>/', views.deleteTask)
# ]

from django.contrib import admin
from django.urls import path, include
from .views import GetAllTasksView, GetTasksByUserIDView, task_detail

urlpatterns = [
    path('all/', GetAllTasksView.as_view()),
    path('my-tasks', GetTasksByUserIDView.as_view()),
    path('details/<int:task_id>/', task_detail)
]