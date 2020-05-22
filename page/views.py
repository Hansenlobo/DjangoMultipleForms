from django.shortcuts import render, redirect
from .forms import TaskForm, TaskaForm
from .models import Task, Taska


def home(request):
    tasks = Task.objects.all()
    tasksa = Taska.objects.all()
    form = TaskForm()
    form1 = TaskaForm()
    if 'btn1' in request.POST:
        form = TaskForm(request.POST)

        if form.is_valid:
            form.save()
            return redirect('/')
    elif 'btn2' in request.POST:
        form1 = TaskaForm(request.POST)
        if form1.is_valid:
            form1.save()
            return redirect('/')
    context = {
        'tasks': tasks,
        'form': form,
        'form1': form1,
        'tasksa': tasksa,
    }
    return render(request, 'page/index.html', context)
