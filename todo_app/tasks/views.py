from django.shortcuts import redirect, render

from todo_app.tasks.forms import AddTaskForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user

# Create your views here.

@login_required
def add_task(request):
    form = AddTaskForm(request.POST or None)

    if form.is_valid():
        task = form.save(commit=False)
        task.user = get_user(request)
        task.save()
        return redirect('home')
    
    context = {
        'form': form,
    }

    return render(request, '../templates/tasks/task-create.html', context=context)