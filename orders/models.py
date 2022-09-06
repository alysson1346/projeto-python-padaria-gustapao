from django.db import models
import uuid

#ORDER
class Order(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
  withdrawal_date = models.DateTimeField()
  comment = models.TextField()
  is_finished = models.BooleanField(default=False, null=True)
  total = models.DecimalField(max_digits=10, decimal_places=2)

  account = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name="orders")
  products = models.ManyToManyField("products.Product", on_delete=models.CASCADE, related_name="orders")
