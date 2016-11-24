# -*- encoding: utf-8; -*-
from django.db import models
from django.contrib.auth.models import User

#class QuestionManager(models.Manager):
#    def new(self):
#        return self.objects.all().order_by('-added_at')
#    def popular(self):
#        return self.objects.all().order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, related_name='+', default=1)
    likes = models.ManyToManyField(User, default=1)
    
    def get_absolute_url(self) :
return '/question/%d/' % self.pk

    #def __unicode__(self):
     #   return self.title
    
    #def get_url(self):
    #    return reverse('questions', kwargs={'id': self.id})

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, null=False, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, related_name='+', default=1)

    #def __unicode__(self):
    #    return self.title
