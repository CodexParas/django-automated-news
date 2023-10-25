import requests
from .models import *
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
from django.contrib.auth.models import User
user = User.objects.get(username="parasgupta")
print(BASE_DIR)

cat = list(Category.objects.values_list('name', flat=True))
def task():
    print("Running....")
    img_url = 'https://blog.finxter.com/wp-content/uploads/2022/04/greenland_01a.jpg'
    response = requests.get(img_url)
    if response.status_code:
        fp = open(f'{BASE_DIR}/public/static/blog/greenland_01a.png', 'wb')
        fp.write(response.content)
        fp.close()
    title="try 1"
    #slug=title.replace(' ','-')
    content="DEMO"
    image="blog/greenland_01a.png"
    cate="News"
    if cate not in cat:
        ca = Category(name=cate)
        ca.save()
    else:
        category = Category.objects.get(name=cate)
    blog_obj = BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image, category=category, slug='try-1'
            )
    blog_obj.save()