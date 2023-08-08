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


class TaskCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']