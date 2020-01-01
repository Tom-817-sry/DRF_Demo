from django.shortcuts import render

# Create your views here.

import uuid
from .models import User

from rest_framework.views import APIView
from rest_framework.response import Response

from utils.permission import MyPermission
from utils.auth import MyAuth
from utils.throttle import MyThrottle

class DemoView(APIView):
    def get(self,request):
        pass
        return Response('auth Demo~!')

class LoginView(APIView):
    def post(self,request):
        username = request.data.get("username")
        pwd = request.data.get("pwd")
        token = uuid.uuid4()
        User.objects.create(username=username,pwd=pwd,token=token)
        return Response("创建用户成功！")

class TestView(APIView):
    authentication_classes = [MyAuth,]
    permission_classes =[MyPermission,]
    throttle_classes = [MyThrottle,]
    def get(self,request):
        print(request.user)
        print(request.auth)
        return Response("test")