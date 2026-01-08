from django.db import models

# Create your models here.


class Tv(models.Model):
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=120)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model} - {self.make}"