from django.urls import path
from . import views

urlpatterns = [
    path('', views.audit_list, name='audit_list'),
    path('<int:pk>/', views.audit_detail, name='audit_detail'),
    path('create/', views.audit_create, name='audit_create'),
    path('<int:pk>/update/', views.audit_update, name='audit_update'),
    path('<int:pk>/delete/', views.audit_delete, name='audit_delete'),
]
