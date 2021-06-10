from django.urls import path
from PhoneBook import views


urlpatterns=[
    path('display/', views.display, name='display'),
    path('add/', views.add, name='add'),
    path('update/', views.update, name='update')
]