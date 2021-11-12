from django.db import models

# Create your models here.
FOOD_STYLES = (
    ('North Indian','North Indian'),
    ('South Indian','South Indian'),
    ('Chinese','Chinese'),
)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    Mobilenumber = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    foodstyle =models.CharField(max_length=50)
    preference = models.CharField(choices=FOOD_STYLES,max_length=50)
    opinion =models.TextField(max_length=100)
    # date = models.DateField()

    def __str__(self):
      return  self.name
