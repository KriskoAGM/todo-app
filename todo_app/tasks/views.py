from django.shortcuts import get_object_or_404, redirect, render

from todo_app.tasks.forms import TaskForm, TaskCommentForm
from todo_app.tasks.models import Task

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user

# Create your views here.


@login_required(login_url='login')
def add_task(request):
    form = TaskForm(request.POST or None)

    if form.is_valid():
        task = form.save(commit=False)
        task.user = get_user(request)
        task.save()
        return redirect('home')

    context = {
        'form': form,
    }

    return render(request, '../templates/tasks/task-create.html', context=context)


@login_required(login_url='login')
def task_details(request, pk):
    task = get_object_or_404(Task, id=pk)

    context = {
        'task': task,
    }

    return render(request, '../templates/tasks/task-details.html', context=context)


@login_required(login_url='login')
def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-details', pk=task.id)
    else:
        form = TaskForm(instance=task)

    context = {
        'form': form,
        'task': task,
    }

    return render(request, '../templates/tasks/task-edit.html', context=context)


@login_required(login_url='login')
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('home')
    
    return render(request, '../templates/tasks/task-delete.html')


@login_required(login_url='login')
def add_comment(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        form = TaskCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.user = request.user
            comment.save()
            return redirect('task-details', pk=task.id)
    else:
        form = TaskCommentForm()
    
    context = {
        'task': task,
        'form': form,
    }

    return render(request, '../templates/tasks/add-comment.html', context=context)


@login_required(login_url='login')
def all_comments(request, pk):
    task = get_object_or_404(Task, id=pk)
    comments = task.comment_set.all()

    context = {
        'task': task,
        'comments': comments,
    }

    return render(request, '../templates/tasks/all-comments.html', context=context)