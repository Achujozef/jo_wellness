from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.
from doctor_api import doctor_get_post_url, doctor_get_all_url
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

class GetFeeds(APIView):
    doctor_get_post_url=doctor_get_post_url
    print("Feeds call Reached The User View")
    def get(self, request):
        
        try:
            print("jsldkvkjlsdcjkvjl;jk")
            response = requests.get(doctor_get_post_url)

            if response.status_code == 200:
                posts = response.json()
              
                
                return Response({'posts': posts}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Failed to retrieve posts'}, status=response.status_code)
        except Exception as e:
            return Response({'error': 'Request failed: ' + str(e)}, status=500)


class GetDoctors(APIView):
    doctor_get_all_url=doctor_get_all_url
    print("Doctor List Call reached View 1 2 3 ")
    def get(self, request):
        try:
            response = requests.get(doctor_get_all_url)
            print('Urls',doctor_get_all_url)
            if response.status_code ==200:
                List_doctor=response.json()
                return Response(List_doctor)
            else:
                return Response({'error': 'External service request failed'}, status=response.status_code)
        except Exception as e:
            return Response({'error':str(e)},status=500)    

# class LikePost(APIView):
#     def post(self, request):
#         post_id = request.data.get('PostId')
#         try:
#             post=