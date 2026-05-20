from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_category, name='view_category'),
    path('<int:pk>/', views.view_specific_category, name='view_specific_category'),
]