import requests
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog.settings')
import django
django.setup()
from home.models import BlogModel
img_url = 'https://blog.finxter.com/wp-content/uploads/2022/04/greenland_01a.jpg'
response = requests.get(img_url)
if response.status_code:
    fp = open('public/static/blog/greenland_01a.png', 'wb')
    fp.write(response.content)
    fp.close()
from django.contrib.auth.models import User
user = User.objects.get(username="parasgupta")
#user="parasgupta"
title="try"
slug=title.replace(' ','-')
content="DEMO"
image="blog/greenland_01a.png"

blog_obj = BlogModel.objects.create(
            user=user, title=title,
            content=content, image=image, slug=slug
        )
blog_obj.save()