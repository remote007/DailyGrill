from django.db import models

# Create your models here.
class ProductsTable(models.Model):
    name = models.CharField(blank=True , max_length=20)
    price = models.FloatField(blank=True)

    class Meta:
        db_table = "products_table"