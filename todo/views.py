from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm


class TaskList(TemplateView):
    template_name = 'todo/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_tasks'] = Task.objects(completed=False).order_by('-created_date')
        context['completed_tasks'] = Task.objects(completed=True).order_by('-created_date')
        return context


class TaskCreate(FormView):
    template_name = 'todo/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        Task(title=form.cleaned_data['title']).save()
        return super().form_valid(form)


def toggle_task(request, pk):
    task = Task.objects(id=pk).first()
    if task:
        task.completed = not task.completed
        task.save()
    return redirect('task-list')