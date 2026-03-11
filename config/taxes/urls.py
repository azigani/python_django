from django.urls import path
from . import views

urlpatterns = [
    path('', views.tax_list, name='tax_list'),
    path('create/', views.tax_create, name='tax_create'),
    path('<int:pk>/', views.tax_detail, name='tax_detail'),
    path('<int:pk>/update/', views.tax_update, name='tax_update'),
    path('<int:pk>/delete/', views.tax_delete, name='tax_delete'),
]
