from django.shortcuts import render, redirect
import random
from django.contrib.auth import logout
from .models import BlogModel
def error(request):
    return render(request,'error.html')

def home(request):
    if BlogModel.objects.count()!=0:
        popular_posts = BlogModel.objects.order_by("-views")[:3]
        if BlogModel.objects.count()>2:
            tops = BlogModel.objects.order_by("-created_at")[:3]
        else:
            tops = 'Null'
        view_op=1
        if BlogModel.objects.count()<9:
            view_op=0
        blogs = BlogModel.objects.order_by("-created_at")[:9]
        for blog in blogs:
            blog.summary = (blog.summary.split('.')[0])+'.'
        context = {'blogs': blogs,'tops': tops, 'view_op':view_op, 'popular_posts' : popular_posts}
        return render(request, 'home.html', context)
    else:
        return redirect('error')

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
    try:
        random_blogs = random.sample(blogs,2)
    except:
        random_blogs = 'Null'
    #print(random_blogs)
    try:
        blog_obj = BlogModel.objects.filter(slug=slug).first()
        # print(blog_obj)
        i = blogs.index(blog_obj)
        if blog_obj.id != BlogModel.objects.last().id:
            next_post = blogs[i+1]
        else:
            next_post = 'Null'
        # print(next_post)
        if BlogModel.objects.count()>1:
            previous_post = blogs[i-1]
        else:
            previous_post = 'Null'
        print(previous_post)
        tags = blog_obj.get_tags()
        # print(tags)
        blog_obj.views=blog_obj.views+1
        blog_obj.save()
        # print(blog_obj,previous_post,next_post)
        context = {'blog_obj':blog_obj,'previous_post':previous_post,'next_post':next_post,'random_blogs':random_blogs, 'popular_posts' : popular_posts, 'tags' : tags}
    except Exception as e:
        print(e)
    #print(context)
    return render(request, 'blog.html', context)