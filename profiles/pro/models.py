from django.db import models

# Create your models here.
class Pro(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    country = models.CharField(max_length=20)

    def _str_(self):
        return self.full_name
