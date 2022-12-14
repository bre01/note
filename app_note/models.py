from django.db import models

# Create your models here.
class Topic(models.Model):#inheritance the class Models.Model 
    topic_name=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self): # django use __str__() method as default way to show the basic info
        return self.topic_name


class Description(models.Model):
    text=models.CharField(max_length=200)
    
    date_added=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.text[:10]

class Post(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE) # connetct entry to topic by a "id" key
    title=models.TextField(max_length=50)
    text=models.TextField(max_length=10000,default="why")
    date_added=models.DateTimeField(auto_now_add=True)
    class Meta():
        verbose_name_plural="posts"
    def __str__(self):
        return self.title

