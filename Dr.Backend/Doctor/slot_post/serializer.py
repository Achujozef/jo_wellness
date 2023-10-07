from rest_framework import serializers
from .models import Post,DoctorSlot
from Authentication.serializer import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostWithDoctorSerializer(serializers.ModelSerializer):
    doctor = UserSerializer()
    class Meta:
        model = Post
        fields ='__all__'

class DoctorSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSlot
        fields = ('doctor','day','start_time')