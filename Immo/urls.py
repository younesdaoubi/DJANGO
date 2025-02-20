from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView #filtrer
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='Immo-home'), #localhost:8000/Immo/
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),  # localhost:8000/Immo/
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='Immo-about'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    #path('post/<int:pk>/favourite_post/', views.PostDetailView.favourite_post, name='favourite_post'),
    path(r'(?P<id>\d+)/favourite_post/', views.PostDetailView.favourite_post, name='favourite_post'),
    path('search_posts/', views.search_posts, name='search-posts'),
    path('favourites/', views.post_favourite_list, name = "post_favourite_list"),
]
