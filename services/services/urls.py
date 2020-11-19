from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.autenticacion.urls')),
    path('accounts/',include('apps.autenticacion.urls')),
    path('cliente/',include("apps.cliente.urls")),
    path('repuesto/',include("apps.repuesto.urls")),
    path('reparacion/',include("apps.reparacion.urls")),
    path('venta/',include("apps.venta.urls")),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)