from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from apps.usuarios.forms import RegistroUsuarioForm

class RegistroUsuario(CreateView):
    model = User
    form_class = RegistroUsuarioForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')