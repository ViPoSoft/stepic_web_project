from django import forms
from .models import AskF
from .models import AnswerF

class AskForm(forms.ModelForm):
    class Meta:
    fields = ('title', 'text',)
    
class AnswerForm(forms.ModelForm):
    class Meta:
    fields = ('text','question',)
    
