from django.urls import path

from .views import TaskListView, TaskDetailView, create_task, mark_task_completed, update_task, CityHistoryListView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('create/', create_task, name='create_task'),
    path('update/<int:task_id>/',update_task , name='update_task'),
    path('mark_completed/<int:task_id>/', mark_task_completed, name='mark_task_completed'),
    path('city_history/', CityHistoryListView.as_view(), name='city_history'),
] 