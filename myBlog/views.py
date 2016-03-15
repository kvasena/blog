from django.shortcuts import render
from .models import Article
from .models import Category
from .models import User
from .models import Comment
from .models import Tag


def article_list(request):
    articles = Article.objects.order_by('created')

    return render(request, 'myBlog/article_list.html', {'articles': articles})
