from django.urls import path
from library import views

urlpatterns = [
    path('', views.index),
    path('search-student/', views.find_student, name='search-student'),
    path('add-student/', views.add_student, name='add-student'),
    path('get-student/<id>/', views.get_student, name='get-student')
]
