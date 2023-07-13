from django.urls import path
from . import views

urlpatterns = [
    path('posts_creted_author/', views.ListPostsAuthor.as_view(),name="posts_creted_author"),
    path('posts_create_author_username/<str:username>/', views.ListPostsForAuthorUsername.as_view(),name="posts_create_author_username"),
    path('posts_create_author_username_query/', views.ListPostsForAuthorUsernameUsingQuery.as_view(),name="posts_create_author_username_query"),
    path('homepage/',views.homepage,name='home_page')
    # path('<int:pk>', views.PostDetail.as_view(),name='post_detail'),
    # path('create/', views.PostCreate.as_view(),name='post_create'),
    # path('update/<int:pk>', views.PostUpdate.as_view(),name='post_update'),
    # path('delete/<int:pk>', views.PostDelete.as_view(),name='post_delete'),
]