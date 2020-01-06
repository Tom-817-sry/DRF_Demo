from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import  Response
from app01.models import Book
from app01.serializers import BookSerializer
from utils.pagination import MyPagination

class BookView(APIView):

    def get(self,request):
        # 1,实例化分页器对象
        queryset = Book.objects.all()
        page_obj = MyPagination()
        # 2，调用分页方法去分页queryset
        page_queryset = page_obj.paginate_queryset(queryset,request,view=self)
        # 3，把分页好的数据序列化返回

        # 4, 带着上一页下一页连接的响应

        ser_obj = BookSerializer(page_queryset,many=True)

        return page_obj.get_paginated_response(ser_obj.data)
        # return Response(ser_obj.data)
# class BookView(APIView):
#     def get(self, request):
#         queryset = Book.objects.all()
#         # 1,实例化分页器对象
#         page_obj = MyPagination()
#         # 2，调用分页方法去分页queryset
#         page_queryset = page_obj.paginate_queryset(queryset, request, view=self)
#         # 3，把分页好的数据序列化返回
#         # 4, 带着上一页下一页连接的响应
#         ser_obj = BookSerializer(page_queryset, many=True)
#
#         return page_obj.get_paginated_response(ser_obj.data)