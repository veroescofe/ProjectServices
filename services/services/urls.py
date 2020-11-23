from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.autenticacion.urls')),
    path('accounts/',include('apps.autenticacion.urls')),
    path('',include("apps.cliente.urls")),
    path('',include("apps.repuesto.urls")),
    path('',include("apps.reparacion.urls")),
    path('',include("apps.venta.urls")),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)