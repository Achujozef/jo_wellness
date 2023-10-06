from django.contrib import admin
from .models import Post,DoctorSlot
# Register your models here.
admin.site.register(DoctorSlot)
admin.site.register(Post)