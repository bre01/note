from django.urls import path
from . import views 
app_name="app_note"
urlpatterns=[
    path('',views.index,name='index'),
    path("topics",views.topics,name="topics"),
    path("topic/<int:topic_id>/",views.topic,name="topic"),
    path("posts/<int:entry_id>/",views.post,name="post")
]