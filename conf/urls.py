from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls', namespace='home')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'conf.views.handler404'
