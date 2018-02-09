from __future__ import unicode_literals

from django.db import models
import django.utils.timezone
from django.contrib.auth.models import User


# Create your models here.
class BlogArticles(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(User, related_name="blog_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=django.utils.timezone.now())

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title
