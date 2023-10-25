from django.urls import path
from .views import *
from . import views
from django.views.generic import RedirectView
urlpatterns = [
    path('', home, name="home"),
    path('page/<no>', page, name="page"),
    path('login/', login_view, name="login_view"),
    path('register/', register_view, name="register_view"),
    path('add-blog/', add_blog, name="add_blog"),
    path('news/<slug>', blog_detail, name="blog_detail"),
    path('see-blog/', see_blog, name="see_blog"),
    path('blog-delete/<id>', blog_delete, name="blog_delete"),
    path('blog-update/<slug>/', blog_update, name="blog_update"),
    path('logout-view/', logout_view, name="logout_view"),
    path('verify/<token>/', verify, name="verify"),
    path(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),

]
