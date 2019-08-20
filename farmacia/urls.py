"""farmacia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^boleta/', include('apps.boleta.urls')),
    url(r'^categoria/', include('apps.categoria.urls')),
    url(r'^clientes/', include('apps.clientes.urls')),
    url(r'^detalle_orden/', include('apps.detalleordenpedido.urls')),
    url(r'^distrito/', include('apps.distrito.urls')),
    url(r'^empleado/', include('apps.empleado.urls')),
    url(r'^orden/', include('apps.ordenpedido.urls')),
    url(r'^presentacion/', include('apps.presentacion.urls')),
    url(r'^producto/', include('apps.producto.urls')),
    url(r'^proveedor/', include('apps.proveedor.urls')),
    url(r'^usuarios/', include('apps.usuarios.urls')),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^accounts/login/', login, {'template_name': 'index.html'}, name='login'),
    url(r'^reset/password_reset/', password_reset, {'template_name': 'recuperacion/password_reset_form.html', 'email_template_name': 'recuperacion/password_reset_email.html'}, name='password_reset'),
    url(r'^reset/password_done/', password_reset_done, {'template_name': 'recuperacion/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_ \-]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name': 'recuperacion/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/', password_reset_complete, {'template_name': 'recuperacion/password_reset_complete.html'}, name='password_reset_complete'),
    url(r'$', login,  {'template_name': 'index.html'}, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
