from django.db import models
from model_utils import Choices
from django.core.validators import MaxValueValidator, MinValueValidator
from computed_property import ComputedTextField, ComputedFloatField




# Create your models here.

class Sub_category(models.Model):
    sub_category = models.CharField(max_length=400)
    shipping = models.FloatField(blank =True)
    commision = models.FloatField()

    def __str__(self):
        return self.sub_category



class Category(models.Model):
    category = models.CharField(max_length=200)


    def __str__(self):
        return self.category




class Product(models.Model):
    item = models.CharField(max_length=200)
    category = models.ForeignKey(Category,max_length= 200, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_category,max_length= 200,on_delete=models.CASCADE,related_name='cats',)
    price = models.FloatField()

    quantity = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1)])

    commision = ComputedFloatField(blank=True,compute_from='commision')
    shipping = ComputedFloatField(blank=True,compute_from='shipping')
    amount_expected = ComputedFloatField(blank=True,compute_from='amount_expected')

    @property
    def commision(self):
       return self.sub_category.commision/100*self.price


    @property
    def shipping(self):
       return self.sub_category.shipping

    @property
    def amount_expected(self):
        return (self.price-(self.shipping+self.commision))*self.quantity


    def __str__(self):
        return self.item



