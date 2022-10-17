from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from ads.views import *
from avito import settings
from users.views import LocationViewSet

router = SimpleRouter()
router.register('location', LocationViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root),
    path('selection/', include('ads.urls.selection_urls')),
#    path('cat/', include('ads.urls.cat_urls')),
    path('ad/', include('ads.urls.ad_urls')),
    path('user/', include('users.urls')),
]
urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
