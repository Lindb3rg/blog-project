from django.db import models

from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.CharField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)
    
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def approve_comment(self):
        return self.comments.filter(approved_comments=True)
    
    def __str__(self) -> str:
        return self.title