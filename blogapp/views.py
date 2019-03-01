from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator#페이지네이션을하기위해 임포트
from .models import Blog
#같은 폴더에 있는 models라는 파이썬 파일로부터 Blog클래스를 import
from .form import BlogPost


def home(request):
    blogs = Blog.objects#blogs라는 변수에 객체목록을 저장 #쿼리셋
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    #request된 페이지가 뭔지를 알아내고(request페이지를 변수에 담아내고)
    page = request.GET.get('page')#request된 페이지 번호가 이 page에 담긴것!
    #request된 페이지를 얻어온 뒤 return 해준다.
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})#세번째 인자로 사전형객체로 blogs키값으로 blogs를 받는다.

def detail(request, blog_id):
#home에 비해 인자를 하나 더 받는다.
    details = get_object_or_404(Blog, pk = blog_id)
    #details변수안에 몇번객체를 넣어줄건데 이 몇번 객체는 get_object_or_404로 받아준다.
    #get_object_or_404는 두개의 인자를 받는데, 첫번째는 어떤 클래스로부터 받는지, 두번째는 검색조건 즉 pk값을 써준다.

    return render(request, 'detail.html', {'details':details})

def new(request):#new.html띄우는 함수
    return render(request, 'new.html')

def create(request):#입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()#Blog라는 클래스로부터 blog라는 객체를 하나 생성
    blog.title = request.GET['title']#블로그 객체안에 title을 넣어준다.
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()#이것을 쓰기 위해 위에 import해준다.
    blog.save()#지금까지 객체에 넣은 내용을 데이터베이스에 저장해라
    return redirect('/blog/'+str(blog.id))#redirect(URL)은 이 위에 있는 것들을 다 처리하고 이 URL로 넘기세요 라는 뜻
    #str을 써준이유는 url은 항상 str인데, blog.id는 int형이기때문에 문자열로 형변환.
    #위에 있는 것이 다 처리되고, save로 데이터베이스에 저장되고, /blog/str(blog_id)로 곧장 이동이 된다.

def blogpost(request):
    #1.입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)#모델객체를 반환하된, 저장하지 않고 모델객체를 가져온다 이 post는 블로그형 객체
            post.pub_date = timezone.now()#입력공간에서 입력받지 않았던 시각을 넣어준다.
            post.save()
            return redirect('home')
    #2.빈페이지를 띄워주는 기능 -> GET
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})


