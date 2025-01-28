import datetime as dt

from django.core.exceptions import MultipleObjectsReturned

from apps.visits_count.models import IpAddressModel, VisitCountModel


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def visit_add(request, advert):
    ip = get_client_ip(request)
    user = request.user

    ip_obj, created = IpAddressModel.objects.get_or_create(ip=ip)

    # варіант, де лише один перегляд зараховується для цього користувача з цієї IP-адреси для конкретного оголошення
    # try:
    #     obj, created = VisitCountModel.objects.get_or_create(ip=ip_obj, advert=advert, user=user.id)
    # except MultipleObjectsReturned:
    #     print("Багато записів з цієї IP")

    # варіант, де на кожне оновлення сторінки додається перегляд
    VisitCountModel.objects.create(ip=ip_obj, advert=advert, user=user.id)


def get_visit_count(advert, user):
    counter = {"count_all": 0, "count_day": 0, "count_week": 0, "count_month": 0}

    if hasattr(user, "profile"):
        if user.profile.premium_acc:
            qs = VisitCountModel.objects.filter(advert=advert)

            today_datetime = dt.datetime.today()

            counter["count_all"] = qs.count()
            counter["count_day"] = qs.filter(created_at__gte=today_datetime - dt.timedelta(hours=24)).count()
            counter["count_week"] = qs.filter(created_at__gte=today_datetime - dt.timedelta(days=7)).count()
            counter["count_month"] = qs.filter(created_at__gte=today_datetime - dt.timedelta(days=30)).count()

    return counter
