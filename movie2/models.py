from django.db import models
from django.contrib.auth.models import  User
from django.utils import  timezone

# Create your models here.
class Posts(models.Model): #i have listed these data in 'post' thus object of this databse is 'post' .also see in views
    
    STATUS_CHOICES= (
        ('draft','Drafts'),
        ('published','Published'),
                                        )
    title=models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    content=models.TextField()
    seo_title = models.CharField(max_length=50)
    seo_description = models.CharField(max_length=50)
    author=models.ForeignKey(User, related_name='blog_posts',on_delete=models.CASCADE)
    published=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title

