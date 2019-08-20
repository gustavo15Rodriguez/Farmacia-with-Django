from django.conf.urls import url
from apps.detalleordenpedido.views import DetallePedidoCrear, DetallePedidoListar, DetallePedidoEditar, DetallePedidoEliminar, ReporteDetallePedidoPDF
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^crear$', login_required(DetallePedidoCrear.as_view()), name='crear_detalles'),
    url(r'^listar$', login_required(DetallePedidoListar.as_view()), name='listar_detalles'),
    url(r'^editar(?P<pk>[\d]+)/$', login_required(DetallePedidoEditar.as_view()), name='editar_detalles'),
    url(r'^eliminar/(?P<pk>[\d]+)/$', login_required(DetallePedidoEliminar.as_view()), name='eliminar_detalles'),
    url(r'^reporte_detalles_pdf/$', login_required(ReporteDetallePedidoPDF.as_view()), name='reporte_detalles_pdf'),
]