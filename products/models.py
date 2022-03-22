"""classes and functions for products models can be found here"""
from django.db import models


class Category(models.Model):
    """Create category class"""

    class Meta:
        """Edit the default plural for category"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """Return name"""
        return self.name

    def get_friendly_name(self):
        """Return friendly name"""
        return self.friendly_name


class Product(models.Model):
    """Create product class"""
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """Return name"""
        return self.name
