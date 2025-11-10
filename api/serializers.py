from rest_framework import serializers
from django.utils.timesince import timesince
from django.contrib.auth.models import User
from .models import BlogPost
from .models import Comment
from .models import Topic
from .models import Category
from .models import Profile
from .models import Request
from .models import Like
from .models import Notification




class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class BlogPostSerializer(serializers.ModelSerializer):

    #prevent client from passing userid themselve 
    # author = serializers.ReadOnlyField(source='author.username')
    author_name = serializers.ReadOnlyField(source='author.username')


    date_since = serializers.SerializerMethodField()

    def get_date_since(self, obj):
        return timesince(obj.published) + " ago"

    class Meta:
        model = BlogPost
        fields = '__all__'




class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    # when we use this then DRF will look for get_<field_name>(self, obj)
    date_since = serializers.SerializerMethodField()

    def get_date_since(self, obj):
        return timesince(obj.created) + " ago"

    class Meta:
        model = Comment
        #id feild is auto added to our models we dont need to specifiy that
        fields = '__all__'




class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
    
        #id feild is auto added to our models we dont need to specifiy that
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    # topics = serializers.PrimaryKeyRelatedField(many=True,queryset=Topic.objects.all())
    topics = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        #id feild is auto added to our models we dont need to specifiy that
        fields = ['id','title','topics']




class ProfileSerializer(serializers.ModelSerializer):

    user_name = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Profile
    
        #id feild is auto added to our models we dont need to specifiy that
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
    
        #id feild is auto added to our models we dont need to specifiy that
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
    
        #id feild is auto added to our models we dont need to specifiy that
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
    
        fields = '__all__'



