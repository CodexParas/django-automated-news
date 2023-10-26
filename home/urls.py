from django.urls import path
from .views import *
from . import views
from django.views.generic import RedirectView
urlpatterns = [
    path('', home, name="home"),
    path('page/<no>', page, name="page"),
    path('news/<slug>', blog_detail, name="blog_detail")
]