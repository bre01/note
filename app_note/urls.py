from django.urls import path
from . import views

app_name = "app_note"
urlpatterns = [
    path('', views.index, name='index'),
    path("topics/", views.topics, name="topics"),
    path("posts/",views.posts,name="posts"),
    path("about/",views.about,name="about"),


    path("topic/<int:topic_id>/", views.topic, name="topic"),
    path("post/<int:entry_id>/", views.post, name="post")
]
