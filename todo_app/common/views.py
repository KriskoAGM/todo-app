from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from todo_app.tasks.models import Task

# Create your views here.

def index(request):

    return render(request, '../templates/common/index.html')

@login_required(login_url='login')
def home_page(request):
    all_tasks = Task.objects.filter(user=request.user)

    context = {
        'all_tasks': all_tasks,
    }
    
    return render(request, '../templates/common/home.html', context=context)