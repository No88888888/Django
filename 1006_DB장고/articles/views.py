from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Articles
# Create your views here.

def index(request):
    articles = Articles.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            # return redirect('articles:index')
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form' : form,

    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    # TODO: 댓글 구현
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    if request.method == 'POST':    # 게시물 수정
        form = ArticleForm(request.POST, instance=article) # 인스턴스 없으면 수정이 아니라 새 글이 작성됨
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:   # 게시물 수정 페이지 랜더링
        form = ArticleForm(instance=article)
    context = {
        'pk' : article.pk,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    article.delete()
    return redirect('articles:index')