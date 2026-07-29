from django.db import models
from articles.models import Article
from mptt.models import MPTTModel, TreeForeignKey

class Comment(MPTTModel):
    # 'related_name' sa a se sa ki pèmèt nou fè article.comments.all() nan views.py
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    # Lojik pou kòmantè imbriqués (nested)
    parent = TreeForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='children'
    )

    class MPTTMeta:
        # Sa a asire kòmantè yo klase pa dat kreyasyon nan pyebwa a
        order_insertion_by = ['created_at']

    def __str__(self):
        return f'Kòmantè {self.body[:20]}... pa {self.name}'