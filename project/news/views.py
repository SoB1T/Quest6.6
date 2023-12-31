from django.views.generic import ListView, DetailView
from .models import Post


class PostsList(ListView):
    model = Post
    ordering = "heading"
    template_name = "posts.html"
    context_object_name = "posts"


class PostDetails(DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"
