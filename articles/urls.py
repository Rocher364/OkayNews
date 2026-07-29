from django.urls import path
from . import views
from .feeds import LatestArticlesFeed
from django.urls import path, include

urlpatterns = [
    # Paj Akèy (Lis atik yo)
    path('', views.article_list, name='article_list'),
    
    # Detay yon atik
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    
    # Detay yon kategori
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    
    # Rechèch
    path('search/', views.search_articles, name='search_articles'),
    
    # RSS Feed ak Newsletter
    path('feed/', LatestArticlesFeed(), name='article_feed'),
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    
    # Paj Legal ak Enfòmasyon
    path('confidentialite/', views.confidentialite_view, name='confidentialite'),
    path('conditions/', views.conditions_view, name='conditions'),
    path('contact/', views.contact_view, name='contact'),
    path('a-propos/', views.about_view, name='about'),

    # Sekirite: Wout pou Dekoneksyon
    path('logout/', views.logout_view, name='logout'),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
]