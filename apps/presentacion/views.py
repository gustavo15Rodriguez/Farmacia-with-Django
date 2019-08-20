from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
from apps.presentacion.models import Presentacion
from apps.presentacion.forms import PresentacionForm

from django.http import HttpResponse
from django.conf import settings
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors

class ReportePresentacionPDF(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/senasoft.png'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"REPORTE DE LAS PRRESENTACIONES")

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
        encabezado = ('Codigo', 'Nombre')
        detalle = [(presentacion.cod_presentacion, presentacion.nom_presentacion) for presentacion in Presentacion.objects.all()]
        detalle_orden = Table([encabezado] + detalle, colWidths=[4 *cm, 4 *cm, 4 *cm, 4 *cm])
        detalle_orden.setStyle(TableStyle(
            [
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))

        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60, y)


class PresentacionCrear(CreateView):
    model = Presentacion
    form_class = PresentacionForm
    template_name = 'presentacion/presentacion_form.html'
    success_url = reverse_lazy('listar_presentaciones')

class PresentacionListar(ListView):
    model = Presentacion
    template_name = 'presentacion/presentacion_listar.html'

class PresentacionEditar(UpdateView):
    model = Presentacion
    form_class = PresentacionForm
    template_name = 'presentacion/presentacion_form.html'
    success_url = reverse_lazy('listar_presentaciones')

class PresentacionEliminar(DeleteView):
    model = Presentacion
    template_name = 'presentacion/presentacion_eliminar.html'
    success_url = reverse_lazy('listar_presentaciones')