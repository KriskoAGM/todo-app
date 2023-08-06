from django import forms

from todo_app.tasks.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']


class DeleteTaskForm(forms.Form):
    pass