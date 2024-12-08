from django.shortcuts import render
from .models import Student, Address
from django.db.models import Count

# Create your views here.
def city_count(request):
    city_stats = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'usermodule/city_count.html', {'city_stats': city_stats})

