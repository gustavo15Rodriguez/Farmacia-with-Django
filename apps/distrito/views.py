from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView
from apps.distrito.models import Distrito
from apps.distrito.forms import DistritoForm

from django.http import HttpResponse
from django.conf import settings
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors

class ReporteDistritoPDF(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/senasoft.png'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"REPORTE DE DISTRITOS")

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
        encabezado = ('Codigo', 'Nombre del distrito')
        detalle = [(distrito.cod_distrito, distrito.nom_distrito) for distrito in Distrito.objects.all()]
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

class DistritoCrear(CreateView):
    model = Distrito
    form_class = DistritoForm
    template_name = 'distrito/distrito_form.html'
    success_url = reverse_lazy('listar_distrito')

class DistritoListar(ListView):
    model = Distrito
    template_name = 'distrito/distrito_listar.html'

class DistritoEditar(UpdateView):
    model = Distrito
    form_class = DistritoForm
    template_name = 'distrito/distrito_form.html'
    success_url = reverse_lazy('listar_distritos')

class DistritoEliminar(DeleteView):
    model = Distrito
    template_name = 'distrito/distrito_eliminar.html'
    success_url = reverse_lazy('listar_distritos')
