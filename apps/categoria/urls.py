from django.conf.urls import url
from apps.categoria.views import CategoriaCrear, CategoriaListar, CategoriaEditar, CategoriaEliminar, ReporteCategoriaPDF
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^crear$', login_required(CategoriaCrear.as_view()), name='crear_categorias'),
    url(r'^listar$', login_required(CategoriaListar.as_view()), name='listar_categorias'),
    url(r'^editar(?P<pk>[\d]+)/$', login_required(CategoriaEditar.as_view()), name='editar_categorias'),
    url(r'^eliminar/(?P<pk>[\d]+)/$', login_required(CategoriaEliminar.as_view()), name='eliminar_categorias'),
    url(r'^reporte_categoria_pdf/$', login_required(ReporteCategoriaPDF.as_view()), name='reporte_categoria_pdf'),
]