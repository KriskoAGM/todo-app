import datetime
from django import forms

from todo_app.tasks.models import Task, Priority, Category, Comment

class TaskForm(forms.ModelForm):
    priority = forms.ModelChoiceField(
        queryset=Priority.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Priority'
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='Select a category',
        required=False,
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'category']
    
    def clean_due_date(self):
        due_date = self.cleaned_data['due_date']
        if due_date and due_date < datetime.date.today():
            raise forms.ValidationError("Due date cannot be in the past.")
        return due_date


class TaskCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']