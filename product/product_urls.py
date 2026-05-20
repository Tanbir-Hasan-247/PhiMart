from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_product, name='view_product'),
    path('<int:id>/', views.view_specific_product, name='view_specific_product'),
]