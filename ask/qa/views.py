from django.template import loader, Context, RequestContext
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Question, User, Answer
from django.views.decorators.http import require_GET
from .forms import AskForm, AnswerForm, LoginForm, SignupForm
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse 

def proba(request):
    return HttpResponse('OK')

def question(request, question_id):
    if request.method == 'POST':
        return answer(request)
    
    q = get_object_or_404(Question, id=question_id)
    a = Answer.objects.filter(question=q.id).order_by('-added_at')
    user = request.user
    form = AnswerForm(initial = {'question': question_id})
    context = {'question': q, 'answers': a, 'form': form, }
return render(request, 'question.html', context) 

def newqa(request):
    qmain = Question.objects.all().order_by('-id')
    
    paginator = Paginator(qmain, 10)
    page = request.GET.get('page')
    try:
        qmain = paginator.page(page)
    except PageNotAnInteger:
        qmain = paginator.page(1)
    except EmptyPage:
        qmain = paginator.page(paginator.num_pages)
    
    t = loader.get_template("new.html")
    c = Context({'questions':qmain, 'request':request})
    return HttpResponse(t.render(c))

def popular(request):
    qmain = Question.objects.all().order_by('-rating')
    
    paginator = Paginator(qmain, 10)
    page = request.GET.get('page')
    try:
        qmain = paginator.page(page)
    except PageNotAnInteger:
        qmain = paginator.page(1)
    except EmptyPage:
        qmain = paginator.page(paginator.num_pages)
    
    t = loader.get_template("popular.html")
    c = Context({'questions':qmain, 'request':request})
    return HttpResponse(t.render(c))
   
def ask(request, *args, **kwargs):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
return render(request, 'ask.html', {'form': form})

def answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            answer = form.save()
            url = answer.get_url()
return HttpResponseRedirect(url)
