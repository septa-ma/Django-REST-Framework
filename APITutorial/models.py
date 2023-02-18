import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    description = models.TextField(max_length=20)
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
