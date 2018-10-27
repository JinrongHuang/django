from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible


class Category(models.Model):
    objects = models.Manager()
    #分类
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    #标签
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    objects = models.Manager()
    # 文章标题
    title = models.CharField(max_length=70)

    # 文章正文
    body = models.TextField()

    # 这两个列分别表示文章的创建时间和最后一次修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要， 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(max_length=200, blank=True)

    # 分类与标签
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_time']