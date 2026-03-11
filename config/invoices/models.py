from django.db import models

class Invoice(models.Model):
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    sale = models.ForeignKey('sales.Sale', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    issued_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=50, default='Pending')
    discount = models.ForeignKey('discounts.Discount', on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.ForeignKey('taxes.Tax', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Invoice #{self.id} for {self.client.name}"
