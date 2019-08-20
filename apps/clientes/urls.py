from django.conf.urls import url
from apps.clientes.views import ClientesCrear, ClientesListar, ClientesEditar, ClientesEliminar, ReporteClientesPDF
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^crear$', login_required(ClientesCrear.as_view()), name='crear_clientes'),
    url(r'^listar$', login_required(ClientesListar.as_view()), name='listar_clientes'),
    url(r'^editar(?P<pk>[\d]+)/$', login_required(ClientesEditar.as_view()), name='editar_clientes'),
    url(r'^eliminar/(?P<pk>[\d]+)/$', login_required(ClientesEliminar.as_view()), name='eliminar_clientes'),
    url(r'^reporte_clientes_pdf/$', login_required(ReporteClientesPDF.as_view()), name='reporte_clientes_pdf'),
]