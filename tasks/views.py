from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.views import View 
from .forms import TaskForm

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
                'error' : 'usuario o contraseña incorrectos'
            })
        else :
            login(request, user)
            return redirect('home')

###   view de proyecto   #
from .models import Project
from .forms import ProjectForm 

class project(View):
# Vista para listar los proyectos
    def project_list(request):
        projects = Project.objects.all()
        return render(request, 'project/project_list.html', {'projects': projects})

    # Vista para crear un nuevo proyecto
    def project_create(request):
        if request.method == 'POST':
            form = ProjectForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('project_list')
        else:
            form = ProjectForm()
        return render(request, 'project/project_form.html', {'form': form})

    # Vista para actualizar un proyecto existente
    def project_update(request, pk):
        project = Project.objects.get(pk=pk)
        if request.method == 'POST':
            form = ProjectForm(request.POST, instance=project)
            if form.is_valid():
                form.save()
                return redirect('project_list')
        else:
            form = ProjectForm(instance=project)
        return render(request, 'project_form.html', {'form': form})

    # Vista para eliminar un proyecto
    def project_delete(request, pk):
        project = Project.objects.get(pk=pk)
        if request.method == 'POST':
            project.delete()
            return redirect('project_list')
        return render(request, 'project/project_confirm_delete.html', {'project': project})
###   view de Task   #
from .models import Task
from .forms import TaskForm

class task(View):

    # Vista para listar todas las tareas
    def task_list(request):
        tasks = Task.objects.all()
        return render(request, 'task/task_list.html', {'tasks': tasks})

# Vista para crear una nueva tarea
    def task_create(request):
        if request.method == "POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.save()
                return redirect('task_detail', pk=task.pk)
        else:
            form = TaskForm()
        return render(request, 'task/task_form.html', {'form': form})

    # Vista para ver los detalles de una tarea específica
    def task_detail(request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task/task_detail.html', {'task': task})

    # Vista para editar una tarea existente
    def task_edit(request, pk):
        task = get_object_or_404(Task, pk=pk)
        if request.method == "POST":
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                task = form.save(commit=False)
                task.save()
                return redirect('task_detail', pk=task.pk)
        else:
            form = TaskForm(instance=task)
        return render(request, 'task/task_form.html', {'form': form})

    # Vista para eliminar una tarea existente
    def task_delete(request, pk):
        task = get_object_or_404(Task, pk=pk)
        if request.method=='POST':
            task.delete()
            return redirect('task_list')
        return render(request, 'task/task_confirm_delete.html', {'task': task})

