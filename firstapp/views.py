from django.shortcuts import render, redirect
from firstapp.models import Article, Comment
from firstapp.form import CommentForm
from django.template import Context, Template

# Create your views here.

def index(request):
	article_list = Article.objects.all()
	context = {}
	context['article_list'] = article_list
	return render(request,'index.html', context)

def detail(request, page_num):
	if request.method == "GET":
		form = CommentForm
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data["name"]
			content = form.cleaned_data["comment"]
			article = Article.objects.get(id=page_num)
			c = Comment(name=name, content=content, belong_to=article)
			c.save()
			return redirect(to="detail", page_num=page_num)
	context = {}
	article = Article.objects.get(id=page_num)
	context['article'] = article
	context['form'] = form
	return render(request, 'detail.html', context)