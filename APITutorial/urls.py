from django.urls import path
# from .views import PostView
from .views import PostCreateView, PostListCreateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('test/', PostListCreateView.as_view(), name='test'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('token/', obtain_auth_token, name='obtain_token')
] 