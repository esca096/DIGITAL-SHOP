from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_added']
        
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
    
    def __str__(self):
        return self.name
    


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categorie')
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['-date_added']
        
    def __str__(self):
        return self.title
    

class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_commande']
        
    def __str__(self):
        return self.nom
    