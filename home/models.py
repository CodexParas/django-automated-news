from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from home.helpers import *
from django.db.utils import IntegrityError
import json
from slugify import slugify

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    id = models.AutoField(primary_key=True)
    content = FroalaField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=1000, null=True, blank=True, unique=True)
    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=1000, default='News')
    summary = models.CharField(max_length=10000, default='Just a News')
    source_url = models.CharField(max_length=1000, default='No Source')

    def set_tags(self,x):
        self.tags=json.dumps(x)

    def get_tags(self):
        return json.loads(self.tags)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            self.slug=slugify(self.title)
            super(BlogModel, self).save(*args, **kwargs)
        except IntegrityError:
            self.slug = generate_slug(self.title)
            super(BlogModel, self).save(*args, **kwargs)
