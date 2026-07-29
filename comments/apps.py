from django.apps import AppConfig

class CommentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comments'  # Sa dwe 'comments', se sa ki korije erè a!
    verbose_name = 'Gestion des Commentaires'