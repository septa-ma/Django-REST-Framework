from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import mixins
from .serialiazers import PostSerializer
from .models import Post

# Create your views here.
# the views type we can access in rest-framework

# 1- make views by using APIView
# the class inheratance from APIView
# class TestView(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self, request, *args, **kwargs):
#         if request.method == 'GET':
#             posts = Post.objects.all()
#             serializer = PostSerializer(posts, many=True)
#             return JsonResponse(serializer.data, safe=False)

#     def post(self, request, *args, **kwargs):
#         if request.method == 'POST':
#             data = JSONParser().parse(request)
#             serializer = PostSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data, status=200)
#             return JsonResponse(serializer.errors, status=400)

# 2- make views by using mixins
# the above code in TestView class is compeletly the same as
# what happening in list and create function of mixin modules.
# mixin classes inheretance from APIView.
# class PostView(mixins.CreateModelMixin, 
#             mixins.ListModelMixin, 
#             generics.GenericAPIView):

#     # because we inheretance from GenericAPIView
#     # need these 2 items
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# 3- make views by using generic-class it has all
# the functionality of makeing a post method
# for makeing get method need to add mixins.ListModelMixin
# and add get method or can make a new class which 
# inheretance from generics.ListCreateAPIView.
# the above code in PostView class is compeletly the same as
# what happening in functions of generics modules.
# generics classes inheretance from mixin.
class PostCreateView(generics.CreateAPIView,
                    mixins.ListModelMixin):
    # because the CreateAPIView inheretance from GenericAPIView
    # need these 2 items
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class PostListCreateView(generics.ListCreateAPIView):
    # because the CreateAPIView inheretance from GenericAPIView
    # need these 2 items
    serializer_class = PostSerializer
    queryset = Post.objects.all()