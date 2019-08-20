from django.conf.urls import url
from apps.ordenpedido.views import OrdenPedidoCrear, OrdenPedidoListar, OrdenPedidoEditar, OrdenPedidoEliminar, ReporteOrdenPedidoPDF
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^crear$', login_required(OrdenPedidoCrear.as_view()), name='crear_ordenes'),
    url(r'^listar$', login_required(OrdenPedidoListar.as_view()), name='listar_ordenes'),
    url(r'^editar/(?P<pk>[\d]+)/$', login_required(OrdenPedidoEditar.as_view()), name='editar_ordenes'),
    url(r'^eliminar/(?P<pk>[\d]+)/$', login_required(OrdenPedidoEliminar.as_view()), name='eliminar_ordenes'),
    url(r'^reporte_orden_pdf/', login_required(ReporteOrdenPedidoPDF.as_view()), name='reporte_orden_pdf'),
]