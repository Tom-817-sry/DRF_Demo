from rest_framework import serializers
from .models import Book


class PublisherSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=32)


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=32)

book_obj = {
        "title": "Alex的图书",
        "w_category": 1,
        "pub_time": "2019-12-06",
        "publisher_id": 1,
        "author_list": [1,2]
    }

# class BookSerializer(serializers.Serializer):
#
#     id = serializers.IntegerField(required=False)    #required 表示不需要传
#     title = serializers.CharField(max_length=32)
#     CHOICES = ((1, "Python"), (2, "Go"), (3, "Linux"))
#     category = serializers.ChoiceField(choices=CHOICES,source="get_category_display",read_only=True)  #read_only=True 表示只在序列化的时候用
#     w_category = serializers.ChoiceField(choices=CHOICES,write_only=True)   #write_only=True 表示只在反序列化的时候用
#     pub_time = serializers.DateField()
#
#     publisher = PublisherSerializer(read_only=True)
#     publisher_id = serializers.IntegerField(write_only=True)
#     author = AuthorSerializer(many=True,read_only=True)
#     author_list = serializers.ListField(write_only=True)
#
#     def create(self, validated_data):
#         book = Book.objects.create(title=validated_data['title'],category=validated_data['w_category'],
#                             pub_time=validated_data['pub_time'],publisher_id=validated_data['publisher_id'])
#         book.author.add(*validated_data['author_list'])
#         return book
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title",instance.title)
#         instance.pub_time = validated_data.get("pub_time",instance.pub_time)
#         instance.category = validated_data.get("category",instance.category)
#         instance.publisher_id = validated_data.get("publisher_id",instance.publisher_id)
#         if validated_data.get('author_list'):
#             instance.author.set(validated_data['author_list'])
#         instance.save()
#         return instance
#
#     def validate_title(self, value):            # 钩子写法，验证put的 包含python
#         if "python" not in value.lower():
#             raise serializers.ValidationError('标题必须含有python')
#         return value
#
#     def validate(self, attrs):
#         if attrs['w_category'] == 1 and attrs['publisher_id'] == 1:
#             return attrs
#         else:
#             raise serializers.ValidationError('不符合')


class BookSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source="get_category_display")
    # publisher = serializers.SerializerMethodField()                 # 这个是方法字段，可以写一个方法帮组过滤
    # author = serializers.SerializerMethodField()
    #
    # def get_publisher(self,obj):    # 钩子方法 get_ 接对象名称
    #     # obj 是我们序列化的每个Book对象
    #     publisher_obj = obj.publisher
    #     return {"id":publisher_obj.id,"title":publisher_obj.title}
    #
    # def get_author(self,obj):
    #     author_query_set = obj.author.all()
    #     return [{"id":author_obj.id,"name":author_obj.name} for author_obj in author_query_set]

    category_display = serializers.CharField(read_only=True)
    publisher_info = serializers.SerializerMethodField(read_only=True)                 # 这个是方法字段，可以写一个方法帮组过滤
    authors = serializers.SerializerMethodField(read_only=True)

    def get_category_display(self,obj):
        return obj.get_category_display()

    def get_publisher_info(self,obj):    # 钩子方法 get_ 接对象名称
        # obj 是我们序列化的每个Book对象
        publisher_obj = obj.publisher
        return {"id":publisher_obj.id,"title":publisher_obj.title}

    def get_authors(self,obj):
        author_query_set = obj.author.all()
        return [{"id":author_obj.id,"name":author_obj.name} for author_obj in author_query_set]

    class Meta:
        model = Book
        fields = "__all__"
        extra_kwargs = {"category":{"write_only":True},"publisher":{"write_only":True},
                        "author":{"write_only":True}}       #通过这个语句进行反序列化，以防重写

