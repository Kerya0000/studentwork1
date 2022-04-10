from .views import NewsList, PostDetail, Search, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView
from django.urls import path

urlpatterns = [
    path('', NewsList.as_view(), name='dieHauptSeite'),
    path('<int:pk>', PostDetail.as_view(), name="post_detail"),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('search/', Search.as_view(), name='search'),
    path('add/', PostCreateView.as_view(), name='post_create'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
               ]




