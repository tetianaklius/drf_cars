import datetime as dt

from apps.currency.models import CurrencyModel


def get_currency_points():
    query_set = CurrencyModel.objects.all()[1:3]
    points = []
    for item in query_set:
        points.append({
            "currency_id": item.id,
            "currency_name": item.name,
            'sale_rate': item.saleRate,
            'purchase_rate': item.purchaseRate,
            "currency_point_date": item.update_at.strftime("%m/%d/%Y, %H:%M:%S"),
        })
    return points


def point_is_actual():
    last_point = CurrencyModel.objects.all()
    point = False

    if last_point:
        point = True
        if dt.datetime.now().hour >= 10:
            res = last_point[1].update_at
            last_date_point = dt.date(res.year, res.month, res.day)

            today = dt.date.today()
            if last_date_point == today:
                point = True
            else:
                point = False

    return point


def get_calculated_prices(price, currency_id):
    points = list(CurrencyModel.objects.all())

    prices = [{"UAH": 0},
              {"USD": 0},
              {"EUR": 0}]

    match currency_id:
        case 1:  # UAH
            prices = [{"UAH": price},
                      {"USD": round(price / points[1].sale_rate, 0)},
                      {"EUR": round(price / points[2].sale_rate, 0)}]
        case 2:  # USD
            prices = [{"USD": price},
                      {"UAH": round(price * points[1].sale_rate, 0)},
                      {"EUR": round(price * points[1].sale_rate / points[2].sale_rate, 0)}]
        case 3:  # EUR
            prices = [{"EUR": price},
                      {"UAH": round(price * points[2].sale_rate, 0)},
                      {"USD": round(price * points[2].sale_rate / points[1].sale_rate, 0)}]

    return prices
