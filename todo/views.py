# todo/views.py
from django.shortcuts import render, redirect
from .models import Task

def index(request):
    # Database-la irundhu ella tasks-ahyum yedukurom
    tasks = Task.objects.all().order_by('-created_at')
    
    # User pudhu task add panna ('POST' request)
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('/') # Add panna apram page-ah refresh pannum
        
    return render(request, 'todo/index.html', {'tasks': tasks})

def delete_task(request, task_id):
    # Specific task-ah id moolama kandupidichu delete panrom
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')
