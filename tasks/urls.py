from django.urls import path
from . import views


urlpatterns = [
    
    path('artista/', views.Artista.artista_list, name='artista_list'),
    path('artista/new', views.Artista.artista_create, name='artista_create'),
    path('artista/<int:pk>/edit/', views.Artista.artista_update, name='artista_update'),
    path('artista/<int:pk>/delete/', views.Artista.artista_delete, name='artista_delete'),
   
    path('obra/', views.Obra.obras_list, name='obra_list'),
    path('obra/new/', views.Obra.obras_create, name='obra_create'),
    path('obra/<int:pk>/', views.Obra.obtras_detail, name='obra_detail'),
    path('obra/<int:pk>/edit/', views.Obra.obras_edit, name='obra_edit'),
    path('obra/<int:pk>/delete/', views.Obra.obras_delete, name='obra_delete'),
]
