from django.contrib.syndication.views import Feed
from django.urls import reverse
from home.models import NewsModel


class LatestEntriesFeed(Feed):
    title = "Automated News Website By Paras Gupta"
    link = "/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return NewsModel.objects.order_by("-created_at")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summary
        
    def item_link(self, item):
        return reverse("blog_detail", args=[item.slug])