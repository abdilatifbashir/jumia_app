from django.db import models
from model_utils import Choices
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Product(models.Model):
    item_name = models.CharField(max_length=200)
    cat_choice =Choices(
        (0, 'tv', 'tv'),
        (1, 'phone', 'phone'),
        (2, 'sound', 'sound'),
      )
    cat = models.IntegerField(choices=cat_choice)
    price = models.FloatField(validators=[MinValueValidator(1)])
    quantity =models.PositiveIntegerField(default=1,validators=[MinValueValidator(1)])
    total = models.FloatField()





    @property
    def get_total(self):
       if self.cat == 0:
         return self.price*0.95*self.quantity
       elif self.cat == 1:
          return self.price*0.96*self.quantity
       elif self.cat ==2:
           return self.price*0.97*self.quantity
    def save(self, *args, **kwargs):
      self.total = self.get_total
      super(Product, self).save(*args, **kwargs)

    def __float__(self):
       return self.total

    def _get_commision(self):
        if self.cat == 0:
          return self.price-self.price*0.95
        elif self.cat == 1:
          return self.price-self.price*0.96
        elif self.cat == 2:
          return self.price-self.price*0.97
    commision =property(_get_commision)


    def __str__(self):
        return self.item_name
