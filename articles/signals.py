from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Article

@receiver(post_save, sender=Article)
def log_article_creation(sender, instance, created, **kwargs):
    """
    Yon signal pou montre yon mesaj nan konsòl la 
    chak fwa yo kreye yon nouvo atik.
    """
    if created:
        print(f"Nouveau article creer: {instance.title}")
    else:
        print(f"Article modifier : {instance.title}")