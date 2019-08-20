from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
from apps.proveedor.models import Proveedor
from apps.proveedor.forms import ProveedorForm

from django.http import HttpResponse
from django.conf import settings
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors

from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

class ReporteProveedorPDF(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/senasoft.png'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"REPORTE DE PROVEEDORES")

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
        encabezado = ('Codigo', 'Proveedor', 'Direccion', 'Celular', 'Distrito')
        detalle = [(proveedor.cod_proveedor, proveedor.nom_proveedor, proveedor.dir_proveedor, proveedor.celular, proveedor.id_distrito) for proveedor in Proveedor.objects.all()]
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

class ProveedorCrear(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('listar_proveedores')

    @method_decorator(permission_required('proveedor.add_proveedor', reverse_lazy('listar_proveedores')))
    def dispatch(self, request, *args, **kwargs):
        return super(ProveedorCrear, self).dispatch(*args, **kwargs)

class ProveedorListar(ListView):
    model = Proveedor
    template_name = 'proveedor/proveedor_listar.html'

class ProveedorEditar(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('listar_proveedores')

    @method_decorator(permission_required('proveedor.proveedor_permission', reverse_lazy('listar_proveedores')))
    def dispatch(self, request, *args, **kwargs):
        return super(ProveedorEditar, self).dispatch(*args, **kwargs)

class ProveedorEliminar(DeleteView):
    model = Proveedor
    template_name = 'proveedor/proveedor_eliminar.html'
    success_url = reverse_lazy('listar_proveedores')