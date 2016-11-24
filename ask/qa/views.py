from django.template import loader, Context, RequestContext
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Question, User

def proba(request):
    return HttpResponse('OK')

def question(request, qid):
    if request.method == "POST":
        return HttpResponse('OK')
    else
        question = get_object_or_404(Question, id=qid)
        return render(request, 'question.html', {
            'question': question,
            'answers': question.answer_set.all()
        })

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
   
def ask(request):
    if request.method == "POST":
        form = askForm(request.POST)
        if form.is_valid():
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = askForm()
    return render(request, 'ask.html', {'form': form, })

def answer(request):
    if request.method == "POST":
        form = answerForm(request.POST)
        if form.is_valid():
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = answerForm()
    return render(request, 'answer.html', {'form': form, })

