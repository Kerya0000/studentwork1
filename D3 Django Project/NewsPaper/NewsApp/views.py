from django.views.generic import ListView, DetailView
from .models import Author, Category, Post, Comment
import datetime

class NewsList(ListView):

    model = Post

    ordering = 'dateCreation'

    template_name = 'news.html'

    context_object_name = 'news'

# Create your views here.

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

