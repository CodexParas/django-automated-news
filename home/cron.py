import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from .get_news import get_article
import urllib.request
from .models import *
from .helpers import *
from django.contrib.auth.models import User

try:
    user = User.objects.get(username="parasgupta")
except:
    c_user = User.objects.create_user("parasgupta", email = None, password = "1234")
    user = User.objects.get(username="parasgupta")
def task():
    cat = list(Category.objects.values_list('name', flat=True))
    prev_list = list(NewsModel.objects.values_list('title', flat=True))
    news = get_article(prev_list)
    img_url = news['image']
    image_name = generate_img(news['title'])+'.jpg'
    urllib.request.urlretrieve(img_url, f'{BASE_DIR}/public/static/blog/{image_name}')
    title=news['title']
    slug=generate_slug(title)
    content=news['content']
    image=f"blog/{image_name}"
    cate=news['category']
    if cate not in cat:
        ca = Category(name=cate)
        ca.save()
        category = Category.objects.get(name=cate)
    else:
        category = Category.objects.get(name=cate)
    blog_obj = NewsModel.objects.create(
                user=user, title=title,
                content=content, image=image, category=category, slug=slug, summary=news['summary'], source_url=news['source']
            )
    blog_obj.set_tags(news['tags'])
    blog_obj.save()