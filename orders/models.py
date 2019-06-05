from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    objects = models.Manager()
    spicy = models.CharField(max_length=200)
    sidemenus = models.CharField(max_length=200, blank=True, null=True)
    toppings = models.CharField(max_length=200, blank=True, null=True)
    drink = models.CharField(max_length=200, blank=True, null=True)
    
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def sidemenus_as_list(self):
        return self.sidemenus.split(', ')
    
    def toppings_as_list(self):
        return self.toppings.split(', ')
    
    def reviews(self):
        return Review.objects.filter(order=self)
    
    
class Review(models.Model):
    objects = models.Manager()
    content = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content