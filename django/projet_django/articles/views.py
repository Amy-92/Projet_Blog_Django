from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Article, Comment
from django.views.generic.edit import CreateView
from django.urls import reverse
from .forms import PostForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def liste_articles(request):
    articles = Article.objects.all()
    return render(request, 'liste.html', {'articles': articles})

def about(request):
    return render (request, 'about.html')

def post(request, id):
    specific_post = Article.objects.get(id=id)
    return render(request, 'post_detail.html', {'article': specific_post})

class CommentCreateView(CreateView):
    model = Comment
    fields = ['nom', 'contenu']
    template_name = 'comment_form.html'

    def form_valid(self, form):
        form.instance.article_id = self.kwargs['id'] # Associer le commentaire à l'article
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article', kwargs={'id': self.kwargs['id']}) # Rediriger vers l'article après soumission
    
def article_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save() #Enregistrement en base
            return  redirect('liste-articles')
    else:
        form = PostForm()
    return render(request, 'article_form.html' , {'form':form})

def article_modify(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = article)
        if form.is_valid():
            form.save()
            messages.success(request, 'L\'article a ete modifie avec succes')
            return redirect('liste-articles')
    else:
        form = PostForm(instance = article)
    return render(request, 'modifier_article.html', {'form': form, 'article': article})

def article_delete(request ,id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'L\'article a ete supprime avec succes')
        return redirect('liste-articles')
    return render(request, 'supprimer_article.html', {'article': article})
