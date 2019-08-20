from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
from apps.empleado.models import Empleado
from apps.empleado.forms import EmpleadoForm

from django.http import HttpResponse
from django.conf import settings
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors

from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

class ReporteEmpleadoPDF(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/senasoft.png'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"REPORTE DE EMPLEADOS")

    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 550
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self, pdf, y):
        encabezado = ('Codigo', 'Nombre', 'Direccion', 'Cargo', 'Edad', 'Celular')
        detalle = [(empleado.cod_empleado, empleado.nom_empleado, empleado.dir_empleado, empleado.cargo, empleado.edad, empleado.celular) for empleado in Empleado.objects.all()]
        detalle_orden = Table([encabezado] + detalle, colWidths=[3.5 *cm, 3.5 *cm, 3.5 *cm, 3.5 *cm])
        detalle_orden.setStyle(TableStyle(
            [
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))

        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60, y)


class EmpleadoCrear(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/empleado_form.html'
    success_url = reverse_lazy('listar_empleados')

    @method_decorator(permission_required('empleado.add_empleado', reverse_lazy('listar_empleados')))
    def dispatch(self, request, *args, **kwargs):
        return super(EmpleadoCrear, self).dispatch(*args, **kwargs)

class EmpleadoListar(ListView):
    model = Empleado
    template_name = 'empleado/empleado_listar.html'

class EmpleadoEditar(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/empleado_form.html'
    success_url = reverse_lazy('listar_empleados')

    @method_decorator(permission_required('empleado.empleado_permission', reverse_lazy('listar_clientes')))
    def dispatch(self, request, *args, **kwargs):
        return super(EmpleadoEditar, self).dispatch(*args, **kwargs)

class EmpleadoEliminar(DeleteView):
    model = Empleado
    template_name = 'empleado/empleado_eliminar.html'
    success_url = reverse_lazy('listar_empleados')