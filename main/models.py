from django.db import models
import uuid
from django.contrib.auth.models import User


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('ball', 'Ball'),
        ('accessories', 'Accessories'),
        ('equipment', 'Equipment'),
        ('training', 'Training'),
    ]
    
    name = models.CharField(max_length=255)
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name
    
    @property
    def is_available(self):
        return self.stock > 0
        
    def increment_stock (self):
        self.stock += 1
        self.save()

