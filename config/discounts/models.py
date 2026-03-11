from django.db import models

class Discount(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    is_percentage = models.BooleanField(default=True)

    def __str__(self):
        return self.name
