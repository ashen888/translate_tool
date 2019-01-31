from django.db import models

# Create your models here.
class ashen(models.Model):
    name = models.CharField(max_length=12)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    hobby = models.CharField(max_length=36)

    def __str__(self):
        return self.name
