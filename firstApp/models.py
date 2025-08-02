from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name

class Chef(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='chefs/')
    bio = models.TextField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Food(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='foods/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='foods')
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, related_name='foods')
    is_on_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name
