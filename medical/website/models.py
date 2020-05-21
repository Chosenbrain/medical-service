from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title= models.CharField(max_length=50)


    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    categories = models.ManyToManyField(Category)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default = 0)
    view_count = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    thumbnail = models.ImageField()
    aboutblog = models.TextField()



    def __str__(self):
        return self.title



    