from django.contrib import admin
from .models import Blog
#같은 폴더의 models로부터 Blog클래스를 import해와라.

admin.site.register(Blog)
#admin사이트에 등록해라.