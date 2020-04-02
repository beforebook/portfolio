from django.db import models

# Create your models here.

class Gallery(models.Model):
    title = models.CharField(default='请输入作品标题', max_length=30)
    description = models.CharField(default='在这里写作品的简介', max_length=80)
    image = models.ImageField(default='default.png', upload_to='images/')


    def __str__(self):
        return self.title
