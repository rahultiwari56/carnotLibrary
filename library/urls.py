from django.urls import path
from library import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('search-student/', views.find_student, name='search-student'),
    path('add-student/', views.add_student, name='add-student'),
    path('get-student/<id>/', views.get_student, name='get-student'),
    path('get-data/', views.get_data, name='get-data'),
]
