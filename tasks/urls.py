from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<str:pk>/', views.updateTask, name='updateTask'),
    path('delete_task/<str:pk>/', views.deleteTask, name='deleteTask'),
    path('login/', views.loginPage, name='loginPage')
]
