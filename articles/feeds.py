from django.contrib.syndication.views import Feed
from .models import Article

class LatestArticlesFeed(Feed):
    title = "OkayNews - Dernières actualités"
    link = "/rss/"
    description = "Les dernières nouvelles tech et articles d'actualité de OkayNews."

    def items(self):
        return Article.objects.order_by('-created_at')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]