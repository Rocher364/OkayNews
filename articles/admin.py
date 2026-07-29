from django.contrib import admin
from .models import Article, Category, Newsletter, ContactMessage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Ranpli slug otomatikman baze sou non an
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')
    search_fields = ('name',)
    list_per_page = 20

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'created_at')
    list_editable = ('category',)
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    list_per_page = 20

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added')
    search_fields = ('email',)
    list_per_page = 50

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    # 'message' ajoute nan list_display pou w ka li l dirèkteman
    list_display = ('nom', 'email', 'message', 'date_envoi')
    # Pèmèt rechèch sou non ak imèl
    search_fields = ('nom', 'email')
    # Pou pa modifye mesaj yo nan admin (sekirite)
    readonly_fields = ('nom', 'email', 'message', 'date_envoi')
    list_per_page = 20