from django.shortcuts import render, redirect
import random
# Create your views here.

from .form import *
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('/')


def home(request):
    view_op=1
    if BlogModel.objects.count()<9:
        view_op=0
    context = {'blogs': BlogModel.objects.order_by("-created_at")[:9],'tops': BlogModel.objects.order_by("-created_at")[:3], 'view_op':view_op}
    return render(request, 'home_new.html', context)

def page(request,no):
    post_no=9
    if no=='1' or BlogModel.objects.count()//post_no<int(no)-1:
        return redirect('/')
    view_op=1
    if BlogModel.objects.count()//post_no<int(no):
        view_op=0
    
    no = int(no)
    start=(no-1)*post_no
    #start=int(no)
    context = {'blogs': BlogModel.objects.order_by("-created_at")[start:start+post_no],'tops': BlogModel.objects.order_by("-created_at")[:3],'no':no,'view_op':view_op}
    return render(request, 'page.html', context)


def login_view(request):
    return render(request, 'login.html')


def blog_detail(request, slug):
    blogs = list(BlogModel.objects.all())
    random_blogs = random.sample(blogs,2)
    #context = {}
    next_post='0'
    try:
        blog_obj = BlogModel.objects.filter(slug=slug).first()
        if blog_obj:
            id=blog_obj.id
            print(id)
        else:
            print("Fuck")
        if id != BlogModel.objects.last().id:
            next_post = BlogModel.objects.filter(id=id+1).first()
        previous_post = BlogModel.objects.filter(id=id-1).first()
        print(previous_post.slug)
        
        blog_obj.views=blog_obj.views+1
        blog_obj.save()
        context = {'blog_obj':blog_obj,'previous_post':previous_post,'next_post':next_post,'random_blogs':random_blogs, 'tops': BlogModel.objects.order_by("-created_at")[:3]}
    except Exception as e:
        print(e)
    return render(request, 'blog.html', context)


def see_blog(request):
    context = {}

    try:
        blog_objs = BlogModel.objects.filter(user=request.user)
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)

    print(context)
    return render(request, 'see_blog.html', context)


def add_blog(request):
    context = {'form': BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            print(request.user)
            print(request.FILES.get('image', ''))
            image = request.FILES.get('image', '')
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                print('Valid')
                content = form.cleaned_data['content']

            blog_obj = BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image
            )
            print(blog_obj)
            return redirect('/add-blog/')
    except Exception as e:
        print(e)

    return render(request, 'add_blog.html', context)


def blog_update(request, slug):
    context = {}
    try:

        blog_obj = BlogModel.objects.get(slug=slug)

        if blog_obj.user != request.user:
            return redirect('/')

        initial_dict = {'content': blog_obj.content}
        form = BlogForm(initial=initial_dict)
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']

            blog_obj = BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image
            )

        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e:
        print(e)

    return render(request, 'update_blog.html', context)


def blog_delete(request, id):
    try:
        blog_obj = BlogModel.objects.get(id=id)

        if blog_obj.user == request.user:
            blog_obj.delete()

    except Exception as e:
        print(e)

    return redirect('/see-blog/')


def register_view(request):
    return render(request, 'register.html')


def verify(request, token):
    try:
        profile_obj = Profile.objects.filter(token=token).first()

        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e:
        print(e)

    return redirect('/')
