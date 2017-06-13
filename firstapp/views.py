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