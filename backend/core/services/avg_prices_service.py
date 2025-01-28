from django.db.models import Avg, Count, F

from apps.cars.adverts.models import CarAdvertModel


def get_avg_prices(advert, user):
    avg_prices = {}
    if hasattr(user, "profile"):
        if user.profile.premium_acc:
            qs = ((CarAdvertModel.objects.filter(brand=advert.brand, mark=advert.mark))
                  .select_related("currency").values("currency__saleRate", "price")
                  .annotate(sum_as_UAH=F("currency__saleRate") * F("price")))

            if advert.region:
                avg_region = qs.filter(region=advert.region).aggregate(avg_price_region=Avg("sum_as_UAH"),
                                                                       counter=Count("price"))

            if advert.city:
                avg_city = qs.filter(city=advert.city).aggregate(avg_price_city=Avg("sum_as_UAH"),
                                                                 counter=Count("price"))

            avg_all = qs.aggregate(avg_price_all=Avg("sum_as_UAH"), counter=Count("price"))

            avg_prices["ccy"] = advert.currency.name
            avg_prices["avg_all"] = round(avg_all["avg_price_all"] / advert.currency.saleRate, 0)

    return avg_prices
