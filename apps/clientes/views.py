from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
from apps.clientes.models import Clientes
from apps.clientes.forms import ClientesForm

from django.http import HttpResponse
from django.conf import settings
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors

from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

class ReporteClientesPDF(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/senasoft.png'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"REPORTE DE CLIENTES")

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
        encabezado = ('Codigo', 'Nombre', 'Direccion', 'Sexo', 'DNI', 'Celular')
        detalle = [(cliente.cod_cliente, cliente.nom_cliente, cliente.sexo, cliente.dni, cliente.celular) for cliente in Clientes.objects.all()]
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


class ClientesCrear(CreateView):
    model = Clientes
    form_class = ClientesForm
    template_name = 'clientes/clientes_form.html'
    success_url = reverse_lazy('listar_clientes')

    @method_decorator(permission_required('clientes.add_clientes', reverse_lazy('listar_clientes')))
    def dispatch(self, *args, **kwargs):
        return super(ClientesCrear, self).dispatch(*args, **kwargs)

class ClientesListar(ListView):
    model = Clientes
    template_name = 'clientes/clientes_listar.html'

class ClientesEditar(UpdateView):
    model = Clientes
    form_class = ClientesForm
    template_name = 'clientes/clientes_form.html'
    success_url = reverse_lazy('listar_clientes')

    @method_decorator(permission_required('clientes.cliente_permission', reverse_lazy('listar_clientes')))
    def dispatch(self, *args, **kwargs):
        return super(ClientesEditar, self).dispatch(*args, **kwargs)

class ClientesEliminar(DeleteView):
    model = Clientes
    template_name = 'clientes/clientes_eliminar.html'
    success_url = reverse_lazy('listar_clientes')