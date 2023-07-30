from django import forms

from todo_app.tasks.models import Task

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']