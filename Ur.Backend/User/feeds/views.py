from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.
from doctor_api import doctor_get_post_url
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

class GetFeeds(APIView):
    doctor_get_post_url=doctor_get_post_url
    def get(self, request):
        print("Reached The User View")
        try:
            userResponse = requests.get(self.doctor_get_post_url)

            if userResponse.status_code == 200:
                posts = userResponse.json()
              
                
                return Response({'posts': posts}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Failed to retrieve posts'}, status=userResponse.status_code)
        except request.exceptions.RequestExpection as e:
            return JsonResponse({'error': 'Request failed: ' + str(e)}, status=500)