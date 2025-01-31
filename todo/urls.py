from django.contrib.sitemaps.views import index
from django.urls import path

from . import views
from .views import home, toggle_task, delete_task, tag_list, add_tag, add_task

urlpatterns = [
    path("", views.home, name="home"),
    path("task/<int:task_id>/toggle/", toggle_task, name="toggle_task"),
    path("task/<int:task_id>/delete/", delete_task, name="delete_task"),
    path("tags/", tag_list, name="tag_list"),
    path("tags/add/", add_tag, name="add_tag"),
    path("tasks/add/", add_task, name="add_task"),
]

app_name = "todo"
