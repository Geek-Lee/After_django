from django.shortcuts import render, redirect
from firstapp.models import Article, Comment
from firstapp.form import CommentForm
from django.template import Context, Template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
	article_list = Article.objects.all()
	context = {}
	page_robot = Paginator(article_list, 9)
	page_num = request.GET.get('page')
	try:
		article_list = page_robot.page(page_num)
	except EmptyPage:
		article_list = page_robot.page(page_robot.num_pages)
	except PageNotAnInteger:
		article_list = page_robot.page(1)
	context['article_list'] = article_list
	return render(request,'index.html', context)

def detail(request, page_num, error_form=None):
	context = {}
	article = Article.objects.get(id=page_num)
	form = CommentForm
	context['article'] = article
	context['form'] = form
	return render(request, 'detail.html', context)

def comment(request, page_num):
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			comment = form.cleaned_data['comment']
			a = Article.objects.get(id=page_num)
			c = Comment(name=name, content=comment, belong_to=a)
			c.save()
	else:
		return render(request, page_num=page_num, error_form=form)
	return redirect(to='detail', page_num=page_num)