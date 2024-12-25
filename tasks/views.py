from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task


def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', context={'tasks': tasks})

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'task_form.html', context={'form': TaskForm()})

def update_task(request,pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'task_form.html', context={'form': TaskForm(instance=task)})


def delete_task(request, pk):
    get_object_or_404(Task, pk=pk).delete()
    return redirect('home')

def detail_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', context={'task': task})