from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
from apps.boleta.models import Boleta
from apps.boleta.forms import BoletaForm

from django.http import HttpResponse
from django.conf import settings
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors

class ReporteBoletaPDF(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/senasoft.png'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"REPORTE DE BOLETAS")

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
        encabezado = ('Numero', 'Fecha', 'Cliente','Subtotal', 'Descuento')
        detalle = [(boleta.num_boleta, boleta.fecha, boleta.cod_cliente, boleta.subtotal, boleta.descuento) for boleta in Boleta.objects.all()]
        detalle_orden = Table([encabezado] + detalle, colWidths=[3 *cm, 3 *cm, 3 *cm, 3 *cm])
        detalle_orden.setStyle(TableStyle(
            [
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))

        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60, y)


class BoletaCrear(CreateView):
    model = Boleta
    form_class = BoletaForm
    template_name = 'boleta/boleta_form.html'
    success_url = reverse_lazy('listar_boletas')

class BoletaListar(ListView):
    model = Boleta
    template_name = 'boleta/boleta_listar.html'

class BoletaEditar(UpdateView):
    model = Boleta
    form_class = BoletaForm
    template_name = 'boleta/boleta_form.html'
    success_url = reverse_lazy('listar_boletas')

class BoletaEliminar(DeleteView):
    model = Boleta
    template_name = 'boleta/boleta_eliminar.html'
    success_url = reverse_lazy('listar_boletas')