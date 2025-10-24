from django.test import TestCase
from django.urls import reverse
from api.models import User, Comment,BlogPost
from rest_framework.test import APITestCase



# Create your tests here.
class CommentAPITestCase(APITestCase):
    def setUp(self):
        # self.admin_user = User.objects.create_superuser(username='admin', password='@QWER1234')
        # self.normal_user = User.objects.create_user(username='billu', password='@QWER1234')


        # self.blog = BlogPost.objects.create(
        #     title="Test Blog",
        #     content="This is a test blog post"
        # )

        # self.comment = Comment.objects.create(
        #     blog = self.blog,
        #     body="sending from test"
        # )

        self.user = User.objects.create_user(username="alok", password="1234")
        self.blog = BlogPost.objects.create(title="Test Blog", content="Some content")

        self.blog1 = BlogPost.objects.create(title="Django Testing", content="Content 1")
        self.blog2 = BlogPost.objects.create(title="Python Tips", content="Content 2")
        self.blog3 = BlogPost.objects.create(title="Django REST Framework", content="Content 3")
        # self.comment = Comment.objects.create(blog=self.blog, body="Test Comment")

        self.client.login(username="alok", password="1234") 

        # self.url = reverse("blog-all")

    def test_get_blogs(self):
        url = reverse("blog-all")
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_blog(self):
        url = reverse("blog-detail" , kwargs={'pk': self.blog.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data['title'], "Test Blog")

    def test_get_search(self):
        
        url = reverse("blogpost-search")
        response = self.client.get(url,{"title": "django"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_comment_create(self):
        url = reverse("comment-create")
        data = {"blog": self.blog.id , "body": "Test Comment"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Comment.objects.count(), 1)
        # print(response.data)

    def test_get_comments(self):
        
        url = reverse("comments-blog" , kwargs={'blog': self.blog.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # print(response.data)
        # self.assertGreaterEqual(len(response.data), 1)








