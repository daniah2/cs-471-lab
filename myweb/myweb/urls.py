from django.contrib import admin
from django.urls import path , include
from django.http import HttpResponse
import apps.bookmodule.views
import apps.usermodule.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('books/', include("apps.bookmodule.urls")),
    path('users/', include("apps.usermodule.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
