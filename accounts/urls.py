from django.urls import include, path
from accounts import views

urlpatterns = [
    
    path('',views.home_view,name='home-view'),
    path('api/students/<int:pk>/', views.StudentDetailAPI.as_view()),
    path('api/teachers/<int:pk>/', views.TeacherDetailAPI.as_view()),
]