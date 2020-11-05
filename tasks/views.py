from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

# Create your views here.
def list_todo_items(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    return render(request, 'tasks/todo_list.html', context)

# why HttpResponse ?
def insert_todo_item(request:HttpResponse):
    todo = Task(title=request.POST['title'])
    todo.save()
    return redirect('/todos/lists/')

def delete_todo_item(request,todo_id):
    todo_to_delete = Task.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/lists/')