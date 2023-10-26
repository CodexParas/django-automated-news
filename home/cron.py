from .get_news import get_article
import urllib.request
import requests
from .models import *
from pathlib import Path
from django.contrib.auth.models import User
user = User.objects.get(username="parasgupta")
BASE_DIR = Path(__file__).resolve().parent.parent
cat = list(Category.objects.values_list('name', flat=True))
prev_list = list(BlogModel.objects.values_list('source_url', flat=True))
def task():
    news = get_article(prev_list)
    img_url = news['image']
    image_name = img_url.split("/")[-1]
    urllib.request.urlretrieve(img_url, f'{BASE_DIR}/public/static/blog/{image_name}')
    title=news['title']
    slug=title.replace(' ','-')
    content=news['content']
    image=f"blog/{image_name}"
    cate=news['category']
    if cate not in cat:
        ca = Category(name=cate)
        ca.save()
        category = Category.objects.get(name=cate)
    else:
        category = Category.objects.get(name=cate)
    blog_obj = BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image, category=category, slug=slug, summary=news['summary'], source_url=news['source']
            )
    blog_obj.set_tags(news['tags'])
    blog_obj.save()