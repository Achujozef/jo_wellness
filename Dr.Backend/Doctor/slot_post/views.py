from django.shortcuts import render
from rest_framework.views import APIView
from Authentication.models import UserAccount
from .models import Post,DoctorSlot
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework import status,generics
from .serializer import PostSerializer,DoctorSlotSerializer,PostWithDoctorSerializer
from .producer import publish
from django.http import JsonResponse
from Authentication.models import UserAccount
from Authentication.serializer import UserSerializer
from rest_framework import viewsets, status

class CreatePostView(APIView):
    def patch(self, request, id):
        user = get_object_or_404(UserAccount, id=id)
        image = request.FILES.get("image")
        description = request.data.get("description")
        print(image,description)
        if not image:
            raise ParseError("No file was submitted.")
        print('njan ivide ethi',image)
        post = Post(doctor=user, image=image,description=description)
        post.save()
   
        return Response(status=status.HTTP_201_CREATED)

class DoctorPostsListView(APIView):
    def get(self, request, id):
        print("the id is",id)
        user = get_object_or_404(UserAccount, id=id)
        posts = Post.objects.filter(doctor=user).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DoctorSlotView(APIView):
    def post(self, request):
            time_slots = request.data.get("newSlots", []) 
            print("time slot",time_slots)
            dayss= request.data.get("day")
            print(dayss)
            doc=request.data.get("user")
            print(doc['id'])
            saved_slots = []
            for time_slot in time_slots:
                serializer = DoctorSlotSerializer(data={
                    "doctor": request.user.id, 
                    "day": request.data.get("day"), 
                    "start_time": time_slot,
                })
                if serializer.is_valid():
                    serializer.save()
                    saved_slots.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(saved_slots, status=status.HTTP_201_CREATED)

    def get(self, request):
        day = request.GET.get('day', 'today')  
        slots = DoctorSlot.objects.filter(day=day)
        serializer = DoctorSlotSerializer(slots, many=True)
        return Response(serializer.data)
    

class testView(APIView):
    def get(self,request):
        print("Rabit On view")
        publish()
        return Response(status=status.HTTP_201_CREATED)
    
class test(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-id')
        post_serializer=PostSerializer(posts,many=True)

        doctor = UserAccount.objects.all()
        doctor_serializer = UserSerializer(doctor,many=True)

        combined_data =[]
        for post in post_serializer.data:
            doctor_id = post['doctor']
            doctor_data = next((doctor for doctor in doctor_serializer.data if doctor['id'] == doctor_id),None)
            if doctor_data:
                post['doctor']=doctor_data
                combined_data.append(post)
                print(post)

        data={'post':combined_data}
        print(data)
        return Response(data, status=status.HTTP_200_OK)
    

class PostListView (generics.ListAPIView):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostWithDoctorSerializer

    def list(self, request, *args, **kwargs):
        posts = self.get_queryset()
        serializer = self.get_serializer(posts, many=True)
        print(serializer.data)
        return Response({'posts': serializer.data}, status=status.HTTP_200_OK)


class PostViewset(viewsets.ViewSet):
    def list (self,requests):
        posts = Post.objects.all().order_by('-id')
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def create(self,request):
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def retrieve(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def update(self,request, pk=None):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(instance=post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    def destroy(self, request, pk=None):
        post =Post.objects.get(pk=pk)
        post.delete()
        return Response("Post Deleted")