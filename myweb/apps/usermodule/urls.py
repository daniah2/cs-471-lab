from . import views
from django.urls import path , include

urlpatterns = [
    path('students/city_count/', views.city_count, name='students.city_count'),
]

