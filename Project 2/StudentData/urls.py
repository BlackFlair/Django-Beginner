from django.urls import path
from StudentData import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show/', views.index)
]