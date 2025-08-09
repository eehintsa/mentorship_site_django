from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='list'),
    path('students/<int:pk>/', views.student_detail, name='detail'),
]
