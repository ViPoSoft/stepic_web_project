from django import forms
from .models import Question, Answer


class AskForm(forms.ModelForm):
    class Meta:
    fields = ('title', 'text',)
    
class AnswerForm(forms.ModelForm):
    class Meta:
    fields = ('text','question',)
    
