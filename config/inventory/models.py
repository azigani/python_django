
from django.db import models

class InventoryItem(models.Model):
	product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
	quantity = models.IntegerField()
	location = models.CharField(max_length=100)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.product.name} at {self.location}"
