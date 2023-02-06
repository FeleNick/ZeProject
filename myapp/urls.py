from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('create/', views.create_item, name='create_item'),
    #path('edit/<int:id>/', views.edit_item, name='edit_item'),
    #path('delete/<int:id>/', views.delete_item, name='delete_item'),
    path('tasks/', views.task_view, name='task_view'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
]