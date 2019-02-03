from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length = 255)#title에는 문자열을 최대 255로 해서 담아줌.
    image = models.ImageField(upload_to='images/')#images라는 디렉토리에 담을 것이라는 의미로 upload to = 'images'
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title