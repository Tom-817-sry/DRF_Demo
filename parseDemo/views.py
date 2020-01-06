from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class DjangoView(View):
    def get(self,request):
        print(type(request))
        return HttpResponse("Django Test")

class DEFView(APIView):
    def get(self,request):
        return Response("DRF解析器的测试~")