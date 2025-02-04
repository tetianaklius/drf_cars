from django.db import models


class IpAddressModel(models.Model):
    class Meta:
        db_table = "ip_address"

    ip = models.CharField(max_length=20)


class VisitCountModel(models.Model):
    class Meta:
        db_table = "visit_count"
        ordering = ["-created_at"]

    ip = models.ForeignKey(IpAddressModel, on_delete=models.CASCADE, related_name="visits", null=True)
    user = models.IntegerField(null=True)
    advert = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
