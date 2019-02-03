from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):#자기자신을 인자로 받고
        return self.title#자기 자신의 제목을 반환한다.


    def summary(self):
        return self.body[:100]