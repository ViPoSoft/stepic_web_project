from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM qa_question q ORDER BY q.added_at DESC")
        last_questions = cursor.fetchall()
        return last_questions

    def popular(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM qa_question q ORDER BY q.rating DESC")
        popular_questions = cursor.fetchall()
        return popular_questions


class Question(models.Model):
    objects = QuestionManager() 
    title = models.CharField(max_length=125)
    text = models.TextField(default="")
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name="q_to_likes")
    

class Answer(models.Model):
    text = models.TextField(default="")
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
