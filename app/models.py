from django.db import models
from model_utils import Choices
from django.core.validators import MaxValueValidator, MinValueValidator
from computed_property import ComputedTextField, ComputedFloatField
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey





# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=200)


    def __str__(self):
        return self.category



class Sub_category(models.Model):
    category = models.ForeignKey(Category,max_length= 200, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=400)
    shipping = models.FloatField(blank =True)
    commision = models.FloatField()

    def __str__(self):
        return self.sub_category



class Product(models.Model):
    item = models.CharField(max_length=200)
    category = models.ForeignKey(Category,max_length= 200, on_delete=models.CASCADE)
    sub_category = ChainedForeignKey(
        Sub_category,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True,
        max_length= 200, on_delete=models.CASCADE)
    price = models.FloatField()
    vendor = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1)])

    commision = ComputedFloatField(blank=True,compute_from='commision')
    shipping = ComputedFloatField(blank=True,compute_from='shipping')
    amount_expected = models.FloatField(blank=True)



    @property
    def get_amount_expected(self):
      return (self.price-(self.shipping+self.commision))*self.quantity
    def save(self, *args, **kwargs):
      self.amount_expected = self.get_amount_expected
      super(Product, self).save(*args, **kwargs)

    def __float__(self):
       return self.amount_expected


    @property
    def commision(self):
       return self.sub_category.commision/100*self.price


    @property
    def shipping(self):
       return self.sub_category.shipping

    # @property
    # def amount_expected(self):
    #     return (self.price-(self.shipping+self.commision))*self.quantity


    def __str__(self):
        return self.item
