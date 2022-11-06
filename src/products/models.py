from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    summery = models.TextField(blank=True, null=False)
    isactive = models.BooleanField(default=True)


    def get_abs_url(self):
        return reverse("products:detail", kwargs={"id": self.id})