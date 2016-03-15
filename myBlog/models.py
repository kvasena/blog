from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(timezone.now())
    updated = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.created = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=255)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def create_tag(self):
        self.save()


class Comment(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created = models.DateTimeField(timezone.now())
    updated = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.created = timezone.now()
        self.save()


class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


