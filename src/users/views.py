from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response



class TestsView(APIView):

    def get(self, request):
        return Response({'ok': 'OK'})
