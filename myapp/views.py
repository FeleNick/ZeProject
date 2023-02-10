from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ItemForm, TaskForm
from .models import Item, Task


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'myapp/index.html'
    model = Task

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class ItemCreateView(LoginRequiredMixin, CreateView):
    template_name = 'myapp/create.html'
    form_class = ItemForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'myapp/edit.html'
    form_class = ItemForm
    model = Item
    success_url = reverse_lazy('index')


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class TaskView(LoginRequiredMixin, CreateView):
    template_name = 'myapp/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('index')
    model = Task

    def get_initial(self):
        task_name = self.kwargs.get('task_name', '')
        return {'task_name': task_name}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'myapp/task_edit.html'
    form_class = TaskForm
    model = Task
    success_url = reverse_lazy('index')
    

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    


