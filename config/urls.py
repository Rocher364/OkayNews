from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from articles.sitemaps import ArticleSitemap
from articles.feeds import LatestArticlesFeed
from django.contrib.sitemaps.views import sitemap as sitemap_view

# Konfigirasyon Sitemap
sitemaps = {
    'articles': ArticleSitemap,
}

urlpatterns = [
    # Wout Admin
    path('admin/', admin.site.urls),
    
    # CKEditor 5 wout (obligatwa pou imaj yo)
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    
    # RSS Feed ak Sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('rss/', LatestArticlesFeed(), name='rss_feed'),
    
    # Wout lang
    path('i18n/', include('django.conf.urls.i18n')),
    
    
]

# Rès URL pwojè a (Articles, Comments, etc.)
urlpatterns += [
    path('', include('articles.urls')),
]

# Jere imaj yo nan mòd devlopman
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)