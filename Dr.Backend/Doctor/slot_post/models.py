from django.db import models
from Authentication.models import UserAccount
# Create your models here.
class Post(models.Model):
    doctor = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctor-posts',blank=True,null=True)
    description = models.CharField(max_length=1500,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0,blank=True) 

class DoctorSlot(models.Model):
    doctor = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    day = models.CharField(max_length=10) 
    start_time = models.TimeField()

