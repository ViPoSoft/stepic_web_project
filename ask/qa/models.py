from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=125)
    text = models.TextField(default="")
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name="q_to_likes")
    
    def __unicode__(self):
        return self.title

    def get_url(self):
        return "/question/{}/".format(self.id)

class Answer(models.Model):
    text = models.TextField(default="")
    #added_at = models.DateTimeField(auto_now_add=True)
    added_at = models.DateField(null=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    #author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.text
