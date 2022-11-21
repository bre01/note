from django.shortcuts import render
from .models import Topic
# Create your views here.
def index(request):
    return render(request, 'app_note/index.html')