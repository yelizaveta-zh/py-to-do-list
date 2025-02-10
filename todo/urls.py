from django.urls import path

from todo.views import (
    toggle_task,
    delete_task,
    tag_list,
    add_tag,
    add_task,
    index,
    delete_tag,
    update_tag,
)

urlpatterns = [
    path("", index, name="index"),
    path("task/<int:task_id>/toggle/", toggle_task, name="toggle-task"),
    path("tasks/add/", add_task, name="add-task"),
    path("task/<int:task_id>/delete/", delete_task, name="delete-task"),
    path("tags/", tag_list, name="tag-list"),
    path("tags/add/", add_tag, name="add-tag"),
    path("tags/<int:tag_id>/delete", delete_tag, name="delete-tag"),
    path("tags/<int:tag_id>/update", update_tag, name="update-tag"),
]

app_name = "todo"
