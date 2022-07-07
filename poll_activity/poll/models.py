from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User=get_user_model()
class Poll(models.Model):
    createdby=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.CharField(max_length=255)
    option1=models.CharField(max_length=255)
    option2=models.CharField(max_length=255)
    option3=models.CharField(max_length=255)
    option4=models.CharField(max_length=255)

class Answers(models.Model):
    poll=models.ForeignKey(Poll,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    option=models.CharField(max_length=255)