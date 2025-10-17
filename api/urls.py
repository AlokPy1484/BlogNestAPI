from django.urls import path
from . import views
from .views import BlogPostSearchView 
from .views import BlogPostList
from .views import CommentBlogList



urlpatterns = [
    
    path('register/', views.RegisterView.as_view(), name='register'),

    path("blogposts/", views.BlogPostCreate.as_view(), name="blogpost-view-create"),

    #when user goes to'/blogposts/3' it will allow them to cRUD that blog
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestory.as_view(),
         name="blog-detail",
         ),
     #BlogPostRetrieve
     path("blogposts/all/", views.BlogPostList.as_view(),
          name="blog-all",
     ),

    path("blogposts/my", views.BlogPostUserList.as_view(),
            name="view",
     ),

    path('blogposts/search/', BlogPostSearchView.as_view(), name='blogpost-search'),



    
    path("comment/", views.CommentCreate.as_view(), name="comment-create"),

    path("comment/all", views.CommentList.as_view(), name="comment-view"),

    #when user goes to'/blogposts/3' it will allow them to cRUD that blog
    path("comment/<int:pk>/", views.CommentRetrieveUpdateDestory.as_view(), name="update",),
    
    path('comment/blog/<int:blog>', CommentBlogList.as_view(), name='comments-blog'),



 #categories
path("topics/", views.TopicListCreate.as_view(), name="topic-list-create"), 
path("topic/<int:pk>/", views.TopicRetrieveUpdateDestroy.as_view(), name="topic-update-delete"), 


#
path("categories/", views.CategoryListCreate.as_view(), name="category-list-create"), 
path("category/<int:pk>/", views.CategoryRetrieveUpdateDestroy.as_view(), name="category-update-delete"), 



#
path("profiles/", views.ProfileListCreate.as_view(), name="profile-list-create"), 
path("profile/<int:pk>/", views.ProfileRetrieveUpdateDestroy.as_view(), name="profile-update-delete"), 


#
path("requests/", views.RequestListCreate.as_view(), name="request-list-create"), 
path("request/<int:pk>/", views.RequestRetrieveUpdateDestroy.as_view(), name="request-update-delete"), 










]