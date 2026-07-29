from django.apps import AppConfig

class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articles'
    verbose_name = 'Gestion des Articles'

    def ready(self):
        # Sa a enpòtan pou Signal yo ka aktive lè sèvè a kòmanse
        import articles.signals