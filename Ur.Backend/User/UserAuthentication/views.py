from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserCreateSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from .models import UserAccount
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ParseError
from rest_framework.exceptions import AuthenticationFailed
from django.db.models import Q
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import jwt
from rest_framework import generics
from .producer import publish



class RegisterUser(APIView):
    def post(self, request):
        data = request.data
        serializer = UserCreateSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.create(serializer.validated_data)

        user = UserSerializer(user)

        return Response(user.data, status=status.HTTP_201_CREATED)


class RetrieveUserView(APIView):

    def get(self, request):
        queryset = UserAccount.objects.filter(is_staff = False).all().order_by('-date_joined')
        serialized = UserSerializer(queryset, many=True)

        return Response(serialized.data)



class BlacklistTokenUpdateView(APIView):
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class EditUser(APIView):
    def patch(self, request, id):
        user = get_object_or_404(UserAccount, id=id)
        image = request.FILES.get("image")
        print(image)
        if not image:
            raise ParseError("No file was submitted.")
        print(image)
        if image:
            
            user.image = image
            print(user.image.url)
        user.save()
        return Response(
            {
                "id": user.id,
                "image": "http://localhost:8000/api/users" + user.image.url,
            }
        )

class GetUser(APIView):
    def get(self,request, id):
        try:
            user = UserAccount.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data)        
        except UserAccount.DoesNotExist:
            raise Http404

class AdminLoginView(APIView):
        def admin_token_view(request):
            email = request.data.get('email')
            password = request.data.get('password')

            user = authenticate(email=email, password=password)
            if user is None:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

            if not user.is_staff:
                return Response({'error': 'You are not authorized to perform this action'}, status=status.HTTP_401_UNAUTHORIZED)

            refresh = RefreshToken.for_user(user)

            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            })

class ProfileUpdateView(APIView):
    def post(self, request ,id):
        user = UserAccount.objects.get(id=id)
        userData =  UserSerializer(instance=user, data=request.data, partial=True)
        if userData.is_valid():
            userData.save()
            return Response(userData.data, status=status.HTTP_200_OK)
        return Response(400)


class DeleteUser(APIView):
    def post(self, request, id):
        user = UserAccount.objects.get(id=id)
        user.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class UserSearchView(APIView):
    def get(self, request):
        keyword = request.GET.get('query')
        print(keyword)
        users = UserAccount.objects.filter(Q(name__icontains = keyword) | Q(phonenumber__icontains = keyword) , is_staff = False)
        serialized = UserSerializer(users, many=True)
        return Response(serialized.data)
    
class usertestView(APIView):
    def get(self,request):
        print('Njan Rabbit Useril  Ethiyalloooo')
        publish()