from django.db import models


class CurrencyModel(models.Model):
    class Meta:
        db_table = "currency"
        ordering = ["id"]

    name = models.CharField(max_length=5)
    desc = models.CharField(max_length=20)

    sale_rate = models.DecimalField(decimal_places=7, max_digits=12, default=1)
    purchase_rate = models.DecimalField(decimal_places=7, max_digits=12, default=1)

    update_at = models.DateTimeField(auto_now=True)


class CurrencyPointModel(models.Model):
    class Meta:
        db_table = "currency_point"
        ordering = ["-date_point"]

    date_point = models.DateField(auto_now_add=True)
    currency = models.ForeignKey(CurrencyModel, on_delete=models.CASCADE, null=True, related_name="currency_point")
    sale_rate = models.DecimalField(decimal_places=7, max_digits=12, null=True)
    purchase_rate = models.DecimalField(decimal_places=7, max_digits=12, null=True)
    