from django.urls import path
from .views import *
from . import views
from django.views.generic import RedirectView
from News.feeds import LatestEntriesFeed
urlpatterns = [
    path('', home, name="home"),
    path('page/<no>', page, name="page"),
    path('news/<slug>', blog_detail, name="blog_detail"),
    path('category/<cat>', category_view, name="category_view"),
    path("feed/", LatestEntriesFeed()),
    path("error",error,name='error')
]