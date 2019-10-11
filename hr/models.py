from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    comission = models.DecimalField(max_digits=10, decimal_places=2, null=True  )
    Designatedid = models.DecimalField(max_digits=10, decimal_places=2 , null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1, null=True)

    def __str__(self):
        return self.name
