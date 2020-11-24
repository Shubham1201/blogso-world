from django.urls import path
# from . import views
from .views import HomeView, ArticalDeatilView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, LikeView, AddCommentView
urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('artical/<int:pk>', ArticalDeatilView.as_view(), name="artical-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('artical/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('artical/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>', CategoryView, name="category"),
    path('like/<int:pk>', LikeView, name="like_post"),
    # path('dislike/<int:pk>', DislikeView, name="dislike_post"),
    path('artical/<int:pk>/commnet', AddCommentView.as_view(), name="add_comment"),
]