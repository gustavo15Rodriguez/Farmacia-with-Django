from django.conf.urls import url
from apps.presentacion.views import PresentacionCrear, PresentacionListar, PresentacionEditar, PresentacionEliminar, ReportePresentacionPDF
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^crear$', login_required(PresentacionCrear.as_view()), name='crear_presentaciones'),
    url(r'^listar$', login_required(PresentacionListar.as_view()), name='listar_presentaciones'),
    url(r'^editar/(?P<pk>[\d]+)/$', login_required(PresentacionEditar.as_view()), name='editar_presentaciones'),
    url(r'^eliminar/(?P<pk>[\d]+)/$', login_required(PresentacionEliminar.as_view()), name='eliminar_presentaciones'),
    url(r'^reporte_presentaciones_pdf/', login_required(ReportePresentacionPDF.as_view()), name='reporte_presentacion_pdf'),
]