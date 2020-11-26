from django.db import models

# Create your models here.
class Poll(models.Model):
    subject=models.CharField('投票主題',max_length=200)
    description=models.TextField('投票主題',max_length=200)
    date_created = models.DateField(auto_now_add=True)

class Option(models.Model):
    poll_id = models.IntegerField()
    title = models.CharField(max_length=200)
    count = models.IntegerField(default=0)