from django.db import models

# Create your models here.

class LikedPosts(models.Model):
    PostId=models.IntegerField(unique=True)
    PostTitle=models.CharField(max_length=1500)
    def __str__(self) -> str:
        return self.PostTitle