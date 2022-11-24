from django.shortcuts import render
from .models import Topic,Post
# Create your views here.
def index(request):
    topics=Topic.objects.order_by("date_added")#it's a list
    posts=Post.objects.order_by("date_added")
    
    context={'topics':topics,"posts":posts} #while context is a dictionary
    return render(request, 'app_note/index.html',context)

def topics(request):
    topics=Topic.objects.order_by("date_added")
    context={"topics":topics}
    return render(request,"app_note/topics.html",context)

def topic(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    posts=topic.post_set.order_by("date_added")
    context={"topic":topic,"posts":posts}
    return render(request,"app_note/topic.html",context)
def posts(request):
    return 0

def post(request,entry_id):
    post=Post.objects.get(id=entry_id)
    
    context={"entry":post}
    return render(request,"app_note/post.html",context)