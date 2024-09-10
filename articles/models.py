from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    somary = models.CharField(max_length=255, blank=False,null=True)
    content = models.TextField()
    date_pu = models.DateField(null=True)
    image = models.ImageField(upload_to='articles/', null=True, blank=False)
    # auteur = models.CharField(max_length=100, null=True, blank=False)  
    date_modification = models.DateTimeField(auto_now=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Commentaire de {self.author} sur {self.article.title}'
    
