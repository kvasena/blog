from django.contrib import admin
from .models import Category
from .models import Article
from .models import Comment
from .models import User
from .models import Tag

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Tag)


