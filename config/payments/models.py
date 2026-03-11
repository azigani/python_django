
from django.db import models

class Payment(models.Model):
	user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	method = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Payment by {self.user.username}"
