from django.shortcuts import render
from rest_framework import generics,status,filters
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, AllowAny
from django.contrib.auth.models import User
from .models import BlogPost
from .models import Comment
from .models import Topic
from .models import Category
from .models import Profile
from .models import Request
from .serializers import BlogPostSerializer
from .serializers import CommentSerializer
from .serializers import TopicSerializer
from .serializers import CategorySerializer
from .serializers import ProfileSerializer
from .serializers import RequestSerializer
from rest_framework.views import APIView
from .pagination import CustomPagination
from .serializers import RegisterSerializer



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # Anyone can create a new user



#defineing ReadOnly for [IsAuthenticated|ReadOnly]
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS



# Create your views here.

#Crud-
#django's builtin api view
class BlogPostCreate(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set author to the currently logged-in user
        serializer.save(author=self.request.user)

    #making a custom view to delete all the 
    def delete(self,request, *args, **kwargs):
        BlogPost.objects,all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#cRUD   
class BlogPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated|ReadOnly]
    lookup_field = "pk"

    def perform_create(self, serializer):
        # Automatically set author to the currently logged-in user
        serializer.save(author=self.request.user)


#view to Read blog, for all user
class BlogPostList(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    pagination_class = CustomPagination 
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['published']
    ordering = ['-published']   

#view to get blog made by loged in user
class BlogPostUserList(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return BlogPost.objects.filter(author=user)


class BlogPostSearchView(APIView):
    def get(self, request, format=None):
        #to get the title from query parameter, if none return ""(empty str) 
        title = request.query_params.get("title",'')
        print("DEBUG title_query:", title)

        if title:
            blog_posts = BlogPost.objects.filter(title__icontains=title)
        else:
            blog_posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        


#get all comments
class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created']
    pagination_class = CustomPagination


#get comment by blog id
class CommentBlogList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created']
    pagination_class = CustomPagination
    ordering = ['-created']   

    def get_queryset(self):
        blog = self.kwargs['blog']
        return Comment.objects.filter(blog=blog)


class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        # Automatically set author to the currently logged-in user
        serializer.save(user=self.request.user)

    def delete(self,request, *args, **kwargs):
        BlogPost.objects,all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class CommentRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated|ReadOnly]
    lookup_field = "pk"

    def perform_create(self, serializer):
        # Automatically set author to the currently logged-in user
        serializer.save(user=self.request.user)




#get all topics & Crud
class TopicListCreate(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated|ReadOnly]

#get specific topic & cRUD
class TopicRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated|ReadOnly]
    lookup_field = "pk"




#get all topics & Crud
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated|ReadOnly]

#get specific topic & cRUD
class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated|ReadOnly]
    lookup_field = "pk"




#get all topics & Crud
class ProfileListCreate(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated|ReadOnly]

#get specific topic & cRUD
class ProfileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated|ReadOnly]
    lookup_field = "pk"



#
class RequestListCreate(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated|ReadOnly]

#get specific topic & cRUD
class RequestRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated|ReadOnly]
    lookup_field = "pk"
