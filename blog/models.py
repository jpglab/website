from django.db import models
from django.contrib import admin
from sorl.thumbnail import ImageField
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_editied = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    body = models.TextField() 
    tags = TaggableManager()

    def get_absolute_url(self):
        return '/blog/%s/' %(self.slug)

    def __unicode__(self):
        return '%s' %self.title

class Picture(models.Model):
    post = models.ForeignKey(Post)
    image = ImageField(upload_to='post_pictures')
    caption = models.CharField(blank=True, max_length=200)

    def __unicode__(self):
        return '%s' %self.image
