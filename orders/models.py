from django.db import models

# Create your models here.
class OrdersTable(models.Model):
    username = models.CharField(blank=True , max_length=20)
    quantity = models.IntegerField(blank=True)

    class Meta:
        db_table = "orders_table"