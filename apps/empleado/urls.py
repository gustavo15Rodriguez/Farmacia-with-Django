from django.conf.urls import url
from apps.empleado.views import EmpleadoCrear, EmpleadoListar, EmpleadoEditar, EmpleadoEliminar, ReporteEmpleadoPDF
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^crear$', login_required(EmpleadoCrear.as_view()), name='crear_empleados'),
    url(r'^listar$', login_required(EmpleadoListar.as_view()), name='listar_empleados'),
    url(r'^editar/(?P<pk>[\d]+)/$', login_required(EmpleadoEditar.as_view()), name='editar_empleados'),
    url(r'^eliminar/(?P<pk>[\d]+)/$', login_required(EmpleadoEliminar.as_view()), name='eliminar_empleados'),
    url(r'^reporte_empleado_pdf/', login_required(ReporteEmpleadoPDF.as_view()), name='reporte_empleado_pdf'),
]