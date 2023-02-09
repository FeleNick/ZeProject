from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView
from .forms import ItemForm, TaskForm, TaskEdit
from .models import Item, Task
 



def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    tasks = Task.objects.filter(user=request.user)
    context = {
        'tasks': tasks
    }
    return render(request, 'myapp/index.html', context)

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'myapp/create.html', context)

def edit_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'myapp/edit.html', context)

def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect('index')

def task_view(request, id=None):
    if id:
        task = get_object_or_404(Task, pk=id)
    else:
        task = Task(user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, initial={'task_name': task.task_name})
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'myapp/task_form.html', {'form': form})

def edit_task(request, id):
    task = get_object_or_404(Task, pk=id)
    form_title = 'Edit Task'
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        form_title = form.fields['task_name'].initial or 'Nope'
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
        
    return render(request, 'myapp/task_edit.html', {'form': form, 'form_title': form_title})

def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('index') 


