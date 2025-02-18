from django.urls import path
from articles.views import liste_articles, home, about, post, article_create, article_modify, article_delete
from .views import CommentCreateView

urlpatterns = [
    path('', home, name ='home'),
    path('posts/', liste_articles, name='liste-articles'),
    path('about/', about, name='about'),
    path('post/<int:id>', post, name='post'),
    path('posts//comment/', CommentCreateView.as_view(), name ='comment_create'),
    path('create/', article_create, name='article_create'),
    path('modify/<int:id>/', article_modify, name='article_modify' ),
    path('delete/<int:id>/', article_delete, name='article_delete')
]