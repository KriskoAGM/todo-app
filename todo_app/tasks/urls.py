from django.urls import path

from todo_app.tasks import views

urlpatterns = [
    path('add/', views.add_task, name='add-task'),
    path('details/<int:pk>/', views.task_details, name='task-details'),
    path('edit/<int:pk>/', views.edit_task, name='edit-task'),
    path('delete/<int:pk>/', views.delete_task, name='delete-task'),
]