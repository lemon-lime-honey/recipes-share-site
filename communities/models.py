from django.db import models
from imagekit.models import ProcessedImageField
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_posts = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts_users', blank=True)


    def __str__(self):
        return f'{self.title} - {self.user}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.post.title} - {self.user}'


class Image(models.Model):
    def image_path(instance, filename):
        return f'communities/posts/{instance.post.pk}/{filename}'


    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=image_path)


    def __str__(self):
        return f'{self.post.title} - image'