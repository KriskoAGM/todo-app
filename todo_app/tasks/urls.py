from django.urls import path

from todo_app.tasks import views

urlpatterns = [
    path('add/', views.add_task, name='add-task'),
]