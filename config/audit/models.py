
from django.db import models

class AuditLog(models.Model):
	action = models.CharField(max_length=100)
	user = models.CharField(max_length=100)
	timestamp = models.DateTimeField(auto_now_add=True)
	details = models.TextField(blank=True)

	def __str__(self):
		return f"{self.action} by {self.user}"
