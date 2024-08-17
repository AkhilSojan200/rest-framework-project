from django.urls import path
from . import views



urlpatterns = [

path('student_list/', views.student_list, name='student_list'),
path('student_details/<int:id>/', views.student_details, name='student_details'),
path('student_class_view/', views.student_class_view.as_view()),
path('student_view_details/<int:pk>/', views.student_view_details.as_view()),

]