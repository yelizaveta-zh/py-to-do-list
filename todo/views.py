from django.shortcuts import render, redirect, get_object_or_404

from todo.forms import TagForm, TaskForm
from todo.models import Task, Tag


def index(request):
    tasks = Task.objects.all()
    return render(request, "todo/index.html", {"tasks": tasks})


def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_done = not task.is_done
    task.save()
    return redirect("/")


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("/")


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "todo/tag_list.html", {"tags": tags})


def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo:tag-list")
    else:
        form = TagForm()
    return render(request, "todo/tag_form.html", {"form": form})


def delete_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    tag.delete()
    return redirect("todo:tag-list")


def update_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect("todo:tag-list")
        else:
            return redirect("todo:tag-list")
    form = TagForm(instance=tag)
    return render(request, "todo/tag_form.html", {"form": form})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = TaskForm()
    return render(request, "todo/task_form.html", {"form": form})
