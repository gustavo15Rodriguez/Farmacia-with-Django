from django.conf.urls import url
from apps.distrito.views import DistritoCrear, DistritoListar, DistritoEditar, DistritoEliminar, ReporteDistritoPDF
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^crear$', login_required(DistritoCrear.as_view()), name='crear_distritos'),
    url(r'^listar$', login_required(DistritoListar.as_view()), name='listar_distritos'),
    url(r'^editar/(?P<pk>[\d]+)/$', login_required(DistritoEditar.as_view()), name='editar_distritos'),
    url(r'^eliminar/(?P<pk>[\d]+)/$', login_required(DistritoEliminar.as_view()), name='eliminar_distritos'),
    url(r'^reporte_distritos_pdf/', login_required(ReporteDistritoPDF.as_view()), name='reporte_distrito_pdf'),
]