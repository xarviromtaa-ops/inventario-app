from django.urls import path
from inventario.views.auth_views import (
    cuentas_redirect_view,
    login_view,
    logout_view,
    registro_view,
)

urlpatterns = [
    path('', cuentas_redirect_view, name='cuentas'),
    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
