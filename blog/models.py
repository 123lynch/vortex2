from turtle import position
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from account.models import UserBase
from ckeditor.fields import RichTextField
from django.urls import reverse
from datetime import datetime, date
from cloudinary.models import CloudinaryField
#from portfolio.models import Category
from taggit.managers import TaggableManager

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=100, null=True)
    
    def __str__(self):
        return self.name

class WriterProfile(models.Model):
    user = models.OneToOneField(
        UserBase,
        related_name='profile',
        on_delete=models.CASCADE,
    )
    image = CloudinaryField('image', null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.CharField(max_length=2000)

    def __str__(self):
        return str(self.user)

#  image = models.ImageField(upload_to='images/', default='images/default.png')

# Create your models here.
class BlogPost(models.Model):
    image = CloudinaryField('image', null=True, blank=True)
    title = models.CharField(max_length=255)
    snippet = models.CharField(max_length=255, default='snippet test')
    slug = models.SlugField(unique=True, max_length=100, null=True)
    author = models.ForeignKey(WriterProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content1 = RichTextField(blank=True, null=True)
    blog_quote = models.CharField(max_length=500, blank=True)
    content2 = RichTextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('BlogPost-details', kwargs={'slug': self.slug})

class BlogComment(models.Model):
    blogpost_connected =  models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(UserBase, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + ' , ' + self.blogpost_connected.title[:40]

    def get_absolute_url(self):
        return reverse('update_comment', kwargs={'pk': self.pk})

class About(models.Model):
    image = CloudinaryField('image', null=True, blank=True)
    title = models.CharField(max_length=255)
    content1 = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title + '|' 'about'

class Roles(models.Model):
    title = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.title