from django.db import models

# Create your models here.
class Topic(models.Model):#inheritance the class Models.Model 
    topic_name=models.CharField(max_length=200)
    date_added=models.DateField(auto_now_add=True)
    def __str__(self): # django use __str__() method as default way to show the basic info
        return self.topic_name


class Description(models.Model):
    text=models.CharField(max_length=200)
    
    date_added=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.text[:10]

class Entry(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE) # connetct entry to topic by a "id" key
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    class Meta():
        verbose_name_plural="entries"
    def __str__(self):
        return self.text[0:20]+"..."

