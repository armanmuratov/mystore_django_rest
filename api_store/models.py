from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    store = models.ManyToManyField(Store)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    update_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.name


    