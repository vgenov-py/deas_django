from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("dea", views.index, name="index"),
    path("todoslosdeas", views.todoslosdeas, name = "todoslosdeas"),
    path("comments/", views.comments, name="comments")
]
