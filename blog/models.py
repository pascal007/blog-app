from django.contrib.auth import get_user_model
from django.db import models

from DockerBlogApp.models import BaseModel
User = get_user_model()


class Post(BaseModel):
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(max_length=5000, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog', null=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
