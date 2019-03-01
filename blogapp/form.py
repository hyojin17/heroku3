from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog#블로그모델을 기반으로
        fields = ['title', 'body']#제목과 내용을 입력받을 것이다.

#위에는 model을 기반으로 한 입력방법

#아래는 임의의 입력방법
# class BlogPost(forms.Form):
#     email = forms.EmailField()
#     files = forms.FileField()
#     url = forms.URLField()
#     words = forms.CharField(max_length=200)
#     max_number = forms.ChoiceField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three')])



