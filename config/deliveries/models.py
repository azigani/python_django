from django.db import models

class Delivery(models.Model):
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    delivery_date = models.DateTimeField()
    status = models.CharField(max_length=50, default='Scheduled')

    def __str__(self):
        return f"Delivery for Order #{self.order.id}"
