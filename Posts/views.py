from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status,generics,mixins
from rest_framework.decorators import api_view,APIView,permission_classes
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.pagination import PageNumberPagination

class CustomePagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    
@api_view(http_method_names=['GET', 'POST'])
@permission_classes([AllowAny])
def homepage(request:Request):

    if request.method == 'POST':
        data = request.data

        response = {"message":"Welcome to homepage","data":data}

        return Response(data=response, status=status.HTTP_201_CREATED)
    
    response = {"message":"Welcome to home page"}
    return Response(data=response,status=status.HTTP_200_OK)

class PostsViewset(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    pagination_class=CustomePagination


class ListPostsAuthor(generics.GenericAPIView,mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        return Post.objects.filter(author=user)
    
    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class ListPostsForAuthorUsername(generics.GenericAPIView, mixins.ListModelMixin):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs.get('username')
        
        return Post.objects.filter(author__username=username)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) 
      
class ListPostsForAuthorUsernameUsingQuery(generics.GenericAPIView, mixins.ListModelMixin):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Post.objects.all()
        username = self.request.query_params.get('username') or None

    
        if username is not None:
            return Post.objects.filter(author__username=username)
        return queryset
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)   
    
