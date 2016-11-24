from django.template import loader, Context, RequestContext
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import Question, User
from forms import AskForm, AnswerFor

def proba(request):
    return HttpResponse('OK')

def question(request, quest_id) :
	try :
		quest = Question.objects.get(id = quest_id)
	except Question.DoesNotExist :
		raise Http404
	answers = Answer.objects.all().filter(question = quest)
	
	title = 'qwest ' + quest_id
	form = AnswerForm(initial{'question' : quest_id})
	
	return render(request, 'question.html', {
		'title' : title,
		'question' : quest,
		'list' : answers,
		'form' : form,
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
   
def askfrm(request):
    if request.method == "POST" :
		print("POST!!!!!!!!!!!!!!!!!!!!!!!!!")
		form = AskForm(request.POST)
		if form.is_valid():
			print("FORM IS VALID!!!!!!!!!!!!")
			quest = form.save()
			print("QUEST IS CREATE!!!!!!!!!!")
			url = quest.get_absolute_url()
			print("URL = " + url +"!!!!!!!!!")
			return HttpResponseRedirect(url)
	else :
		form = AskForm()
	return render(request, 'ask_add.html', {
		'form' : form
})

def answerfrm(request):
    if request.method == "POST" :
		form = AnswerForm(request.POST)
		if form.is_valid():
			answer = form.save()
			url = '/question/' + form.question
            return HttpResponseRedirect(url)
