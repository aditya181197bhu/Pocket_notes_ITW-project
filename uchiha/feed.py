from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import *
class LatestEntriesFeed(Feed):
    title = "Latest Notes "
    link = "/sitenews/"
    description = "Most important subjects links."

    def items(self):
        return Notes4.objects.order_by('-created_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.subject

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('comm')