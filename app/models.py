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

    @property
    def commision(self):
       return self.sub_category.commision/100*self.price




    # def _get_shipping(self):
    #
    #       return self.sub_category.shipping
    # shipping = property(_get_shipping)

    @property
    def shipping(self):
       return self.sub_category.shipping




    # def _get_total(self):
    #
    #       return (self.price-(self.shipping+self.commision))*self.quantity
    # total = property(_get_total)



    def __str__(self):
        return self.item
    
for instance in Product.objects.all().iterator():
      instance.save()
