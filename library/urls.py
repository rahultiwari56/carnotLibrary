from django.urls import path
from library import views

urlpatterns = [
    path('', views.index),
    path('search-student/', views.find_student),
    path('add-student/', views.add_student),
]
