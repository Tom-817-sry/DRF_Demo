from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BookSerializer

from .models import Book,Publisher,Author



class GenericAPIView(APIView):
    query_set = None
    serializer_class = None

    def get_queryset(self):
        return self.query_set

    def get_serializer(self,*args,**kwargs):
        return self.serializer_class(*args,**kwargs)

class RetrieveModelMixin(object):
    def retrieve(self,request,id):
        book_obj = self.get_queryset().filter(id=id).first()
        ret = self.get_serializer(book_obj)
        return Response(ret.data)

class ListModelMixin(object):     #get方法抽离出来
    def list(self,request):
        queryset = self.get_queryset()
        ret = self.get_serializer(queryset,many=True)
        return Response(ret.data)

class CreateModelMixin(object):
    # def create(self):
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class UpdateModelMixin(object):
    def update(self,request,id):
        book_obj = self.get_queryset().filter(id=id).first()
        serializer = self.get_serializer(book_obj, data=request.data, partial=True)  # partial=True表示允许部分更新
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  # validated_data 是验证通过的数据   ， data的验证通过后再序列化好的数据
        else:
            return Response(serializer.errors)

class DestroyModelMixin(object):
    def destroy(self,request,id):
        book_obj = self.get_queryset().filter(id=id).first()
        book_obj.delete()
        return Response("")

class ListCreateAPIView(GenericAPIView,ListModelMixin,CreateModelMixin):
    pass

class RetrieveUpdateDestroyAPIView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    pass

class BookView(ListCreateAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer

    def get(self,request):
        # book_obj = Book.objects.first()
        # ret = BookSerializer(book_obj)
        # book_obj = Book.objects.all()
        # ret = BookSerializer(book_obj,many=True)

        return self.list(request)

    def post(self,request):
        print(request.data)
        # serializer = BookSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return  Response(serializer.data)
        # else:
        #     return Response(serializer.errors)
        return self.create(request)

class BookEditView(RetrieveUpdateDestroyAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer
    def get(self,request,id):
        # book_obj = Book.objects.filter(id=id).first()
        # ret = BookSerializer(book_obj)
        # book_list = self.get_queryset()
        # ret = self.serializer_class(book_list,many=True)
        return self.retrieve(request,id)

    def put(self,request,id):
        # book_obj = Book.objects.filter(id=id).first()
        # serializer = BookSerializer(book_obj,data=request.data,partial=True)   #partial=True表示允许部分更新
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)   #validated_data 是验证通过的数据   ， data的验证通过后再序列化好的数据
        # else:
        #     return Response(serializer.errors)
        return self.update(request,id)

    def delete(self,request,id):
        # book_obj = Book.objects.filter(id=id).first()
        # book_obj.delete()
        return self.destroy(request,id)


from rest_framework.viewsets import ModelViewSet


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


from rest_framework import views
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

