from django.contrib import admin
from django.urls import path
import blogapp.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/<int:blog_id>', blogapp.views.detail, name="detail"),
    #blog다음에 숫자로 구분해주기위해 pathconverter인 <>사용
    #blogapp안에있는 views라고 하는 파일안에 있는 detail함수에게 blog_id라고 하는 인자를 전달해줄것이다.
    #그리고 이 패스의 이름은 datail이라고 설정.
    path('blog/new/', blogapp.views.new, name="new"),
    path('blog/create', blogapp.views.create, name="create"),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
