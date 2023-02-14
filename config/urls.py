from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import static
from django.conf import settings 
from config.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homeapp.urls'))
]

if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)