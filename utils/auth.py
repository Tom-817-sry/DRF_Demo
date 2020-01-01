from rest_framework.exceptions import AuthenticationFailed
from authDemo.models import User
from rest_framework.authentication import BaseAuthentication

class MyAuth(BaseAuthentication):
    def authenticate(self,request):                   #如果想使用认证组件，必须重写该方法
        token = request.query_params.get('token',"")
        if not token:
            raise BaseAuthentication("没有携带token")
        user_obj = User.objects.filter(token=token).first()
        if not user_obj:
            raise BaseAuthentication("token不合法")

        return (user_obj,token)    #user,auth  两个东西