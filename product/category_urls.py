from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryListCreateView.as_view(), name='view_category'),
    path('<int:pk>/', views.SpecificCategoryView.as_view(), name='view_specific_category'),
]