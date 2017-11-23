from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, 'blog/post_list.html', {'posts':posts})

def branch1(request):
    return render(request, 'blog/branch1.html', {})
