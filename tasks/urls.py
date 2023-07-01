from django.urls import path
from . import views


urlpatterns = [
    
    path('project/', views.project.project_list, name='project_list'),
    path('project/new', views.project.project_create, name='project_create'),
    path('project/<int:pk>/edit/', views.project.project_update, name='project_update'),
    path('project/<int:pk>/delete/', views.project.project_delete, name='project_delete'),
   
    path('task/', views.task.task_list, name='task_list'),
    path('task/new/', views.task.task_create, name='task_create'),
    path('task/<int:pk>/', views.task.task_detail, name='task_detail'),
    path('task/<int:pk>/edit/', views.task.task_edit, name='task_edit'),
    path('task/<int:pk>/delete/', views.task.task_delete, name='task_delete'),
]