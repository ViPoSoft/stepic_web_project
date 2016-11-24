# -*- encoding: utf-8; -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
#class QuestionManager(models.Manager):
#    def new(self):
#        return self.objects.all().order_by('-added_at')
#    def popular(self):
#        return self.objects.all().order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_user')

    def get_url(self):
        return reverse('question', kwargs={'question_id': self.pk})

    #qobjects = models.Manager()
    #objects = QuestionManager()

    def __unicode__(self):
        return self.title
    
    #def get_url(self):
    #    return reverse('questions', kwargs={'id': self.id})

class Answer(models.Model):
    text = models.TextField()
    #added_at = models.DateTimeField(blank=True,  null=True, default=datetime.utcnow())
    added_at = models.DateTimeField(blank=True,  auto_now_add=True)
    #question = models.OneToOneField(Question, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('question', kwargs={'question_id': self.question.id})
    
    def __unicode__(self):
        return "Answer by {0} to question {1}: {2}...".\
format(self.author.username, self.question.id, self.text[:50])
