from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
class Question(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    question= models.CharField(max_length=300,null=True, blank=True)
    timestamp= models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
	answer = models.CharField(max_length=1000, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, blank=True)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	upvotes = models.IntegerField(blank=True)

	def __str__(self):
		return self.answer

class Upvote(models.Model):
	reader = models.ForeignKey(User, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
