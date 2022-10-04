from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ads.views import *
from avito import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root),
    path('cat/', include('ads.urls.cat_urls')),
    path('ad/', include('ads.urls.ad_urls')),
    path('user/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
