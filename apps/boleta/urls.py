from django.conf.urls import url
from apps.boleta.views import BoletaCrear, BoletaListar, BoletaEditar, BoletaEliminar, ReporteBoletaPDF
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^crear$', login_required(BoletaCrear.as_view()), name='crear_boletas'),
    url(r'^listar$', login_required(BoletaListar.as_view()), name='listar_boletas'),
    url(r'^editar/(?P<pk>[\w]+)/$', login_required(BoletaEditar.as_view()), name='editar_boletas'),
    url(r'^eliminar/(?P<pk>[\w]+)/$', login_required(BoletaEliminar.as_view()), name='eliminar_boletas'),
    url(r'^reporte_boletas_pdf/$', login_required(ReporteBoletaPDF.as_view()), name='reporte_boletas_pdf'),
]