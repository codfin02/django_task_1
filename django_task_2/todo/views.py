from django.http import Http404
from django.shortcuts import render

from todo.models import Todo


def todo_list(request):
    todos = Todo.objects.all().only('id', 'title').order_by('id')
    context = {'todos': todos}
    return render(request, 'todo_list.html', context)


def todo_info(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
    except Todo.DoesNotExist as exc:
        raise Http404('Todo does not exist') from exc

    context = {'todo': todo}
    return render(request, 'todo_info.html', context)
