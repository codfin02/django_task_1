from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Todo


@login_required
def todo_list(request):
    todos = Todo.objects.filter(owner=request.user).order_by('is_completed', 'due_date')
    context = {'data': todos}
    return render(request, 'todo_list.html', context)


@login_required
def todo_info(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, owner=request.user)
    context = {'todo': todo}
    return render(request, 'todo_detail.html', context)
