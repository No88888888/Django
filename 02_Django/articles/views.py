from django.shortcuts import render
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
    title = request.GET.get('title')
    content = request.GET.get('content')
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
    
    return render(request, 'articles/create.html')