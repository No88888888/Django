from django.shortcuts import render, redirect
from .models import Articles
# Create your views here.
def index(request):
    # DB의 전체 데이터를 조회
    articles = Articles.objects.all()
    context = {
        'articles' : articles,
        }
    
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 사용자의 데이터를 받아서 DB에 저장
    title = request.POST.get('title')
    content = request.POST.get('content')
    # DB에 저장
    
    # 1번째 방법
    # article = Articles()
    # article.title = title
    # article.content = content
    # article.save()
    
    #2번째 방법(권장)
    article = Articles(title=title, content=content) # 앞에가 필드 뒤에가 사용자로 받아서 저장한 변수
    article.save()
    
    #3번째 방법
    # Articles.objects.create(title=title, content=content)
    # return render(request, 'articles/create.html')
    return redirect('articles:detail', article.pk)

#게시글 상세보기
def detail(request, pk):
    articles = Articles.objects.get(pk=pk)
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    articles = Articles.objects.get(pk=pk)
    articles.delete()
    return redirect('articles:index')

def edit(request, pk):
    articles = Articles.objects.get(pk=pk)
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/edit.html', context)



def update(request, pk):
    articles = Articles.objects.get(pk=pk)
    
    articles.title = request.POST.get('title')
    articles.content = request.POST.get('content')
    articles.save()
    return redirect('articles:detail', articles.pk)