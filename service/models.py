from django.db import models
class Topics(models.Model):
    topic_icon=models.CharField(max_length=50)
    topic_title=models.CharField(max_length=50)
    topic_description=models.TextField()

# Create your models here.
