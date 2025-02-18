from django.db import models

# Create your models here.
#Table article
class Article(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

#Table categorie
class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

#Table commentaire
class Comment(models.Model):
    article = models.ForeignKey('Article', related_name ='comments', on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.nom} on {self.article}'