from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'el usuario ya existe'
                })
    return render(request, 'signup.html', {
        'form': UserCreationForm,
        'error': 'contraseñas no coinciden'
    })


def cerrar(request):
    logout(request)
    return redirect('home')


def entrar(request):
    if request.method == 'GET':
        return render(request, 'entrar.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'entrar.html', {
                'form': AuthenticationForm,
                'error': 'usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('home')


###   view de proyecto   #
from .models import Artista_Model
from .forms import ArtistaForm


class Artista(View):
    # Vista para listar los proyectos
    def artista_list(request):
        artistas = Artista_Model.objects.all()
        return render(request, 'artista/artista_list.html', {'artistas': artistas})

    # Vista para crear un nuevo proyecto
    @login_required
    def artista_create(request):
        if request.method == 'POST':
            form = ArtistaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('artista_list')
        else:
            form = ArtistaForm()
        return render(request, 'artista/artista_form.html', {'form': form})

    # Vista para actualizar un proyecto existente
    @login_required
    def artista_update(request, pk):
        artista = Artista_Model.objects.get(pk=pk)
        if request.method == 'POST':
            form = ArtistaForm(request.POST, instance=artista)
            if form.is_valid():
                form.save()
                return redirect('artista_list')
        else:
            form = ArtistaForm(instance=artista)
        return render(request, 'artista/artista_form.html', {'form': form})

    # Vista para eliminar un proyecto
    def artista_delete(request, pk):
        artista = Artista_Model.objects.get(pk=pk)
        if request.method == 'POST':
            artista.delete()
            return redirect('artista_list')
        return render(request, 'artista/artista_confirm_delete.html', {'artista': artista})


###   view de Obra   #
from .models import Obra_Model
from .forms import ObraForm


class Obra(View):

    # Vista para listar todas las obras
    def obras_list(request):
        obras = Obra_Model.objects.all()
        return render(request, 'obra/obra_list.html', {'obras': obras})

    # Vista para crear una nueva obra
    def obras_create(request):
        if request.method == "POST":
            form = ObraForm(request.POST)
            if form.is_valid():
                obra = form.save(commit=False)
                obra.save()
                return redirect('obra_detail', pk=obra.pk)
        else:
            form = ObraForm()
        return render(request, 'obra/obra_form.html', {'form': form})

    # Vista para ver los detalles de una obra específica
    def obtras_detail(request, pk):
        obra = get_object_or_404(Obra_Model, pk=pk)
        return render(request, 'obra/obra_detail.html', {'obra': obra})

    # Vista para editar una obra existente
    def obras_edit(request, pk):
        obra = get_object_or_404(Obra_Model, pk=pk)
        if request.method == "POST":
            form = ObraForm(request.POST, instance=obra)
            if form.is_valid():
                obra = form.save(commit=False)
                obra.save()
                return redirect('obra_detail', pk=obra.pk)
        else:
            form = ObraForm(instance=obra)
        return render(request, 'obra/obra_form.html', {'form': form})

    # Vista para eliminar una obra existente
    def obras_delete(request, pk):
        obra = get_object_or_404(Obra_Model, pk=pk)
        if request.method == 'POST':
            obra.delete()
            return redirect('obra_list')
        return render(request, 'obra/obra_confirm_delete.html', {'obra': obra})
