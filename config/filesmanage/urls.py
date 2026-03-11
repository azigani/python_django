from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_list, name='file_list'),
    path('<int:pk>/', views.file_detail, name='file_detail'),
    path('create/', views.file_create, name='file_create'),
    path('<int:pk>/update/', views.file_update, name='file_update'),
    path('<int:pk>/delete/', views.file_delete, name='file_delete'),
]
