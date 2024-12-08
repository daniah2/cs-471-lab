from . import views
from django.urls import path , include

urlpatterns = [
    path('students/', views.list_students, name='list_students'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),

]

