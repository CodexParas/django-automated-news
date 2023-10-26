from django.shortcuts import render, redirect
import random
from .form import *
from django.contrib.auth import logout

def home(request):
    popular_posts = BlogModel.objects.order_by("-views")[:3]
    tops = BlogModel.objects.order_by("-created_at")[:3]
    view_op=1
    if BlogModel.objects.count()<9:
        view_op=0
    blogs = BlogModel.objects.order_by("-created_at")[:9]
    for blog in blogs:
        blog.summary = (blog.summary.split('.')[0])+'.'
    context = {'blogs': blogs,'tops': tops, 'view_op':view_op, 'popular_posts' : popular_posts}
    return render(request, 'home.html', context)

def page(request,no):
    popular_posts = BlogModel.objects.order_by("-views")[:3]
    tops = BlogModel.objects.order_by("-created_at")[:3]
    post_no=9
    if no=='1' or BlogModel.objects.count()//post_no<int(no)-1:
        return redirect('/')
    view_op=1
    if BlogModel.objects.count()//post_no<int(no):
        view_op=0
    no = int(no)
    start=(no-1)*post_no
    blogs = BlogModel.objects.order_by("-created_at")[start:start+post_no]
    for blog in blogs:
        blog.summary = (blog.summary.split('.')[0])+'.'
    context = {'blogs': blogs,'tops': tops,'no':no,'view_op':view_op, 'popular_posts' : popular_posts}
    return render(request, 'page.html', context)

def category_view(request,cat):
    cat = cat.capitalize()
    category = Category.objects.get(name=cat)
    popular_posts = BlogModel.objects.order_by("-views")[:3]
    blogs = BlogModel.objects.filter(category=category)
    for blog in blogs:
        blog.summary = (blog.summary.split('.')[0])+'.'
    context = {'blogs': blogs,'popular_posts' : popular_posts, 'cat':cat}
    return render(request, 'category.html', context)

def blog_detail(request, slug):
    blogs = list(BlogModel.objects.all())
    popular_posts = BlogModel.objects.order_by("-views")[:3]
    random_blogs = random.sample(blogs,2)
    print(random_blogs)
    #context = {}
    next_post='0'
    try:
        blog_obj = BlogModel.objects.filter(slug=slug).first()
        i = blogs.index(blog_obj)
        if blog_obj.id != BlogModel.objects.last().id:
            next_post = blogs[i+1]
        previous_post = blogs[i-1]
        tags = blog_obj.get_tags()
        blog_obj.views=blog_obj.views+1
        blog_obj.save()
        context = {'blog_obj':blog_obj,'previous_post':previous_post,'next_post':next_post,'random_blogs':random_blogs, 'popular_posts' : popular_posts, 'tags' : tags}
    except Exception as e:
        print(e)
    return render(request, 'blog.html', context)