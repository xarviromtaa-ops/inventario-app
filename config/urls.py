from django.contrib import admin
from django.urls import include, path
from inventario.views.home_views import inventario_redirect_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include('inventario.urls.auth_urls')),
    path('', include('inventario.urls.home_urls')),
    path('inventario/', inventario_redirect_view, name='inventario'),
    path('inventario/', include('inventario.urls')),
]
