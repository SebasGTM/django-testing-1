from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    create_date = models.DateField()
    isactive = models.BooleanField(default=True)

    def get_absolute_url(self):
        reverse("articles:article-details", kwargs={"id": self.id})