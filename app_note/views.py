from django.shortcuts import render
from .models import Topic,Entry
# Create your views here.
def index(request):
    topics=Topic.objects.order_by("date_added")#it's a list
    entries=Entry.objects.order_by("date_added")
    
    context={'topics':topics,"entries":entries} #while context is a dictionary
    return render(request, 'app_note/index.html',context)

def topics(request):
    topics=Topic.objects.order_by("date_added")
    context={"topics":topics}
    return render(request,"app_note/topics.html",context)

def topic(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by("date_added")
    context={"topic":topic,"entries":entries}
    return render(request,"app_note/topic.html",context)