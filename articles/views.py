from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.conf import settings

# Enpòtasyon modèl yo
from .models import Article, Category, Newsletter, ContactMessage

# --- KOREKSYON ICI: Enpòtasyon depi aplikasyon comments ---
from comments.models import Comment
from comments.forms import CommentForm

# --- Paj Piblik ---

def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    
    # Jwenn kòmantè yo (Asire w ou gen related_name='comments' nan modèl Comment an)
    comments = article.comments.all() 
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
            messages.success(request, "Kòmantè w la byen afiche!")
            return redirect('article_detail', slug=article.slug)
    else:
        comment_form = CommentForm()
    
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'articles/article_detail.html', context)

# ... (Rete fonksyon yo pa chanje)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = category.articles.all().order_by('-created_at')
    return render(request, 'articles/article_list.html', {'articles': articles, 'category': category})

def search_articles(request):
    query = request.GET.get('q', '')
    articles = Article.objects.all()
    if query:
        articles = articles.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).distinct()
    return render(request, 'articles/article_list.html', {'articles': articles, 'query': query})

def newsletter_subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email and "@" in email and "." in email:
            obj, created = Newsletter.objects.get_or_create(email=email)
            if created:
                messages.success(request, "Mèsi! Ou byen anrejistre.")
            else:
                messages.info(request, "Ou deja abòne.")
        else:
            messages.error(request, "Tanpri antre yon imèl ki valab.")
    return redirect('article_list')

# --- Paj Legal ak Pèsonèl ---

def confidentialite_view(request):
    return render(request, 'legal/confidentialite.html', {'title': 'Confidentialité'})

def conditions_view(request):
    return render(request, 'legal/conditions.html', {'title': 'Conditions d\'utilisation'})

def about_view(request):
    return render(request, 'pages/about.html', {'title': 'À propos de OkayNews'})

def contact_view(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if nom and email and message:
            ContactMessage.objects.create(nom=nom, email=email, message=message)
            try:
                send_mail(
                    f"Nouveau messsage: {nom}",
                    f"Email: {email}\n\n{message}",
                    settings.DEFAULT_FROM_EMAIL,
                    ['admin@okaynews.com'],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Erreur email: {e}")
            messages.success(request, "Messsage envoyes avec succes!")
            return redirect('contact')
        else:
            messages.error(request, "Remplier tout les jardins.")
    return render(request, 'legal/contact.html')

# --- Fonksyon Jesyon Admin & Sekirite ---

def logout_view(request):
    logout(request)
    messages.info(request, "connection avec succes.")
    return redirect('article_list')

@staff_member_required
def admin_dashboard_view(request):
    return render(request, 'admin/dashboard.html')