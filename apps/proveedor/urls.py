from django.conf.urls import url
from apps.proveedor.views import ProveedorCrear, ProveedorListar, ProveedorEditar, ProveedorEliminar, ReporteProveedorPDF
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^crear$', login_required(ProveedorCrear.as_view()), name='crear_proveedores'),
    url(r'^listar$', login_required(ProveedorListar.as_view()), name='listar_proveedores'),
    url(r'^editar/(?P<pk>[\d]+)/$', login_required(ProveedorEditar.as_view()), name='editar_proveedores'),
    url(r'^eliminar/(?P<pk>[\d]+)/$', login_required(ProveedorEliminar.as_view()), name='eliminar_proveedores'),
    url(r'^reporte_proveedor_pdf/', login_required(ReporteProveedorPDF.as_view()), name='reporte_proveedor_pdf'),
]