from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'content', 'tags']
        
        # Ajoute widgets pou kontwole aparans fòm nan
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Antre tit atik la'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Ekri kontni atik la isit la...', 
                'rows': 10
            }),
            'tags': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Egzanp: teknoloji, nouvèl, ayiti'
            }),
        }

    # Ou ka ajoute etikèt (labels) si ou vle
    labels = {
        'title': 'Titre article',
        'category': 'Categorie',
        'content': 'contenu article',
        'tags': 'Etiquette (Tags)',
    }