from rest_framework import serializers

from apps.currency.models import CurrencyModel, CurrencyPointModel


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyModel
        fields = (
            "name", "sale_rate", "purchase_rate"
        )
        read_only_fields = ('name', 'saleRate', 'purchaseRate')

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs["name"] = self.context["name"]
        attrs["sale_rate"] = self.context["sale_rate"]
        attrs['purchase_rate'] = self.context["purchase_rate"]
        return attrs


class CurrencyPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyPointModel
        fields = (
            "date_point", "currency", "sale_rate", "purchase_rate",
        )
