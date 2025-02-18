from django import forms
from .models import Article, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'categorie']