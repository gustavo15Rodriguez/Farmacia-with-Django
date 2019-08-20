from django.conf.urls import url
from apps.producto.views import ProductoCrear, ProductoListar, ProductoEditar, ProductoEliminar, ReporteProductoPDF
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^crear$', login_required(ProductoCrear.as_view()), name='crear_productos'),
    url(r'^listar$', login_required(ProductoListar.as_view()), name='listar_productos'),
    url(r'^editar/(?P<pk>[\d]+)/$', login_required(ProductoEditar.as_view()), name='editar_productos'),
    url(r'^eliminar/(?P<pk>[\d]+)/$', login_required(ProductoEliminar.as_view()), name='eliminar_productos'),
    url(r'^reporte_producto_pdf/', login_required(ReporteProductoPDF.as_view()), name='reporte_producto_pdf'),
]