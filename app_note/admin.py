from django.contrib import admin
# contains Users and Groups models in admin sites
# Register your models here.
from .models import Topic,Description,Post
admin.site.register(Topic)
admin.site.register(Description)
admin.site.register(Post)




