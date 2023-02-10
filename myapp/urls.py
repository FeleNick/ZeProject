from django.urls import path
from .views import IndexView, TaskView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tasks/', TaskView.as_view(), name='task_view'),
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name='edit_task'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
]