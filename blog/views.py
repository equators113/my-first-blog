from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # publish date가 없으면 목록에 표시되지 않음
    return render(request, 'blog/post_list.html', {'posts':posts})
