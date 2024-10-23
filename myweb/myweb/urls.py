from django.contrib import admin
from django.urls import path , include
from django.http import HttpResponse
import apps.bookmodule.views
import apps.usermodule.views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('books/', include("apps.bookmodule.urls")),
    path('users/', include("apps.usermodule.urls"))
]
