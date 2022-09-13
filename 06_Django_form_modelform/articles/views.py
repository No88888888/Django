from django.shortcuts import render, redirect
from .form import ArticleForm
from .models import Articles
from django.views.decorators.http import require_http_methods, require_POST, require_safe
# Create your views here.

@require_safe
def index(request):
    article = Articles.objects.all()
    context ={
        'article' : article,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

# def edit(request, pk):
#     article = Articles.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article' : article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context )

@require_http_methods(['GET', 'POST'])
def update(request,pk):
    article = Articles.objects.get(pk=pk)
    if request.method=='POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        'article' : article,
    }
    return render(request, 'articles/update.html', context)

@require_safe
def detail(request, pk):
    article = Articles.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    article = Articles.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)
        