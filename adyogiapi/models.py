from django.db import models

# Create your models here.


class ProductType(object):
    DEV = 1
    PROD = 2


class Product(models.Model):
    PRODUCT_TYPE_CHOICES = (
        (ProductType.DEV, 'Development'),
        (ProductType.PROD, 'Production')
    )
    name = models.CharField(max_length=128, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    slug = models.CharField(max_length=32, null=True, blank=True)
    product_type = models.IntegerField(default=0, blank=True, null=True, choices=PRODUCT_TYPE_CHOICES)

    def __str__(self):
        return self.name