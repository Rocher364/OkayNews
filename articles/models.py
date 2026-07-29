from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field
from taggit.managers import TaggableManager

# 1. Modèl Kategori
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

# 2. Modèl Atik
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    content = CKEditor5Field('Content', config_name='default')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    # Metòd sa a obligatwa pou Sitemap
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

# 3. Modèl Newsletter
class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

# 4. Modèl ContactMessage
class ContactMessage(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_envoi'] 

    def __str__(self):
        return f"Message de {self.nom} - {self.email}"