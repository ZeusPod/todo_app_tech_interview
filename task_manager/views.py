from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from task_manager.models import Task, CityHistory
from .form import TaskForm
from utils.weather_api import get_weather
# Create your views here.


class TaskListView(ListView):
    model = Task    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all().order_by('-created_at').filter(completed=False) 
        return context
    


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_manager/task_detail.html'
    context_object_name = 'task'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = context['task']

        if task.city:
            weather_data = get_weather(task.city)
            if 'error' in weather_data:
                context['weather_error'] = weather_data['error']
            else:
                context['temperature'] = round(weather_data['main']['temp'] - 273.15, 2)
                context['humidity'] = weather_data['main']['humidity']
                context['weather_description'] = weather_data['weather'][0]['description']
        return context

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            if task.city:
                CityHistory.objects.create(task=task, city=task.city, created_at=task.created_at)
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_manager/create_task.html', {'form': form})



def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    context = {'form': form}
    return render(request, 'task_manager/update_task.html', context)





def mark_task_completed(task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task_manager:task_list')


class CityHistoryListView(ListView):
    model = CityHistory
    template_name = 'task_manager/history_city.html'
    context_object_name = 'city_history'