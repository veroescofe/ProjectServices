from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.autenticacion.urls')),
    path('accounts/',include('apps.autenticacion.urls')),
    path('cliente/',include("apps.cliente.urls")),
    path('repuesto/',include("apps.repuesto.urls")),
    path('reparacion/',include("apps.reparacion.urls")),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)